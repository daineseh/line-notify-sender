import json
import os


class Token:
    def __init__(self, json_name):
        with open(json_name) as fp:
            self.__client_secret = json.load(fp)

    def get_data(self):
        for key, value in self.__client_secret.items():
            yield (key, value)


if __name__ == '__main__':
    token = Token("token.json")
    print(token)

