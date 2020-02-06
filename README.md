# line-notify-sender
A Simple Front End for LINE Notify

## Prerequisites

You have to generate access token on below site.

https://notify-bot.line.me

## Package Dependencies

```
pip install requests
```

## Usage

Fill the tokens to auth.json that you got from LINE Notify website
```
{
    "TOEKN_0_ALIAS": "TOKEN_0",
    "TOKEN_1_ALIAS": "TOKEN_1"
    "LINE": "//FILL_THE_TOKEN_HERE"
}
```

Run the program by GUI
```
python gui_sender.py
```

Run the program by console
```
python sender.py "MESSAGE CONTENT"
```

## Reference

[LINE Notify API Document](https://notify-bot.line.me/doc/)
