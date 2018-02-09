#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: 陈二狗


import xlrd

def _int(data):
    """ srt --> int """
    if data == '':
        return 0
    return int(data)


def _float(data):
    """str -> int"""
    if data == '':
        return 0.0
    else:
        return float(data)


def _utf8(data):
    """unicode -> str encoding utf-8"""
    return data.encode('utf-8').strip()



class server_info(object):

    def __init__(self):
        self.gameserver = {}

    def load(self):
        excel_file = 'model/serverinfo_ce.xlsx'
        self.loadCEgameServerInfo(excel_file,"gameserver")
        # self.loadServerInfo(excel_file,"server")

    def loadCEgameServerInfo(self, excel_file, sheet_name):
        book = xlrd.open_workbook(excel_file)
        self.game_server_info = {}
        sheet = book.sheet_by_name(sheet_name)
        #print sheet.name

        for i in xrange(1, sheet.nrows):
            game_server_id = _int(sheet.cell_value(i,0))
            self.game_server_info[game_server_id] = {}
            self.game_server_info[game_server_id]['serverID'] = _int(sheet.cell_value(i, 0))
            self.game_server_info[game_server_id]['servername'] = _utf8(sheet.cell_value(i, 1))
            self.game_server_info[game_server_id]['IP'] = _utf8(sheet.cell_value(i, 2))
            self.game_server_info[game_server_id]['port'] = _int(sheet.cell_value(i, 3))
            self.game_server_info[game_server_id]['gamepath'] = _utf8(sheet.cell_value(i, 4))
            self.game_server_info[game_server_id]['bakpath'] = _utf8(sheet.cell_value(i, 5))
            self.game_server_info[game_server_id]['Domain'] = _utf8(sheet.cell_value(i, 6))
            self.game_server_info[game_server_id]['gameport'] = _int(sheet.cell_value(i, 7))
            self.game_server_info[game_server_id]['mysqldata'] = _utf8(sheet.cell_value(i, 8))
            self.game_server_info[game_server_id]['mysqluser'] = _utf8(sheet.cell_value(i, 9))
            self.game_server_info[game_server_id]['mysqlpasswd'] = _utf8(sheet.cell_value(i, 10))
            self.game_server_info[game_server_id]['NATport'] = _int(sheet.cell_value(i, 11))

    def getCEgameServerInfo(self):
        return self.game_server_info

    def getGameServerInfoByID(self,game_server_id):
        # print "debug====",self.game_server_info
        return self.game_server_info[game_server_id]

    def getServerIP(self):
        allServerIP = []
        allServerport = []
        dicall = {}
        server_list = []
        for i in self.game_server_info.keys():
            ServerIP = self.game_server_info[i]['IP']
            Serverport = self.game_server_info[i]['port']
            allServerIP.append(ServerIP)
            allServerport.append(Serverport)
            dic = {i: {"IP":ServerIP, "port":Serverport}}
            dicall.update(dic)
        for s in dicall.values():
            if s not in server_list:
                server_list.append(s)
        return server_list





