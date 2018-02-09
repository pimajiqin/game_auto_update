#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗



from model.scp_ssh import *
from model.serverinfo import *
import threading
import time

server_info = server_info()
server_info.load()
serverlist = server_info.getServerIP()

def run(i,command):
    time.sleep(1)
    U = SCP_SSH(i['IP'], 'ft', i['port'], '/home/ft/.ssh/id_rsa')
    print U.ssh(command)

def runall(command):
    for i in serverlist:
        t = threading.Thread(target=run,args=(i,command))
        t.start()
    t.join()

def scpone(i,localpath,remotepath ):
    U = SCP_SSH(i['IP'], 'ft', i['port'], '/home/ft/.ssh/id_rsa')
    U.scp(localpath, remotepath)

def scpall(localpath,remotepath):
    for i in serverlist:
        scpone(i, localpath, remotepath)

if __name__ == '__main__':
    starttime = time.time()

    print "====== 清空 ======"
    runall('rm -rf /tmp/temp/*')
    time.sleep(3)
    print "====== 检查 ======"
    runall('hostname&&ls /tmp/temp/')
    time.sleep(3)
    print "====== 上传 ======"
    scpall('/opt/scripts/ce/newpack/newpack.tar.gz', '/tmp/temp/newpack.tar.gz')
    time.sleep(1)
    print "====== 解压 ======"
    runall('hostname&&cd /tmp/temp&&tar zxf newpack.tar.gz')
    time.sleep(3)
    print "====== 检查 ======"
    runall('hostname&&ls /tmp/temp/')
    time.sleep(1)

    endtime = time.time()
    print(endtime - starttime)
