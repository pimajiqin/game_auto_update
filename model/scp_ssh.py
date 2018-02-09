#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗


import paramiko



class SCP_SSH(object):

    def __init__(self,ip,user,port,pkey):
        self.ip = ip
        self.user = user
        self.port = port
        self.pkey = pkey

    def ssh(self,command):
        private_key = paramiko.RSAKey.from_private_key_file(self.pkey)
        transport = paramiko.Transport((self.ip, self.port))
        transport.connect(username=self.user, pkey=private_key)
        ssh = paramiko.SSHClient()
        ssh._transport = transport
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read()
        transport.close()
        return result

    def scp(self,localpath,remotepath):
        private_key = paramiko.RSAKey.from_private_key_file(self.pkey)
        trans = paramiko.Transport((self.ip, self.port))
        trans.connect(username=self.user, pkey=private_key)
        sftp = paramiko.SFTPClient.from_transport(trans)
        sftp.put(localpath=localpath, remotepath=remotepath)
        trans.close()



