<template>
  <div id="personalCenter">
    <div id="container" @click="getXY">
      <canvas id="qipan" width="561px" height="561px">
        <!-- 切勿通过style或script标签修改canvas的width和height属性 -->
      </canvas>
    </div>
  </div>
</template>

<script>
import request from "@/utils/request";
import Cookie from "js-cookie";

export default {
  data() {
    return {
      qizis: [],
      qizipre: {
        x: -1,
        y: -1
      }
    };
  },

  methods: {
    qipanInit() {
      var qipan = document.getElementById("qipan");

      var cxt = qipan.getContext("2d");
      cxt.fillStyle = "#E6A23C";
      cxt.fillRect(0, 0, 561, 561);
      for (let i = 0; i < 15; i++) {
        cxt.moveTo(i * 40 + 0.5, 0);
        cxt.lineTo(i * 40 + 0.5, 561);
        cxt.moveTo(0, i * 40 + 0.5);
        cxt.lineTo(561, i * 40 + 0.5);
        // 1px问题，canvas的线条画法不一样，canvas的每条线都有一条无限细的“中线”，线条的宽度是从中线向两侧延伸的。
      }
      cxt.stroke();

      cxt.fillStyle = "#000000";
      cxt.beginPath();
      cxt.arc(120 + 0.5, 120 + 0.5, 4, 0, Math.PI * 2);

      cxt.closePath();
      cxt.fill();

      cxt.beginPath();
      cxt.arc(440 + 0.5, 120 + 0.5, 4, 0, Math.PI * 2);
      cxt.closePath();
      cxt.fill();

      cxt.beginPath();
      cxt.arc(120 + 0.5, 440 + 0.5, 4, 0, Math.PI * 2);
      cxt.closePath();
      cxt.fill();

      cxt.beginPath();
      cxt.arc(440 + 0.5, 440 + 0.5, 4, 0, Math.PI * 2);
      cxt.closePath();
      cxt.fill();

      this.qiziPreInit(this.qizipre.x, this.qizipre.y);

      for (let i = 0; i < this.qizis.length; i++) {
        this.qiziInit(this.qizis[i].x, this.qizis[i].y, i);
      }
    },

    qiziInit(x, y, n) {
      x *= 40;
      y *= 40;
      var qipan = document.getElementById("qipan");
      var cxt = qipan.getContext("2d");

      if (n % 2 === 0) {
        cxt.fillStyle = "#000000";
      } else {
        cxt.fillStyle = "#ffffff";
      }

      cxt.beginPath();
      cxt.arc(x + 0.5, y + 0.5, 18, 0, Math.PI * 2);
      cxt.closePath();
      cxt.fill();
    },

    qiziPreInit(x, y) {
      if (x === -1 || y === -1) {
        return;
      }
      x *= 40;
      y *= 40;
      var qipan = document.getElementById("qipan");
      var cxt = qipan.getContext("2d");
      cxt.moveTo(x + 16 + 0.5, y + 2 + 0.5);
      cxt.lineTo(x + 2 + 0.5, y + 2 + 0.5);
      cxt.lineTo(x + 2 + 0.5, y + 16 + 0.5);

      cxt.moveTo(x - 16 + 0.5, y + 2 + 0.5);
      cxt.lineTo(x - 2 + 0.5, y + 2 + 0.5);
      cxt.lineTo(x - 2 + 0.5, y + 16 + 0.5);

      cxt.moveTo(x + 16 + 0.5, y - 2 + 0.5);
      cxt.lineTo(x + 2 + 0.5, y - 2 + 0.5);
      cxt.lineTo(x + 2 + 0.5, y - 16 + 0.5);

      cxt.moveTo(x - 16 + 0.5, y - 2 + 0.5);
      cxt.lineTo(x - 2 + 0.5, y - 2 + 0.5);
      cxt.lineTo(x - 2 + 0.5, y - 16 + 0.5);
      cxt.stroke();
    },

    getXY(e) {
      var x = e.offsetX;
      var y = e.offsetY;

      if (
        ((x % 40 >= 0 && x % 40 <= 10) || (x % 40 >= 30 && x % 40 < 40)) &&
        ((y % 40 >= 0 && y % 40 <= 10) || (y % 40 >= 30 && y % 40 < 40))
      ) {
        x = parseInt((x + 20) / 40);
        console.log(x);
        y = parseInt((y + 20) / 40);
        if (x === this.qizipre.x && y === this.qizipre.y) {
          this.qizis.push({
            x,
            y
          });
          this.qipanInit();
        } else {
          this.qizipre = { x, y };
          this.qipanInit();
        }
      }
    }
  },

  mounted() {
    Cookie.set("name", "cookie测试");
    this.qipanInit();
    this.qiziInit(280, 280, 0);
    this.qiziInit(320, 320, 1);
    this.qiziPreInit(280, 320);
    this.qiziInit(280, 320, 0);
    request({
      url: "test",
      method: "get"
    }).then(res => {
      console.log(res.data);
    });
  }
};
</script>
<style>
#container {
  width: 561px;
  height: 561px;
  margin: auto;
}
</style>
