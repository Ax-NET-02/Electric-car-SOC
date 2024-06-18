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
  </template>
  
  <script setup lang="ts">
  import { UploadFilled } from '@element-plus/icons-vue'
  </script>
  