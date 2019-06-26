from django.test import TestCase

# Create your tests here.
import jwt
import datetime
import http.client
import base64
import ssl
import sys
import json
import urllib.request
import ast
import requests

class jwtTest:
  serverIP = ""
  adminID = ""
  adminPW = ""
  data = ""
  
  tenants = []
  eGeos = []
  intHosts = []
  exHosts = []
  cusHosts = []
  securityEvents = []
  exThreats = []
  
  
  def __init__(self, ip, id, pw):
    self.serverIP = ip
    self.adminID = id
    self.adminPW = pw
    
    self.getTenants()
    self.eGeos = self.getDataWithId(str(self.tenants[0]['id']), '/externalGeos/tags')
    self.intHosts = self.getDataWithId(str(self.tenants[0]['id']), '/internalHosts/tags')
    self.exHosts =  self.getDataWithId(str(self.tenants[0]['id']), '/externalHosts/tags')
    self.cusHosts = self.getDataWithId(str(self.tenants[0]['id']), '/customHosts/tags')
    self.securityEvents = self.getDataWithId(str(self.tenants[0]['id']), '/security-events/templates')
    self.exThreats = self.getDataWithId(str(self.tenants[0]['id']), '/externalThreats/tags')
    
  def getTenants(self):
      try:
        s = self.getSession()
        encoded = self.getEncodedJWT()
        
        url = 'https://'+self.serverIP+'/sw-reporting/v1/tenants'
        sendUrl = url + "?" + str(encoded)
        respone = s.get(sendUrl)
        
        data = respone.json()['data']
        self.tenants = data
        
      except Exception as e:
        print(e)
  
  def getDataWithId(self, id, path):
      try:
        s = self.getSession()
        encoded = self.getEncodedJWT()

        url = 'https://'+self.serverIP+'/sw-reporting/v1/tenants/'+id+path
        sendUrl = url + "?" + str(encoded)
        respone = s.get(sendUrl)
        
        data = respone.json()['data']
        
        print(url)
     
        print(respone.json())
        
        return data

      
      except Exception as e:
        print(e)
        
  
   

  
    
  def getSession(self):
      data = {
        'username': self.adminID,
        'password': self.adminPW
      }
      
      
      
      session = requests.Session()
      res = session.post('https://'+self.serverIP+'/token/v2/authenticate', data=data, verify=False)  
      
      
      return session
    
    
    
  def getEncodedJWT(self):
      claims = {   
         "sub": self.adminID,   
         "name": self.adminID,   
         "admin": True,
       
      }
    
      print("================================")

      encodedJWT = jwt.encode(claims, key='secret', algorithm="HS256")
      print("jwt = " + str(encodedJWT))
      print("================================")
      
      return encodedJWT
      
      
      