import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import joblib

def run_linear_regression(data_path, target_column, test_size=0.3, random_state=42):
    # 读取数据
    data = pd.read_csv(data_path)
    # 准备特征数据和目标数据
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    # 初始化多元线性回归模型
    model = LinearRegression()
    # 在训练集上训练模型
    model.fit(X_train, y_train)
    # 在测试集上进行预测
    y_pred = model.predict(X_test)
    # 计算模型R^2得分和均方误差
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print("模型R^2得分:", r2)
    print("模型均方误差:", mse)
    # 保存训练好的模型到文件
    joblib.dump(model, 'linear_regression_model.pkl')
    return r2, mse

def load_model():
    # 加载训练好的模型
    return joblib.load('linear_regression_model.pkl')

def predict_soc(model, input_data):
    # 将输入的数据转换为 DataFrame
    input_df = pd.DataFrame([input_data],
                            columns=['累计里程', '车速', '总电压', '总电流', '功率', '车辆状态', '充电状态', '运行模式', '故障等级', '故障率', 'DC-DC状态',
                                     '绝缘电阻', '电池单体电压最高值', '电池单体电压最低值', '最高温度值', '最低温度值'])
    # 进行预测
    soc_prediction = model.predict(input_df)
    # 返回预测结果，四舍五入到最近的整数
    return float(soc_prediction[0].round())
