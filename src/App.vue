<template>
  <div id="app" v-loading.fullscreen.lock="loading">
    <!-- <el-col :span="4" style="float: left;">
      <SquareGuid />
    </el-col>
    <el-col :span="20" v-loading.fullscreen.lock="loading">
      <router-view></router-view>
    </el-col>-->

    <el-container>
      <el-header id="headerContent">
        <SquareGuid />
      </el-header>

      <el-main id="mainConent">
        <router-view></router-view>
      </el-main>
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
// import $ from "jquery";

export default {
  name: "App",
  data() {
    return {
      // ex: true
    };
  },

  components: {
    SquareGuid
    // SquareLoading
  },

  computed: {
    ...mapState(["loading"])
  }

  // watch: {
  //   loading: function(val) {
  //     if (val) {
  //       $(".loading").show();
  //     }
  //     $(".loading").hide();
  //   }
  // }
};
</script>

<style>
/* .loading {
  position: absolute;
  top: 300px;
  left: 900px;
} */

#headerContent {
  min-width: 620px;
  width: 100%;
  height: auto;
  padding: 0;
  position: fixed;

  z-index: 1;
}

#mainConent {
  width: 60%;
  min-width: 620px;
  min-height: 800px;
  background-color: aliceblue;
  opacity: 0.8;
  margin: auto;
  margin-top: 80px;
}
</style>
