from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, HTTPException, File, UploadFile
import uvicorn
import PredictionModel
import os

app = FastAPI()

# 配置 CORS 中间件，允许跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应指定允许的前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义 GET 请求接口
@app.get("/get")
def get_data():
    return {"Cumulative_Mileage": "get方法"}

# 定义 POST 请求接口用于预测
@app.post("/post")
def post_data(
    cumulative_mileage: str = Form(...),  # 累计里程
    vehicle_speed: str = Form(...),       # 车速
    total_voltage: str = Form(...),       # 总电压
    total_current: str = Form(...),       # 总电流
    power_consumption: str = Form(...),   # 功率
    vehicle_status: str = Form(...),      # 车辆状态
    charging_status: str = Form(...),     # 充电状态
    operating_mode: str = Form(...),      # 运行模式
    fault_level: str = Form(...),         # 故障等级
    fault_rate: str = Form(...),          # 故障率
    DCDC_Status: str = Form(...),         # DC-DC状态
    insulation_resistance: str = Form(...),  # 绝缘电阻
    maximumBattery_Voltage: str = Form(...),  # 电池单体电压最高值
    minimumBattery_Voltage: str = Form(...),  # 电池单体电压最低值
    maximum_temperature: str = Form(...),     # 最高温度值
    minimum_temperature: str = Form(...),     # 最低温度值
):
    try:
        # 加载训练好的模型
        model = PredictionModel.load_model()

        # 定义输入数据并进行类型转换
        input_data = {
            '累计里程': float(cumulative_mileage),
            '车速': float(vehicle_speed),
            '总电压': float(total_voltage),
            '总电流': float(total_current),
            '功率': float(power_consumption),
            '车辆状态': float(vehicle_status),
            '充电状态': float(charging_status),
            '运行模式': float(operating_mode),
            '故障等级': float(fault_level),
            '故障率': float(fault_rate),
            'DC-DC状态': float(DCDC_Status),
            '绝缘电阻': float(insulation_resistance),
            '电池单体电压最高值': float(maximumBattery_Voltage),
            '电池单体电压最低值': float(minimumBattery_Voltage),
            '最高温度值': float(maximum_temperature),
            '最低温度值': float(minimum_temperature)
        }
        
        # 预测 SOC（电池剩余电量）值
        predicted_soc = PredictionModel.predict_soc(model, input_data)
        return {"SOC": predicted_soc}
    
    except Exception as e:
        # 如果发生异常，返回 HTTP 500 错误
        raise HTTPException(status_code=500, detail=str(e))

# 定义 POST 请求接口用于上传 CSV 文件并进行模型训练
@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...), target_column: str = Form(...)):
    try:
        # 保存上传的文件
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        
        # 运行线性回归模型训练
        r2, mse = PredictionModel.run_linear_regression(file_location, target_column)
        
        # 删除临时文件
        os.remove(file_location)
        
        return {"R2 Score": r2, "Mean Squared Error": mse}
    
    except Exception as e:
        # 如果发生异常，返回 HTTP 500 错误
        raise HTTPException(status_code=500, detail=str(e))

# 运行应用程序
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=2024, reload=True)
