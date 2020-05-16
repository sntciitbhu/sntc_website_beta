import os
import requests
import json
from collections import namedtuple

class user():

    
    def __init__(self):
        self.heading = ['name', 'email', 'rollnumber', 'bday', 'phone', 'gender', 'hostel', 'institute', 'branch', 'course', 'year', 'skills', 'interests', 'superhero', 'sub_clubs', 'achievements', 'notifications', 'meassages']
        self.url = "https://script.google.com/macros/s/AKfycbzUVKHuk3EP8sIrJtPd9zrAPxtkC8Q-aOqtlRyGdcmqSvNp5sA/exec?"
        self.details = {}

    
    def getdetails(self ,id_token):
        payload = {'action': "getstudent",
                    'id_token':id_token}
        response = requests.get(self.url,params=payload)
        vals = response.json()
        # print (vals)
        self.details = vals
        return self.details


    def create(self, response):
        data = json.dumps(response)
        print(data)
        self.response = response
        payload = {'action': 'createuser'}

        response = requests.post(self.url,data =data, params = payload)
        vals = response.json()
        self.details = vals
        return self.details

    def update(self, response, action):
        data = json.dumps(response)
        print(data)
        self.response = response
        payload = {'action': action}
        response = requests.post(self.url,data=data, params=payload)
        vals = response.json()
        self.details = vals
        return self.details


class superuser():

    
    def __init__(self):
        self.heading = ['name', 'email', 'rollnumber', 'bday', 'phone', 'gender', 'hostel', 'institute', 'branch', 'course', 'year', 'skills', 'interests', 'superhero', 'sub_clubs', 'achievements', 'notifications', 'meassages']
        self.url = "https://script.google.com/macros/s/AKfycbzUVKHuk3EP8sIrJtPd9zrAPxtkC8Q-aOqtlRyGdcmqSvNp5sA/exec?"
        self.details = {}

    
    def allStudents(self):
        payload = {'action': "getAllStudents"}
        response = requests.get(self.url,params=payload)
        vals = response.json()
        data_table = [[vals[head][row] for head in self.heading] for row,_ in enumerate(vals[self.heading[0]])]
        return self.heading,data_table

