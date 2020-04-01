export function init(url){
    var socket = new WebSocket("ws://118.178.94.45:8081/" + url);
    socket.onopen = () => {
        console.log(url+"连接成功")
    }
    socket.onerror = () => {
        console.log(url+"连接错误")
    }
    socket.onclose = () =>{
        console.log(url+"连接关闭")
    }
    socket.onmessage = ()=>{
        console.log(url+"接收数据成功")
    }
    
    return socket;
}