<script setup lang="ts">

import { reactive } from "vue";
import { UploadFilled } from '@element-plus/icons-vue'

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
csvData: "",
Modelselection: "",
});

</script>

<template>
    <el-upload
      class="upload-demo"
      drag
      action="https://127.0.0.1:2024/upload-csv"
      multiple
    >
      <el-icon class="el-icon--upload"><upload-filled /></el-icon>
      <div class="el-upload__text">
        将文件拖放到此处或单击 <em>上传</em>
      </div>
      <template #tip>
        <div class="el-upload__tip">
          请上传一个CSV格式的数据集
        </div>
      </template>
    </el-upload>

    <el-form :model="form" label-width="auto" style="margin-top: 4%;">
    <el-row :gutter="20">
      <el-col :span="12">
        <div class="grid-content">
          <el-form-item label="数据集选择">
            <el-select v-model="form.csvData" placeholder="请选择使用的数据集">
              <el-option label="预测SOC数据集.csv" value="predictSOC"></el-option>
              <el-option label="预训练数据集.csv" value="predictSET"></el-option>
            </el-select>
          </el-form-item>
        </div>
      </el-col>

      <el-col :span="12">
        <div class="grid-content">
          <el-form-item label="训练模型选择">
            <el-select v-model="form.Modelselection" placeholder="请选择使用的训练模型">
              <el-option label="线性回归[Linear Regression]" value="LinearRegression"></el-option>
              <el-option label="支持向量机[SVM, Support Vector Machine]" value="SVM"></el-option>
              <el-option label="随机森林[Random Forest]" value="RandomForest"></el-option>
            </el-select>
          </el-form-item>
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="12">
      <el-col :span="6">
        <div class="grid-content">
          <el-form-item label="测试集数据占比">
            <el-input v-model="form.cumulative_mileage">
              <template #append>test_size</template>
            </el-input>
          </el-form-item>
        </div>
      </el-col>

      <el-col :span="6">
        <div class="grid-content">
          <el-form-item label="随机性">
            <el-input v-model="form.cumulative_mileage">
              <template #append>random_state</template>
            </el-input>
          </el-form-item>
        </div>
      </el-col>
    </el-row>
    </el-form>
  </template>
  