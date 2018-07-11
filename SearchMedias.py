from tkinter import *
import webbrowser

yT = "https://www.youtube.com/results?search_query="
ch = "&sp=EgIQAkIECAESAA%253D%253D"

fB = "https://www.facebook.com/search/pages/?q="

tW = "https://twitter.com/search?f=users&vertical=default&q="
user = "&src=tyah"

def Search():
    t = v.get()
    q = t.split()

    def YouTube(q):
        for i in range(len(q) - 1):
            q[i] = q[i] + "+"
        n = "".join(q)
        return yT + n + ch

    def Facebook(q):
        for i in range(len(q) - 1):
            q[i] = q[i] + "%20"
        n = "".join(q)
        return fB + n

    def Twitter(q):
        for i in range(len(q) - 1):
            q[i] = q[i] + "%20"
        n = "".join(q)
        return tW + n + user

    list = [YouTube(q), Facebook(q), Twitter(q)]

    y = webbrowser.open(list[0],new=0, autoraise=True)
    f = webbrowser.open(list[1],new=0, autoraise=True)
    t = webbrowser.open(list[2],new=0, autoraise=True)

root = Tk()
root.title("Search Engine")
root.geometry("300x100")

l = Label(root, text="Search:").grid(row=0)

v = StringVar()
e = Entry(root, textvariable=v)
e.grid(row=0, column=2)

b = Button(root, text="Search", command=Search).grid(row=0, column=3)


# You = Label(root, text="Youtube:").grid(row=5)
# Face = Label(root, text="Facebook:").grid(row=6)
# Twitter = Label(root, text="Twitter:").grid(row=7)


root.mainloop()