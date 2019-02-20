from django.db import models
import random

# Create your models here.

import http.client
import base64
import ssl
import sys

class getAllUser:
    # host and authentication credentials
    host = "10.0.0.51" # "10.20.30.40"
    user = "ERSAdmin" # "ersad"
    password = "Password1!" # "Password1"

    def __init__(self):
        self.host = "10.0.0.51" # "10.20.30.40"
        self.user = "ERSAdmin" # "ersad"
        self.password = "Password1!" # "Password1"

        conn = http.client.HTTPSConnection("{}:9060".format(self.host), context=ssl.SSLContext(ssl.PROTOCOL_TLSv1))

        creds = str.encode(':'.join((self.user, self.password)))
        encodedAuth = bytes.decode(base64.b64encode(creds))

        headers = {
            'accept': "application/json",
            'authorization': " ".join(("Basic",encodedAuth)),
            'cache-control': "no-cache",
            }

        conn.request("GET", "/ers/config/internaluser/", headers=headers)

        res = conn.getresponse()
        data = res.read()

        print("Status: {}".format(res.status))
        print("Header:\n{}".format(res.headers))
        print("Body:\n{}".format(data.decode("utf-8")))








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
