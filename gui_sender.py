from tkinter import messagebox
import sys
import tkinter as tk

from auth import Token
from notify import RESPONSE_HEADER, line_notify


def send_text(text):
    assert isinstance(text, tk.Text)
    content = text.get("1.0", tk.END)
    if not content.strip():
        return

    for name, token in auth_obj.datas():
        req = line_notify(token, content)
        req_msg = RESPONSE_HEADER.get(req)
        if not req_msg:
            req_msg = RESPONSE_HEADER.get(0)
        status.config(text=req_msg)


def main():
    global win
    global auth_obj
    global status

    try:
        auth_obj = Token("auth.json")
    except Exception as e:
        tk.messagebox.showerror("Error", e)
        sys.exit(1)

    win = tk.Tk()
    win.title("LiNe nOtIfy Sender")

    label = tk.Label(win, text="Message content:", anchor=tk.W)
    label.pack(fill=tk.BOTH)

    text = tk.Text(win)
    text.pack(fill=tk.BOTH)

    button = tk.Button(win, text="Send", command=lambda: send_text(text))
    button.pack()

    status = tk.Label(win, text="Ready", anchor=tk.W)
    status.pack(fill=tk.BOTH)

    win.mainloop()


if __name__ == '__main__':
    main()

