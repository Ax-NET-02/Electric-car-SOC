<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <el-col :span="20">
          <el-menu
            default-active="/predict"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
            router
          >
            <el-menu-item index="/predict">
              <el-icon><icon-menu /></el-icon>
              <span>预测</span>
            </el-menu-item>

            <el-menu-item index="/train">
              <el-icon><setting /></el-icon>
              <span>模型训练</span>
            </el-menu-item>
          </el-menu>
        </el-col>
      </el-aside>
      <el-container>
        <el-header></el-header>
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};

const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
</script>

<style scoped>
.common-layout {
  height: 100vh;
}
</style>
