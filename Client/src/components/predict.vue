<script lang="ts" setup>
import { ElNotification } from "element-plus";
import { reactive } from "vue";
import { ref } from 'vue'
import type { UploadInstance } from 'element-plus'

// do not use same name with ref
const form = reactive({
  cumulative_mileage: "",
  vehicle_speed: "",
  total_voltage: "",
  total_current: "",
  power_consumption: "",
  vehicle_status: "",
  operating_mode: "",
  fault_level: "",
  fault_rate: "",
  DCDC_Status: "",
  insulation_resistance: "",
  maximumBattery_Voltage: "",
  minimumBattery_Voltage: "",
  maximum_temperature: "",
  minimum_temperature: "",
  SelectModel: "",
});

const onSubmit = () => {
  ElNotification({
    title: "Error",
    message: "This is an error message",
    type: "error",
  });
};

const uploadRef = ref<UploadInstance>()

const submitUpload = () => {
  uploadRef.value!.submit()
}
</script>

<template>
  <el-form :model="form" label-width="auto" style="margin-left: 9%;">
    <el-row :gutter="20">
      <el-col :span="12">
        <div class="grid-content">
          <el-form-item label="模型选择">
            <el-select v-model="form.SelectModel" placeholder="请选择使用的模型">
              <el-option label="预测SOC.pkl" value="PredictingSOC"></el-option>
              <el-option label="预训练模型.pkl" value="Pre-training"></el-option>
            </el-select>
          </el-form-item>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content" style="margin-left: 20%">
          <el-upload ref="uploadRef" class="upload-demo"
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15" :auto-upload="false">
            <template #trigger>
              <el-button type="primary">选择模型</el-button>
            </template>

            <el-button class="ml-3" type="success" @click="submitUpload" style="margin-left: 2%;">
              上传模型
            </el-button>

            <template #tip>
              <div class="el-upload__tip">
                上传.pkl后缀的模型文件
              </div>
            </template>
          </el-upload>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="12">
    <el-col :span="6">
      <div class="grid-content">
        <el-form-item label="累计里程">
          <el-input v-model="form.cumulative_mileage" />
        </el-form-item>
      </div>
    </el-col>

    <el-col :span="6">
      <div class="grid-content">
        <el-form-item label="车速">
          <el-input v-model="form.vehicle_speed" />
        </el-form-item>
      </div>
    </el-col>
    </el-row>
    <el-row :gutter="12">
      <el-col :span="6">
      <div class="grid-content">
        <el-form-item label="总电压">
          <el-input v-model="form.total_voltage" />
        </el-form-item>
      </div>
    </el-col>

    <el-col :span="6">
      <div class="grid-content">
        <el-form-item label="总电流">
          <el-input v-model="form.total_current" />
        </el-form-item>
      </div>
    </el-col>
    </el-row>
  </el-form>
</template>

<style scoped>
.submit-button {
  margin-left: auto;
  /* 自动调整左边距，使按钮右对齐 */
  display: block;
  /* 确保按钮为块级元素 */
}

.el-row {
  margin-bottom: 20px;
}

.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}

.fixed-aside {
  height: 100%;
}

.main-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.header {
  flex: 0 0 auto;
}

.main-content {
  flex: 1 1 auto;
  overflow: hidden; /* Hide the scrollbars */
}
</style>