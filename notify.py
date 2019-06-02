import requests

RESPONSE_HEADER = {200: "Success",
                   400: "Unauthorized request",
                   401: "Invalid access token",
                   500: "Failure due to server error",
                   0: "Processed over time or stopped"}


def line_notify(token, msg):
    # https://notify-bot.line.me
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code

