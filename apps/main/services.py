import os
import requests
import json
from collections import namedtuple

class user():

    
    def __init__(self):
        self.heading = ["auth_token","name","year","branch","email","college","roll_number","achievements","interests","sub_clubs","notifications","meassages"]
        self.url = "https://script.google.com/macros/s/AKfycbzUVKHuk3EP8sIrJtPd9zrAPxtkC8Q-aOqtlRyGdcmqSvNp5sA/exec?"
        self.details = {}

    
    def getdetails(self ,id_token):
        payload = {'id_token':id_token}
        response = requests.get(self.url,params=payload)
        vals = response.json()
        # print (vals)
        self.details = vals
        return self.details


    def create(self, response):
        data = json.dumps(response)
        print(data)
        self.response = response
        response = requests.post(self.url,data)
        vals = response.json()
        # print (vals)
        self.details = vals
        return self.details
