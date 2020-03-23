<template>
  <div>个人</div>
</template>

<script>
import request from "@/utils/request";

export default {
  mounted() {
    request({
      url: "test",
      method: "get"
    }).then(res => {
      console.log(res.data.message);
    });
  }
};
</script>
<style>
#mainmainConent {
  width: 60%;
  min-width: 500px;
  background-color: aliceblue;
  opacity: 0.5;
  margin: auto;
}
</style>
