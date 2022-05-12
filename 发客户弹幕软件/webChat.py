# -*- coding: utf-8 -*-
# @Time    : 2022/2/18 
# @Author  :
import os
import time
import socket
import requests as requests

from messages import message_pb2
from messages.chat import ChatMessage

def downloadImg(url,path):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        open(path, 'wb').write(r.content) # 将内容写入图片
        print(f"CODE: {r.status_code} download {url} to {path}") # 返回状态码
        r.close()
        return path
    else:
        print(f"CODE: {r.status_code} download {url} Failed.")
        return "error"

def getScriptDir():
    return os.path.split(os.path.realpath(__file__))[0]

class Socket():
    def sendMsg(msg):
        Address = ('127.0.0.1', 25565) # Socket服务器地址,根据自己情况修改
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(Address)  # 尝试连接服务端
            s.sendall(msg.encode()) # 尝试向服务端发送消息
        except Exception:
            print(time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime()) + ' [ERROR] 无法连接到Socket服务器,请检查服务器是否启动')
        s.close()

class Watcher():
    def __init__(self):
        self.monitoringFile = f'{getScriptDir()}\\douyinLiveFile'

    def startWatcher(self):
        while True:
            files = os.listdir(self.monitoringFile)
            if files:
                for _ in files:
                    filepath = self.monitoringFile + '\\' + _

                    with open(filepath, 'rb') as f:
                        # print(f.read())
                        response = message_pb2.Response()
                        response.ParseFromString(f.read())

                    for message in response.messages:
                        if message.method == 'WebcastChatMessage':
                            chat_message = ChatMessage()
                            chat_message.set_payload(message.payload)

                            # userID
                            userID = chat_message.user().id
                            # 发言
                            content = chat_message.instance.content
                            # 头像
                            userHeaderImg = chat_message.user().avatarThumb.urlList[0]
                            print(userID, content, userHeaderImg)
                            filePath = downloadImg(userHeaderImg,f"{getScriptDir()}\\userImages\\{userID}.jpg")
                            Socket.sendMsg(f"{userID}\0{content}\0{filePath}")
                            # 用户uid\0用户发送的消息\0用户头像路径
                            # print(chat_message)
                    try:
                        os.remove(filepath)
                    except PermissionError as e:
                        time.sleep(1)
                        os.remove(filepath)

            time.sleep(2)

if __name__ == '__main__':
    if not os.path.isdir(getScriptDir()+"\\douyinLiveFile"):
        os.makedirs(getScriptDir()+"\\douyinLiveFile")
    if not os.path.isdir(getScriptDir()+"\\userImages"):
        os.makedirs(getScriptDir()+"\\userImages")
    Watcher().startWatcher()