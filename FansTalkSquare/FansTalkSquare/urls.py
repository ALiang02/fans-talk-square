"""FansTalkSquare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from datetime import time

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse, HttpResponse

from  dwebsocket.decorators import accept_websocket
from flask import json


@accept_websocket
def test(request):
    if request.is_websocket():
        print(request)
        try:
            while 1:
                message = request.websocket.wait()  # 接受前段发送来的数据
                print(message)
                if message:
                    message = bytes.decode(message)
                    print(message)
                    request.websocket.send(message.encode())  # 发送给前段的数据

        except Exception as e:
            try:
                request.websocket.close()
                return
            except:
                return

def demo(request):
    print(request)


    recive_data = json.loads(request.POST.get('data'))
    print(recive_data)
    print(type(recive_data))
    send_data = {
        "message" : "成功"
    }
    print(type(send_data))
    return JsonResponse(send_data);
    # return HttpResponse(json.dumps(send_data))

rooms = [];


def getRooms(request):
    #将数据库中的rooms返回给用户
    # recive_data = ""
    # send_data = {
    #     "rooms": [{"name": "房间名1"},{"name": "房间名2"},{"name": "房间名3"}]
    # }
    # return JsonResponse(send_data);
    send_data = {
        "rooms": rooms
    }

    return JsonResponse(send_data);

def addRoom(request):
    #将用户建立的房间添加到数据库中
    # recive_data = {"name": "房间名"}
    # send_data = ""
    # return JsonResponse(send_data);
    recive_data = json.loads(request.POST.get('data'))

    rooms.append(recive_data);

    send_data = {}
    return JsonResponse(send_data);



def removeRoom(request):
    # 在数据库中删除用户的房间
    # recive_data = {"name": "房间名"}
    # send_data = ""
    # return JsonResponse(send_data);

    recive_data = json.loads(request.POST.get('data'))
    room = recive_data

    # rooms = list(filter(lambda value: value['name']!=room['name'],rooms))
    rooms.remove(room)

    send_data = {}
    return JsonResponse(send_data)


webSocketRequests = []
@accept_websocket
def game(request):
    if request.is_websocket():
        print(request)
        try:
            while 1:
                message = request.websocket.wait()  # 接受前段发送来的数据
                print(message)
                if message:
                    print(message)
                    message = eval(bytes.decode(message))


                    if(message['act'] == "build"):
                        print("build")
                        webSocketRequests.append({
                            'name': message['game']['gamer1'],
                            'request':request.websocket
                        })
                    if(message['act'] == "join"):
                        print("join")
                        webSocketRequests.append({
                            'name': message['game']['gamer2'],
                            'request': request.websocket
                        })
                        send_message = {
                            'act': "join",
                            'gamer2': message['game']['gamer2']
                        }
                        print(message)
                        print(webSocketRequests)
                        # print(json.loads(message))

                        for webSocketRequest in webSocketRequests:
                            print(webSocketRequest)
                            print(webSocketRequest['name'])
                            print(message['game']['gamer1'])
                            if(webSocketRequest['name']==message['game']['gamer1']):
                                print('true')
                                webSocketRequest['request'].send(json.dumps(send_message).encode())
                    if (message['act'] == "quit"):
                        print("quit")

                        send_message = {
                            'act': "quit",
                        }
                        for webSocketRequest in webSocketRequests:
                            if (webSocketRequest['name'] == message['to']):
                                webSocketRequest['request'].send(json.dumps(send_message).encode())
                    if(message['act'] == "qizi"):
                        print("qizi")
                        send_message = {
                            'act': "qizi",
                            'qizi': message['qizi']
                        }

                        for webSocketRequest in webSocketRequests:
                            if(webSocketRequest['name']==message['to']):
                                webSocketRequest['request'].send(json.dumps(send_message).encode())

        except Exception as e:
            try:
                for webSocketRequest in webSocketRequests:
                    if (webSocketRequest['request'] == request.websocket):
                        webSocketRequests.remove(webSocketRequest)
                        for room in rooms:
                            if(room['name'] == webSocketRequest['name']):
                                rooms.remove(room)
                request.websocket.close()
                return
            except:
                return
    # 一名用户建立了一个房间等待其他玩家加入
    #第1个webSocket连接
    # recive_data = {
    #       'act': "build",
    #       'game': { 'gamer1': '1号玩家', 'gamer2': "?" }
    #  }

    # 一名用户建立了一个房间等待其他玩家加入
    # 第2个webSocket连接收到recive_data，触发第1个webSocket发送send_data
    # recive_data = {
    #     'act': "join",
    #     'game': {'gamer1': '1号玩家', 'gamer2': "2号玩家"}
    # }
    # send_data = {
    #     'act': "join",
    #     'gamer2': "2号玩家"
    # }

    #此时共建立了两个webSocket连接建立完成，开始下棋

    #1（2）号玩家下棋之后将这枚棋子的坐标发送给2（1）号玩家
    # 第1（2）个webSocket连接接收到recive_data，触发第2个webSocket连接发送send_data
    # recive_data = {'act': "qizi", 'qizi': {'x' : '坐标x', 'y' : '坐标y'}, 'from': "1(2)号玩家",'to': "2(1)号玩家"}
    # send_data = {'act': "qizi", 'qizi': {'x': '坐标x', 'y': '坐标y'}}

    #第1(2)个webSocket连接关闭时
    #触发第2(1)个webSocket连接发送send_data,若第2(1)个webSocket连接已经不存在，则不发送
    # send_data = {'act': 'quit'}
    #
    #
    # return



urlpatterns = [

    path('test', test),
    path('demo', demo),
    path('getRooms',getRooms),
    path('addRoom',addRoom),
    path('removeRoom',removeRoom),
    path('game',game),

]
