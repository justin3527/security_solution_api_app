import http.client
import base64
import ssl
import sys
import json
import urllib.request
import ast
import requests, time

class FirePower:
  serverIP = ""
  adminID = ""
  adminPW = ""
  baseURL = ""
  auth_path = ""
  serverInfo = {}
  accessPolicies = []
  filePolicies = []
  natPolicies = []
  intrusionPolicies = []
  policyRules = []
  ruleActions = []
  ruleNames = []
  snmpAlerts = []
  syslogAlerts = []
  
  def __init__(self):
    return
  
  def __init__(self, ip=None, id=None, pw=None):
    
    if ip == None:
      return
    else:
      self.serverIP = ip
      self.adminID = id
      self.adminPW = pw
      self.baseURL = "https://"+self.serverIP
      self.auth_path = self.baseURL+'/api/fmc_platform/v1/auth/generatetoken' 
                         
      self.getServerInfo()
      self.getAccessPolicies()
      self.getPolicyRules()
      
      self.getFilePolicies()
      self.getIntrusionPolicies()      
      self.getPolicyRules()
      
      self.getSnmpAlerts()
      self.getSyslogAlerts()
      
  
  def getPolicyRules(self):
       self.policyRules = []
      
       respone = self.requestGet("/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/"+self.accessPolicies[0]['id']+"/accessrules")
       
       print("@#$#%^%$&$^&%^*^&*^&*%^&@#$#%^%$&$^&%^*^&*^&*%^&")
       print(respone)
       print("@#$#%^%$&$^&%^*^&*^&*%^&@#$#%^%$&$^&%^*^&*^&*%^&")
       self.policyRules = respone['items']
       '''   
       respone = self.requestGet("/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies/"+self.accessPolicies[0]['id']+"/accessrules")
       self.policyRules.append(respone)
       print("-====================")
       print(self.policyRules)
       names = ""
       
       for k in range(len(self.policyRules)):
         for i in self.policyRules[k]:
           names = names + i['name'] + "/"
         self.ruleNames.append(names)
         '''
       print(self.ruleNames)  
 
  def getFilePolicies(self):
  
    respone = self.requestGet("/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/filepolicies")
    print("==========file================")
    print(respone['items'])
    self.filePolicies = respone['items']
    
  def getNATPolicies(self):
    respone = self.requestGet("/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/ftdnatpolicies")
    print("==========nat================")
    print(respone['items'])
    
    self.natPolicies = respone['items']
    
  def getIntrusionPolicies(self):
    
    respone = self.requestGet("/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/intrusionpolicies")
    print("==========intrusion================")
    print(respone['items'])
    
    self.intrusionPolicies = respone['items']
    
  def getSnmpAlerts(self):
    
    respone = self.requestGet("/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/snmpalerts")
    print("==========snmpAlert================")
    print(respone['items'])
    
    self.snmpAlerts = respone['items']
    
  def getSyslogAlerts(self):
    
    respone = self.requestGet("/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/syslogalerts")
    print("==========syslogAlert================")
    print(respone['items'])
    
    self.syslogAlerts = respone['items']
      
  def getServerInfo(self):
    respone = self.requestGet("/api/fmc_platform/v1/info/serverversion")
    self.serverInfo = respone['items'][0]
    print(self.serverInfo)
    print(self.serverInfo["geoVersion"])
      
  def getAccessPolicies(self):
    respones = self.requestGet("/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies")
      
    self.accessPolicies = respones['items']    
    
  
  def requestGet(self, path):
    headers = {'Content-Type': 'application/json'}
    
    try:
        # 2 ways of making a REST call are provided:
        # One with "SSL verification turned off" and the other with "SSL verification turned on".
        # The one with "SSL verification turned off" is commented out. If you like to use that then 
        # uncomment the line where verify=False and comment the line with =verify='/path/to/ssl_certificate'
        # REST call with SSL verification turned off: 
        # r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)
        # REST call with SSL verification turned on: Download SSL certificates from your FMC first and provide its path for verification.
        
        s = requests.Session() 
        r = s.post(self.auth_path, headers=headers, auth=requests.auth.HTTPBasicAuth(self.adminID,self.adminPW), verify=False)
        
        auth_headers = r.headers
        auth_token = auth_headers.get('X-auth-access-token', default=None)
        if auth_token == None:
            print("auth_token not found. Exiting...")
            sys.exit()
    except Exception as err:
        print ("Error in generating auth token --> "+str(err))
        return
     
    headers['X-auth-access-token']=auth_token
     
    
    url = self.baseURL + path
    if (url[-1] == '/'):
        url = url[:-1]
     
    # GET OPERATION
     
    
    try:
        # REST call with SSL verification turned off: 
        # r = requests.get(url, headers=headers, verify=False)
        # REST call with SSL verification turned on:
        r = requests.get(url, headers=headers, verify=False)
        status_code = r.status_code
        resp = r.text
        if (status_code == 200):
            print("GET successful. Response data --> ")
            json_resp = json.loads(resp)
            print(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))
            
            return json_resp
        else:
            r.raise_for_status()
            print("Error occurred in GET --> "+resp)
    except requests.exceptions.HTTPError as err:
        print ("Error in connection --> "+str(err)) 
    finally:
        if r : r.close()
        
  
  def getSession(self):
      data = {
        'username': self.adminID,
        'password': self.adminPW
      }
      
      
      
      session = requests.Session()
      res = session.post(self.auth_path, data=data, verify=False)  
      
      
      return session

  
  def getAccessPliciesData():  
    return 1