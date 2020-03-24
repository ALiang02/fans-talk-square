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
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
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

import store from "./store";

import Cookie from "js-cookie";

// import $ from "jquery";
// import imgsrc from "./assets/2.png";

export default {
  name: "App",
  data() {
    return {};
  },

  components: {
    SquareGuid

    // SquareLoading
  },

  computed: {
    ...mapState(["loading"])
  },

  methods: {
    live2dLoad() {
      var live2d = document.createElement("script"); // 创建script标签;
      live2d.type = "text/javascript"; // 设置type属性;
      live2d.src = "http://118.178.94.45:8080/live2d/live2d-widget/autoload.js"; // 引入url;
      document.body.appendChild(live2d); // 将script引入<head>中;
    }
  },

  mounted() {
    this.live2dLoad();
    if (localStorage.getItem("imgNum") != null) {
      store.commit("setBackImg", localStorage.getItem("imgNum"));
    } else {
      store.commit("setBackImg", "2");
    }

    if (!Cookie.get("userName")) {
      var d = new Date();
      var userName = d.getHours() + "-" + d.getMinutes() + "-" + d.getSeconds();
      Cookie.set("userName", userName);
    }
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
  min-width: 650px;
  width: 100%;
  height: auto;
  padding: 0;
  position: fixed;

  z-index: 1;
}

#mainConent {
  width: 60%;
  min-width: 650px;
  min-height: 800px;
  background-color: aliceblue;
  opacity: 0.8;
  margin: auto;
  margin-top: 80px;
}
</style>
