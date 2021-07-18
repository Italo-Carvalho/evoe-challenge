import re
import requests
import json
from flask import session, request
from werkzeug.utils import redirect


class WebService():
    url = 'http://127.0.0.1:8000'
    refresh = None

    def createUser(self, username, password):
        response = requests.post(f"{self.url}/user/",
             data={"username":username, "password":password})
        return response

    def loginUser(self, username, password):
        login = requests.post(f"{self.url}/token/",
                     data={"username":username,"password":password})
        if login.json()['refresh']:
            return login.json()['refresh']
        return login

    def accessToken(self, refresh):

        if refresh:
            response = requests.post(f"{self.url}/token/refresh/", data={"refresh":refresh})   
            if response.status_code == 200:
                return response.json()['access']
            breakpoint()    
        else:
            
            return 'denied'

         
    def getData(self, refresh, page):
        auth = self.accessToken(refresh)
        if auth != 'denied':
            data =  requests.get(f"{self.url}/notes/?page={page}"
                , headers={'Authorization': f'Bearer {auth}'})

            return json.loads(data.content)
        return 'denied'

    def createData(self, refresh, title, body):
        auth = self.accessToken(refresh)
        if auth != 'denied':
            return requests.post(f"{self.url}/notes/"
                ,data={"title": title, "body": body}
                , headers={'Authorization': f'Bearer {auth}'}).status_code
        return 'denied'
            
    def delData(self , refresh, pk):
        auth = self.accessToken(refresh)
        if auth != 'denied':
            return requests.delete(f"{self.url}/notes/{pk}"
                , headers={'Authorization': f'Bearer {auth}'}).status_code
        return 'denied'

    def putData(self, refresh, pk, title, body):
        auth = self.accessToken(refresh)
        if auth != 'denied':
            return requests.put(f"{self.url}/notes/{pk}"
                ,data={"title": title, "body": body}
                , headers={'Authorization': f'Bearer {auth}'}).status_code
        return 'denied'