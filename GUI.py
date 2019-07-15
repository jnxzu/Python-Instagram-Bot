from tkinter import *
from Bot import *

window = Tk()
window.title("Instagram Bot")
window.resizable(0, 0)
window.geometry("250x300")


def start():
    login = login_input.get()
    pw = pw_input.get()
    hashtag = hashtag_input.get()
    count = int(count_input.get())
    window.destroy()
    new_bot = Bot()
    new_bot.login(login, pw)
    new_bot.like(hashtag, count)


Label(window, text="Login").place(relx=0.5, rely=0.05, anchor=CENTER)
login_input = Entry(window, width=20)
login_input.place(relx=0.5, rely=0.15, anchor=CENTER)
Label(window, text="Password").place(relx=0.5, rely=0.25, anchor=CENTER)
pw_input = Entry(window, width=20, show="*")
pw_input.place(relx=0.5, rely=0.35, anchor=CENTER)
Label(window, text="Hashtag").place(relx=0.5, rely=0.45, anchor=CENTER)
hashtag_input = Entry(window, width=20)
hashtag_input.place(relx=0.5, rely=0.55, anchor=CENTER)
Label(window, text="Count").place(relx=0.5, rely=0.65, anchor=CENTER)
count_input = Entry(window, width=20)
count_input.place(relx=0.5, rely=0.75, anchor=CENTER)

start = Button(window, text="Start", width=5, command=start).place(relx=0.5, rely=0.9, anchor=CENTER)

window.mainloop()
