<template>
  <div id="app">
    <el-col :span="4">
      <SquareGuid />
    </el-col>
    <el-col :span="20">
      <router-view></router-view>
    </el-col>

    <div v-if="loading">
      <SquareLoading class="loading"></SquareLoading>
    </div>
  </div>
</template>

<script>
import SquareGuid from "./components/SquareGuid.vue";
import SquareLoading from "./components/SquareLoading.vue";
import { mapState } from "vuex";
import $ from "jquery";

export default {
  name: "App",
  data() {
    return {
      ex: true
    };
  },

  components: {
    SquareGuid,
    SquareLoading
  },

  computed: {
    ...mapState(["loading"])
  },

  watch: {
    loading: function(val) {
      if (val) {
        $(".loading").show();
      }
      $(".loading").hide();
    }
  }
};
</script>

<style>
.loading {
  position: absolute;
  top: 300px;
  left: 900px;
}
</style>
