<template>
  <div>
    <el-row>
      <el-col :span="12" :offset="4">
        <SquareArticle></SquareArticle>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import SquareArticle from "./../components/SquareArticle";

export default {
  data() {
    return {
      value: ""
    };
  },

  components: {
    SquareArticle
  }
};
</script>
