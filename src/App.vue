<template>
  <div id="app" v-loading.fullscreen.lock="loading">
    <!-- <el-col :span="4" style="float: left;">
      <SquareGuid />
    </el-col>
    <el-col :span="20" v-loading.fullscreen.lock="loading">
      <router-view></router-view>
    </el-col>-->

    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="60">
          <SquareGuid />
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>

    <!-- <div v-if="loading">
      <SquareLoading class="loading"></SquareLoading>
    </div>-->
  </div>
</template>

<script>
import SquareGuid from "./components/SquareGuid.vue";
// import SquareLoading from "./components/SquareLoading.vue";
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
    SquareGuid
    // SquareLoading
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
