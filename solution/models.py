from django.db import models
import random
from django import template


# Create your models here.

import http.client
import base64
import ssl
import sys
import json
import urllib.request
import ast

class ServerData(models.Model):
    name = models.CharField(max_length=128)
    ip = models.CharField(max_length=128)
    adminID = models.CharField(max_length=128)
    adminPW = models.CharField(max_length=128)
    
    def getName(self):
      return self.name
      
    def getIP(self):
      return self.ip
      
    def getID(self):
      return self.adminID
      
    def getPW(self):
      return self.adminPW

class getAllUser:
    # host and authentication credentials
    host = "" # "10.20.30.40"
    admin = "" # "ersad"
    password = "" # "Password1"
    user_id = ""  # "d83da9b6-6fd0-4704-bc37-69ceaaa5f633"
    users = []
    userDetails = []
    
    createResult = ""
    changeResult = ""
    
   
    
    
    def __init__(self, serverInfo):
        print("===============================solution init=========================================")
        self.host = serverInfo.ip # "10.20.30.40"
        self.admin = serverInfo.adminID # "ersad"
        self.password = serverInfo.adminPW # "Password1"
      
        conn = http.client.HTTPSConnection("{}:9060".format(self.host), context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))

        creds = str.encode(':'.join((self.admin, self.password)))
        encodedAuth = bytes.decode(base64.b64encode(creds))

        headers = {
            'accept': "application/json",
            'authorization': " ".join(("Basic",encodedAuth)),
            'cache-control': "no-cache",
            }

        conn.request("GET", "/ers/config/internaluser/", headers=headers)

        res = conn.getresponse()
        data = res.read()

        print("==================================ALL USER================================================")
        print("Status: {}".format(res.status))
        print("Header:\n{}".format(res.headers))
        print("Body:\n{}".format(data.decode("utf-8")))
        
        dict=json.loads(data.decode('utf-8'))
        self.users = dict['SearchResult']['resources']
        
       

        
    def getUserDetail(self):
       self.userDetails = []
       for i in range(len(self.users)):
          self.userDetails.append(self.userDetail(i))
          self.userDetails[i] = ast.literal_eval(self.userDetails[i])
       print("-====================")
       print(self.userDetails)
       print("****************"+str(self.users))
        
    def userDetail(self, idx):
        self.user_id = str(self.users[idx]['id'])

        # host and authentication credentials
        

        conn = http.client.HTTPSConnection("{}:9060".format(self.host), context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))

        creds = str.encode(':'.join((self.admin, self.password)))
        encodedAuth = bytes.decode(base64.b64encode(creds))

        headers = {
            'accept': "application/json",
            'authorization': " ".join(("Basic",encodedAuth)),
            'cache-control': "no-cache",
            }

        conn.request("GET", "/ers/config/internaluser/{}".format(self.user_id), headers=headers)

        res = conn.getresponse()
        data = res.read()
        
        print("==================================USER Detail================================================")
        print("Status: {}".format(res.status))
        print("Header:\n{}".format(res.headers))
        print("Body:\n{}".format(data.decode("utf-8")))
        
        dict=json.loads(data.decode('utf-8'))
        
        print("test : "+str(dict['InternalUser']['id']))
        
        return str(dict['InternalUser'])



    def createUser(self, userInfo):
        #parameters
        name = userInfo['userID']  # "chris"
        first = userInfo['userName']  # "Chris
        last = "."  # "Colombus"
        passwd = userInfo['userPW']  # "Password1"
        email = userInfo['userID'] + "@airquay.com"  # "chris@cisco.com"
        expiry_date = "2020-01-29"  # "2017-01-29"



        conn = http.client.HTTPSConnection("{}:9060".format(self.host), context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))

        creds = str.encode(':'.join((self.admin, self.password)))
        encodedAuth = bytes.decode(base64.b64encode(creds))

        req_body_json = """  {{
            "InternalUser" : {{
                "name" : "{}",
                "enabled" : true,
                "email" : "{}",
                "password" : "{}",
                "firstName" : "{}",
                "lastName" : "{}",
                "changePassword" : true,
                "expiryDateEnabled" : true,
                "expiryDate" : "{}",
                "enablePassword" : "{}",
                "customAttributes" : {{
                }},
                "passwordIDStore" : "Internal Users"
            }}
        }}
        """.format(name,email,passwd,first,last,expiry_date,passwd)

        headers = {
            'accept': "application/json",
            'content-type': "application/json",
            'authorization': " ".join(("Basic",encodedAuth)),
            'cache-control': "no-cache",
            }

        conn.request("POST", "/ers/config/internaluser/", headers=headers, body=req_body_json)

        res = conn.getresponse()
        data = res.read()
        
        print("==================================Create USER================================================")
        print("Status: {}".format(res.status))
        print("Header:\n{}".format(res.headers))
        print("Body:\n{}".format(data.decode("utf-8")))
          
        if str(res.status) == "201":
          self.createResult = "Success"     
        else:
          dict=json.loads(data.decode('utf-8'))
          self.createResult = str(dict['ERSResponse']['messages'][0]['title'])
          
        print(self.createResult)
    
    
    def findUserIDByName(self, name):
      for i in self.users:
        if i['name'] == name:
          return i['id']
    
    def changePW(self,userInfo):
        #parameters
        user_id = self.findUserIDByName(userInfo['cuserID']) # "f330048f-cfb0-45db-8ef0-39efc650b711"
        name = userInfo['cuserID']
        new_passwd = userInfo['nuserPW'] # "Password6"

        # host and authentication credentials
        


        conn = http.client.HTTPSConnection("{}:9060".format(self.host), context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))

        creds = str.encode(':'.join((self.admin, self.password)))
        encodedAuth = bytes.decode(base64.b64encode(creds))

        req_body_json = """  {{
            "InternalUser" : {{
                "id" : "{}",
                "name" : "{}",
                "password" : "{}",
                "customAttributes" : {{
                }}
            }}
        }}
        """.format(user_id,name,new_passwd)

        headers = {
            'accept': "application/json",
            'content-type': "application/json",
            'authorization': " ".join(("Basic",encodedAuth)),
            'cache-control': "no-cache",
            }

        conn.request("PUT", "/ers/config/internaluser/{}".format(user_id), headers=headers, body=req_body_json)

        res = conn.getresponse()
        data = res.read()

        print("==================================Change Password================================================")
        print("Status: {}".format(res.status))
        print("Header:\n{}".format(res.headers))
        print("Body:\n{}".format(data.decode("utf-8")))
        
        
        if str(res.status) == "200":
          self.changeResult = "Success"     
        else:
          dict=json.loads(data.decode('utf-8'))
          self.changeResult = str(dict['ERSResponse']['messages'][0]['title'])
          
        print(self.changeResult)




class GuessNumbers(models.Model):
    name = models.CharField(max_length = 24)

    lottos = models.CharField(max_length = 255, default = '[1,2,3,4,5,6]')

    text = models.CharField(max_length = 255, default = '"solution hello"')

    num_lotto = models.IntegerField(default = 5)

    update_date = models.DateTimeField()

    def generate(self):

        self.lottos = ""
        origin = list(range(1,46))
        for _ in ramge(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess)+'\n'
        self.update_date = timezone.now()
        self.save()
