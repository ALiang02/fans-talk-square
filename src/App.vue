<template>
  <div id="app">
    <!-- <el-container>
      <el-aside width="200px">
        <hello-world />
      </el-aside>
      <el-main>
        <square-center />
      </el-main>
    </el-container>-->

    <el-row>
      <el-col :span="4">
        <SquareGuid />
      </el-col>
      <el-col :span="20">
        <router-view />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import SquareGuid from "./components/SquareGuid.vue";

export default {
  name: "App",
  components: {
    SquareGuid
  }
};
</script>

<style>
</style>
