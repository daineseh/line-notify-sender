import os
import sys

from auth import Token
from notify import RESPONSE_HEADER, line_notify

AUTH_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'auth.json')
LINE_AUTH_KEY = 'LINE'


def main():
    try:
        auth_obj = Token(AUTH_FILE)
    except Exception as e:
        raise ValueError(e)

    msg = ' '.join(sys.argv[1:])

    req = line_notify(auth_obj.get_data(LINE_AUTH_KEY), msg)
    req_msg = RESPONSE_HEADER.get(req)
    if not req_msg:
        req_msg = RESPONSE_HEADER.get(0)
    print(f'[LINE] {req}: {req_msg}')


if __name__ == '__main__':
    main()
