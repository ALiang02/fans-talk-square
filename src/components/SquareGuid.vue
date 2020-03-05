<template>
  <div>
    <el-col>
      <el-menu default-active="1" class="el-menu-vertical-demo" router>
        <el-menu-item index="SquareCenter">
          <i class="el-icon-location"></i>
          <span slot="title">广场</span>
        </el-menu-item>
        <el-menu-item index="PersonalCenter">
          <i class="el-icon-user"></i>
          <span slot="title">个人</span>
        </el-menu-item>

        <el-menu-item index="SquareWallPaper">
          <i class="el-icon-picture"></i>
          <span slot="title">壁纸</span>
        </el-menu-item>
        <el-menu-item index="SquareLive">
          <i class="el-icon-service"></i>
          <span slot="title">网页小人</span>
        </el-menu-item>

        <el-menu-item index="PersonalSetting">
          <i class="el-icon-setting"></i>
          <span slot="title">设置</span>
        </el-menu-item>
        <el-menu-item index="SquareInfo">
          <i class="el-icon-info"></i>
          <span slot="title">关于</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </div>
</template>

<script>
export default {};
</script>

<style >
</style>
