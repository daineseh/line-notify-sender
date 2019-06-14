import json
import os


class Token:
    def __init__(self, json_name):
        with open(json_name) as fp:
            self.__client_secret = json.load(fp)

    def datas(self):
        for key, value in self.__client_secret.items():
            yield (key, value)

    def get_data(self, key):
        if key not in self.__client_secret:
            return None
        return self.__client_secret.get(key)



if __name__ == '__main__':
    token = Token("auth.json")
    print(token)

