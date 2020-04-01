<template>
  <div>
    <el-form :model="userForm" ref="userForm" label-width="80px" :inline="true">
      <el-form-item
        label="姓名"
        prop="name"
        :rules="[
      { required: true, message: '年龄不能为空'},
      {min: 1, max: 8, message: '最大为8个字符'}     
    ]"
      >
        <el-input type="age" v-model="userForm.name" autocomplete="off"></el-input>
      </el-form-item>
      <el-button @click="submitName">修改</el-button>
      <el-button @click="resetName">重置</el-button>
    </el-form>
  </div>
</template>

<script>
import Cookie from "js-cookie";
import store from "../store";

export default {
  data() {
    return {
      userForm: {
        name: store.state.username
      }
    };
  },
  methods: {
    submitName() {
      if (this.userForm.name === store.state.username) {
        this.$alert("姓名与之前一致", "修改失败", {
          confirmButtonText: "确定"
        });
        return;
      }
      this.$refs["userForm"].validate(valid => {
        if (valid) {
          Cookie.set("userName", this.userForm.name);
          store.state.username = this.userForm.name;
          this.$alert("姓名已修改", "修改成功", {
            confirmButtonText: "确定"
          });
        } else {
          this.$alert("姓名不符合规范", "修改失败", {
            confirmButtonText: "确定"
          });
        }
      });
    },

    resetName() {
      this.$refs["userForm"].resetFields();
    }
  }
};
</script>