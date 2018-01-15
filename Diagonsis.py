import requests
import hmac, hashlib
import base64
import json
from enum import Enum

Gender = Enum("Gender", "Male Female")

SelectorStatus = Enum("SelectorStatus", "Man Woman Boy Girl")

class Diagonsis:
    def __init__(self, username, password, authServiceUrl, language, healthServiceUrl):
        self._handleRequiredArguments(username, password, authServiceUrl, healthServiceUrl, language)

        self._language = language
        self._healthServiceUrl = healthServiceUrl
        self._token = self._loadToken(username, password, authServiceUrl)

    myToken = '<token>'
    myUrl = '<website>'
    head = {'Authorization': 'token {}'.format(myToken)}
    response = requests.get(myUrl, headers=head)

    def _loadToken(self, username, password, url):
        rawHashString = hmac.new(bytes(password, encoding='utf-8'), url.encode('utf-8')).digest()
        computedHashString = base64.b64encode(rawHashString).decode()


        postHeaders = {
            'Authorization': 'Bearer {}'.format(username + ':' + computedHashString)
        }
        responsePost = requests.post(url, headers=postHeaders)

        data = json.loads(responsePost.text)
        return data

