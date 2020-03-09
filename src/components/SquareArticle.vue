<template>
  <div>
    <el-row>
      <el-row>
        <div>
          <el-link class="title">
            <h1>标题</h1>
          </el-link>
        </div>
        <div>
          <span>发表于</span>
          <el-link type="primary" class="time">
            <div>时间</div>
          </el-link>
          <span>由</span>
          <el-link type="primary" class="author">
            <div>作者</div>
          </el-link>
        </div>
      </el-row>
      <el-row>
        <el-image src fit="contain">
          <div slot="error" class="image-slot">
            <i class="el-icon-picture-outline"></i>
          </div>
        </el-image>
      </el-row>
      <el-row>
        <el-link type="primary" class="tag">
          <div>标签</div>
        </el-link>
      </el-row>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imagesrc: "https://hacg.tw/wp/wp-content/uploads/2020/03/021.jpg",
      titleurl: "#",
      timerul: "#",
      authorurl: "#",
      tagurl: "#"
    };
  }
};
</script>

