<template>
  <div>
    <span>选择壁纸：</span>
    <el-select v-model="value">
      <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option>
    </el-select>
  </div>
</template>

<script>
import store from "../store";

export default {
  data() {
    return {
      options: [
        {
          value: "1",
          label: "1"
        },
        {
          value: "2",
          label: "2"
        },
        {
          value: "3",
          label: "3"
        },
        {
          value: "4",
          label: "4"
        },
        {
          value: "5",
          label: "5"
        },
        {
          value: "6",
          label: "6"
        }
      ],
      value: store.state.imgNum
    };
  },

  watch: {
    value: function() {
      store.commit("setBackImg", this.value);
    }
  }
};
</script>
