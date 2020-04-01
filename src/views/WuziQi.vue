<template>
  <div id="personalCenter">
    <div id="container" @click="getXY">
      <canvas id="qipan" width="601px" height="601px">
        <!-- 切勿通过style或script标签修改canvas的width和height属性 -->
      </canvas>
    </div>
    <div class="gamerMsg">
      <div class="gamer">{{gamer1}}</div>
      <div class="gamer">vs</div>
      <div class="gamer">{{gamer2}}</div>
    </div>

    <div id="start" align="center">
      <el-button type="primary" @click="build">创建对局</el-button>
      <el-button type="primary" @click="join">加入对局</el-button>
      <el-button type="primary" @click="refresh">刷新对局</el-button>
      <el-button type="primary" @click="start">开始</el-button>
      <el-button type="primary" @click="quit">退出</el-button>
    </div>

    <div align="center">
      <div v-for="room in rooms" :key="room.name">
        <input type="radio" name="room" :value="room.name" class="room" @click="roomChoose" />
        {{room.name+"的房间"}}
      </div>
    </div>
  </div>
</template>

<script>
import Cookie from "js-cookie";
import service from "@/utils/request.js";
import { init } from "@/utils/webSocket.js";

export default {
  data() {
    return {
      qizis: [],
      qizipre: {
        x: -1,
        y: -1
      },
      gameIsStarted: false,
      turn: false,
      username: Cookie.get("userName"),
      gamer1: "?",
      gamer2: "?",
      count: 5,
      room: "",
      rooms: [
        {
          name: "五子棋无敌"
        },
        {
          name: "天下无敌"
        },
        {
          name: "大脑天宫"
        }
      ],
      socket: ""
    };
  },

  methods: {
    getRooms() {
      service({
        url: "getRooms",
        data: {}
      }).then(res => {
        this.rooms = res.data.rooms;
        for (var room of res.data.rooms) {
          if (room.name === this.username) {
            this.gamer1 = this.username;
          }
        }
      });
    },

    addRoom() {
      service({
        url: "addRoom",
        data: {
          name: this.username
        }
      });
    },

    removeRoom() {
      service({
        url: "removeRoom",
        data: {
          name: this.username
        }
      });
    },

    roomChoose(e) {
      this.room = e.srcElement.value;

      // e.srcElement.e.srcElement.style.background = "#E6A23C";
    },

    quit() {
      // this.socket.close();
      this.socket = "";
      if (this.gamer1 === this.username) {
        this.removeRoom();
      }
      this.gamer1 = "?";
      this.gamer2 = "?";
      this.getRooms();
    },

    refresh() {
      this.getRooms();
    },

    sendWebSocket(message) {
      console.log("sendWebSocket:");
      console.log(message);
      if (message.act === "qizi") {
        this.turn = false;
      }
      console.log(this.socket.readyState);
      if (this.socket.readyState === 1) {
        this.socket.send(JSON.stringify(message));
      }
    },

    reciveWebSocket(message) {
      var data = JSON.parse(message.data);
      console.log(data);
      console.log("reciveWebSocket" + data);
      //todo
      if (data.act === "qizi") {
        this.gameIsStarted = true;
        this.turn = true;
        this.qizis.push(data.qizi);

        this.qizipre.x = -1;
        this.qizipre.y = -1;
        this.qipanInit();
        this.victory();
      }
      if (data.act === "join") {
        this.gamer2 = data.gamer2;
      }
      if (data.act === "quit") {
        if (this.gamer1 === this.username) {
          this.gamer2 = "?";
          this.gameIsStarted = false;
        } else {
          this.gamer1 = "?";
          this.gameIsStarted = false;
        }
      }
    },

    build() {
      if (this.gamer1 === "?" && this.gamer2 === "?") {
        // this.rooms.push({
        //   name: this.username
        // });
        this.addRoom();
        this.getRooms();
        this.gamer1 = this.username;
        this.socket = init("game");
        this.socket.onmessage = this.reciveWebSocket;

        let _this = this;
        setTimeout(function() {
          _this.sendWebSocket({
            act: "build",
            game: { gamer1: _this.gamer1, gamer2: "?" }
          });
        }, 1000);
      } else {
        alert("请先退出对局");
      }
    },

    join() {
      if (this.gamer1 !== "?" || this.gamer2 !== "?") {
        alert("请先退出对局");
        return;
      }
      if (this.room === "") {
        alert("请先选择对战对局");
        return;
      }
      this.gamer1 = this.room;
      this.gamer2 = this.username;
      this.socket = init("game");
      this.socket.onmessage = this.reciveWebSocket;
      let _this = this;
      setTimeout(function() {
        _this.sendWebSocket({
          act: "join",
          game: { gamer1: _this.gamer1, gamer2: _this.gamer2 }
        });
      }, 1000);
    },

    start() {
      if (this.gamer1 === this.username && this.gamer2 !== "?") {
        alert("游戏开始");
        this.gameIsStarted = true;
        this.turn = true;
        this.qizis = [];
        this.qizipre = {
          x: -1,
          y: -1
        };
        this.qipanInit();
        this.qipanInit();
      } else if (this.gamer1 !== "?" && this.gamer2 === this.username) {
        alert("请呼叫房主开始游戏");
      } else {
        alert("还不能开始哟");
      }
    },

    qipanInit() {
      var qipan = document.getElementById("qipan");

      var cxt = qipan.getContext("2d");
      cxt.lineWidth = 1;
      cxt.strokeStyle = "black";

      cxt.fillStyle = "#E6A23C";
      cxt.fillRect(0, 0, 601, 601);
      for (let i = 0; i < 15; i++) {
        cxt.moveTo(i * 40 + 0.5 + 20, 0 + 20);
        cxt.lineTo(i * 40 + 0.5 + 20, 561 + 20);
        cxt.moveTo(0 + 20, i * 40 + 0.5 + 20);
        cxt.lineTo(561 + 20, i * 40 + 0.5 + 20);
        // 1px问题，canvas的线条画法不一样，canvas的每条线都有一条无限细的“中线”，线条的宽度是从中线向两侧延伸的。
      }
      cxt.stroke();

      cxt.fillStyle = "#000000";
      cxt.beginPath();
      cxt.arc(120 + 0.5 + 20, 120 + 0.5 + 20, 4, 0, Math.PI * 2);

      cxt.closePath();
      cxt.fill();

      cxt.beginPath();
      cxt.arc(440 + 0.5 + 20, 120 + 0.5 + 20, 4, 0, Math.PI * 2);
      cxt.closePath();
      cxt.fill();

      cxt.beginPath();
      cxt.arc(120 + 0.5 + 20, 440 + 0.5 + 20, 4, 0, Math.PI * 2);
      cxt.closePath();
      cxt.fill();

      cxt.beginPath();
      cxt.arc(440 + 0.5 + 20, 440 + 0.5 + 20, 4, 0, Math.PI * 2);
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
      cxt.arc(x + 0.5 + 20, y + 0.5 + 20, 18, 0, Math.PI * 2);
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
      cxt.moveTo(x + 16 + 0.5 + 20, y + 2 + 0.5 + 20);
      cxt.lineTo(x + 2 + 0.5 + 20, y + 2 + 0.5 + 20);
      cxt.lineTo(x + 2 + 0.5 + 20, y + 16 + 0.5 + 20);

      cxt.moveTo(x - 16 + 0.5 + 20, y + 2 + 0.5 + 20);
      cxt.lineTo(x - 2 + 0.5 + 20, y + 2 + 0.5 + 20);
      cxt.lineTo(x - 2 + 0.5 + 20, y + 16 + 0.5 + 20);

      cxt.moveTo(x + 16 + 0.5 + 20, y - 2 + 0.5 + 20);
      cxt.lineTo(x + 2 + 0.5 + 20, y - 2 + 0.5 + 20);
      cxt.lineTo(x + 2 + 0.5 + 20, y - 16 + 0.5 + 20);

      cxt.moveTo(x - 16 + 0.5 + 20, y - 2 + 0.5 + 20);
      cxt.lineTo(x - 2 + 0.5 + 20, y - 2 + 0.5 + 20);
      cxt.lineTo(x - 2 + 0.5 + 20, y - 16 + 0.5 + 20);
      cxt.stroke();
    },

    getXY(e) {
      if (this.gameIsStarted === false) {
        return;
      }
      if (this.turn === false) {
        return;
      }
      //获取x,y坐标
      var x = e.offsetX - 20;
      var y = e.offsetY - 20;

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
          var n = this.qizis.length - 1;
          var to;
          if (n % 2 === 0) {
            to = this.gamer2;
          } else {
            to = this.gamer1;
          }
          this.sendWebSocket({
            act: "qizi",
            qizi: { x: x, y: y },
            to
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
        return;
      }
      if (this.check(1, 0, line)) {
        return;
      }
      if (this.check(1, 1, line)) {
        return;
      }
      if (this.check(1, -1, line)) {
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
              console.log("胜利");
              if (n % 2 === 0) {
                console.log(this.gamer1 + "胜利");
              } else {
                console.log(this.gamer2 + "胜利");
              }
              this.gameIsStarted = false;
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
      cxt.moveTo(line[0].x * 40 + 0.5 + 20, line[0].y * 40 + 0.5 + 20);
      cxt.lineTo(line[1].x * 40 + 0.5 + 20, line[1].y * 40 + 0.5 + 20);
      cxt.lineTo(line[2].x * 40 + 0.5 + 20, line[2].y * 40 + 0.5 + 20);
      cxt.lineTo(line[3].x * 40 + 0.5 + 20, line[3].y * 40 + 0.5 + 20);
      cxt.lineTo(line[4].x * 40 + 0.5 + 20, line[4].y * 40 + 0.5 + 20);
      if (n % 2 === 0) {
        cxt.strokeStyle = "black";
      } else {
        cxt.strokeStyle = "white";
      }
      cxt.stroke();
    }

    // start() {
    //   this.gameIsStarted = true;
    //   this.qizis = [];
    //   this.qizipre = {
    //     x: -1,
    //     y: -1
    //   };
    //   this.qipanInit();
    //   this.qipanInit();
    // }
  },

  mounted() {
    this.qipanInit();
    this.getRooms();
  }
};
</script>
<style>
#container {
  width: 601px;
  height: 601px;
  margin: auto;
}

.gamerMsg {
  width: 601px;
  margin: auto;
  margin-top: 10px;
  margin-bottom: 10px;
}

.gamer {
  width: 200px;
  height: 100%;

  text-align: center;
  /* float: left; */
  display: inline-block;
}

.gameroom {
  list-style-type: none;
  text-align: center;
}
</style>
