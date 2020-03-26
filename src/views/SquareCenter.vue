<template>
  <div>
    <el-row>
      <el-col :span="12" :offset="4">
        <SquareArticle></SquareArticle>
      </el-col>
    </el-row>
    <div>
      <button @click="sendWebSocket">webSocket发消息</button>
      <button @click="sendAxios">axios发消息</button>
    </div>
  </div>
</template>

<script>
import SquareArticle from "./../components/SquareArticle";
import { init } from "@/utils/webSocket.js";
import service from "@/utils/request.js";

export default {
  data() {
    return {
      socket1: ""
    };
  },
  components: {
    SquareArticle
  },

  methods: {
    sendWebSocket() {
      var message = { name: "测试", age: "18" };
      this.socket1.send(JSON.stringify(message));
    },

    sendAxios() {
      service({
        url: "demo",
        data: {
          name: "测试",
          age: 18,
          schoole: { grade: 2, term: 2 },
          arr: [1, 2, 3]
        }
      }).then(res => {
        console.log(res);
      });
    }
  },

  mounted() {
    // 初始化
    this.socket1 = init("test");
    this.socket1.onmessage = res => {
      console.log(res);
    };
  }
};
</script>
