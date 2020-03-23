<template>
  <div id="personalCenter">
    <div id="container" @click="getXY">
      <canvas id="qipan" width="561px" height="561px">
        <!-- 切勿通过style或script标签修改canvas的width和height属性 -->
      </canvas>
    </div>
    <button type="button" name="myBtn" @click="restart">按钮</button>
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
      cxt.lineWidth = 1;
      cxt.strokeStyle = "black";

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
      //x,y是棋子坐标,n是棋子次序,画上棋子
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
      //x,y是坐标,画上预选位置
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
      //获取x,y坐标
      var x = e.offsetX;
      var y = e.offsetY;

      if (
        ((x % 40 >= 0 && x % 40 <= 10) || (x % 40 >= 30 && x % 40 < 40)) &&
        ((y % 40 >= 0 && y % 40 <= 10) || (y % 40 >= 30 && y % 40 < 40))
      ) {
        x = parseInt((x + 20) / 40);
        y = parseInt((y + 20) / 40);
        if (x === this.qizipre.x && y === this.qizipre.y) {
          this.qizis.push({
            x,
            y
          });
          this.qizipre.x = -1;
          this.qizipre.y = -1;
          this.qipanInit();
          this.victory();
        } else {
          this.qizipre = { x, y };
          this.qipanInit();
        }
      }
    },

    victory() {
      var line = [];
      if (this.check(0, 1, line)) {
        console.log("胜利");

        return;
      }
      if (this.check(1, 0, line)) {
        console.log("胜利");

        return;
      }
      if (this.check(1, 1, line)) {
        console.log("胜利");

        return;
      }
      if (this.check(1, -1, line)) {
        console.log("胜利");

        return;
      }
    },

    check(east, north, line) {
      line = [];
      var n = this.qizis.length - 1;
      var x = this.qizis[n].x;
      var y = this.qizis[n].y;

      for (let i = -4; i <= 4; i++) {
        for (let j = n % 2; j <= n; j += 2) {
          if (
            this.qizis[j].x === x + east * i &&
            this.qizis[j].y === y + north * i
          ) {
            line.push(this.qizis[j]);
            if (line.length === 5) {
              this.drawVctLine(line, n);
              return true;
            }
            break;
          } else if (j === n || j === n - 1) {
            line = [];
          }
        }
      }
    },

    drawVctLine(line, n) {
      var qipan = document.getElementById("qipan");
      var cxt = qipan.getContext("2d");
      cxt.lineWidth = 10;
      cxt.moveTo(line[0].x * 40 + 0.5, line[0].y * 40 + 0.5);
      cxt.lineTo(line[1].x * 40 + 0.5, line[1].y * 40 + 0.5);
      cxt.lineTo(line[2].x * 40 + 0.5, line[2].y * 40 + 0.5);
      cxt.lineTo(line[3].x * 40 + 0.5, line[3].y * 40 + 0.5);
      cxt.lineTo(line[4].x * 40 + 0.5, line[4].y * 40 + 0.5);
      if (n % 2 === 0) {
        cxt.strokeStyle = "black";
      } else {
        cxt.strokeStyle = "white";
      }
      cxt.stroke();
    },

    restart() {
      this.qizis = [];
      this.qizipre = {
        x: -1,
        y: -1
      };
      this.qipanInit();
      this.qipanInit();
    }
  },

  mounted() {
    Cookie.set("name", "cookie测试");
    this.qipanInit();
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
