from tkinter import *
import time
import threading
import random


class TypeSpeedGUI:

    def __init__(self) -> None:
        self.root = Tk()
        self.root.title(" Typing Speed Test")
        self.root.geometry("800x600")

        self.texts = open('texts.txt', 'r').read().split('\n')

        self.frame = Frame(self.root)

        self.target_label = Label(
            self.frame, text=random.choice(self.texts), font=('Arial', 18))
        self.target_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.user_input = Entry(self.frame, width=40, font=('Helvitica', 24))
        self.user_input.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.user_input.bind('<KeyRelease>', self.start)

        self.speed_label = Label(
            self.frame, text='Speed: \n 0:00 CPS \n 0:00 CPM \n 0:00 WPS \n 0:00 WPM', font=('helvitica', 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = Button(
            self.frame, text="Reset", command=self.reset, font=('helvitica', 24))
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.frame.pack(expand=True)

        self.count = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()

        if not self.target_label.cget('text').startswith(self.user_input.get()):
            self.user_input.config(fg='red')
        else:
            self.user_input.config(fg='balck')

        if self.user_input.get() == self.target_label.cget('text')[:-1]:
            self.running = False
            self.user_input.config(fg='green')

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.count += 0.1
            cps = len(self.user_input.get()) / self.count
            cpm = cps * 60
            wps = len(self.user_input.get().split(' ')) / self.count
            wpm = wps * 60

            self.speed_label.config(
                text=f"Speed: \n {cps:.2f}  CPS \n {cpm:.2f} CPM\n {wps:.2f} WPS \n {wpm:.2f} WPM ")

    def reset(self):
        self.running = False
        self.count = 0
        self.speed_label.config(
            text='Speed: \n 0:00 CPS \n 0:00 CPM \n 0:00 WPS \n 0:00 WPM')
        self.target_label.config(text=random.choice(self.texts))
        self.user_input.delete(0, END)


TypeSpeedGUI()
