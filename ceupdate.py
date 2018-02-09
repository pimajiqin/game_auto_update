#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: 陈二狗


from model.scp_ssh import *
from model.serverinfo import *
import threading
import time

server_info = server_info()
server_info.load()
serverlist = server_info.getCEgameServerInfo()



def run(i,command1,command2):
    time.sleep(1)
    U = SCP_SSH(i['IP'], 'ft', i['port'], '/home/ft/.ssh/id_rsa')
    print U.ssh("%s%s%s" % (command1,i['gamepath'],command2))

def runall(command1,command2):
    for i in range(1,len(serverlist)+1):
        t = threading.Thread(target=run,args=(serverlist[i],command1,command2))
        t.start()
    t.join()


if __name__ == '__main__':
    starttime = time.time()

    print "====== test ======"
    runall('hostname&&cat ','/logic/cfg/serverID.xml' )
    time.sleep(3)

    endtime = time.time()
    print(endtime - starttime)