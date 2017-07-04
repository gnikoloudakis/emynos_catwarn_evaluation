import time
import random

import datetime

from CatMessage import *
import requests
import eRequest


class eFunctions:
    def __init__(self):
        self.erequests = []
        self.responceTime = ""
        self.throughPut = ""
        self.latency = ""
        self.severity = ['Extreme', 'Severe', 'Moderate', 'Minor', 'Unknown']

    def sendMessages(self, repeat, ip, port, id):
        if ip == '127.0.0.1':
            r = self.postMessages(repeat, ip, port, "/api/cap", id)
            r1 = requests.get("http://" + ip + ":" + port + "/api/export")
            # self.wtiteToFile(False)
            return r
        else:
            r = self.postMessages(repeat, ip, port, "/api/cap", id)
            r1 = requests.get("http://" + ip + ":" + port + "/api/export/response")
            r2 = requests.get("http://" + ip + ":" + port + "/api/export/latency")
            r3 = requests.get("http://" + ip + ":" + port + "/api/export/throughput")

            self.responceTime = r1.content
            self.latency = r2.content
            self.throughPut = r3.content
            self.wtiteToFile(True)
            return r

    def wtiteToFile(self, selector):
        global fo
        content = ""
        # try:
        #     fo = open("Latency.txt", "a")
        #     for mess in self.erequests:
        #         content += "  " + str(mess.end - mess.start) + "\n"
        #
        #     fo.write(datetime.datetime.fromtimestamp(self.erequests[0].getStart()).strftime('%Y-%m-%d %H:%M:%S') + "\n")
        #     fo.write(content)
        #     fo.write(datetime.datetime.fromtimestamp(self.erequests[len(self.erequests) - 1].getEnd()).strftime('%Y-%m-%d %H:%M:%S') + "\n")
        # except IOError:
        #     print "shit happened/Latency"
        # finally:
        #     fo.close()
        ###############################################################################################################
        if selector:
            try:
                fo = open("ResponseTime.txt", "a")
                fo.write(self.responceTime)
            except IOError:
                print "shit happened/ResponseTime"
            finally:
                fo.close()
            ###############################################################################################################
            try:
                fo = open("ThroughPut.txt", "a")
                fo.write(self.throughPut)
            except IOError:
                print "shit happened/ThroughPut"
            finally:
                fo.close()
            ###############################################################################################################
            try:
                fo = open("Latency.txt", "a")
                fo.write(self.latency)
            except IOError:
                print "shit happened/Latency.txt"
            finally:
                fo.close()

    def postMessages(self, repeat, ip, port, elemenet, id):
        for i in range(repeat):
            m = Message(str(i) + id, severity=self.severity[random.randint(0, 4)]).message
            messageRequest = eRequest.request(time.time(), None)
            try:
                r = requests.post("http://" + ip + ":" + port + elemenet, data=m, headers={'Content-Type': 'text/plain'})
            except Exception:
                print Exception.message

            messageRequest.setEnd(time.time())
            self.erequests.append(messageRequest)
        return r.content
