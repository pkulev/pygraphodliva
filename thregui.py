# from threading import Queue, Thread
from Tkinter import Label, Tk


def main():
    root = Tk()
    w = Label(root, text="Hello, world!")
    w.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
