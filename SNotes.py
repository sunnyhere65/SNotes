import os
from datetime import date
from tkinter import *
import webbrowser
from PIL import ImageGrab

root = Tk()
root.title("SNotes")
icon = PhotoImage(file='./notes.png')
root.iconbitmap('./notes.ico')

label = Label(root, bg='gray3')
label.place(x=0, y=0, relwidth=1, relheight=1)
today = str(date.today())
mainhead = Label(root, text="Enter the subject", bg="gray3",
             border=0, font=("Helvetica", 14), fg="green1")
mainhead.pack(pady=(30, 0))
fnam = Entry(root, width=18, fg="gray7", bg="white", border=0,
             font=("Verdana", 13), justify="center")
fnam.pack(pady=(10, 5), ipady=5)
fnam.focus()

path = os.path.normpath(os.path.expanduser("~/Desktop"))
os.chdir(path)
isnt = os.path.isdir("SNotes")
if not isnt:
    os.mkdir("SNotes")
    os.chdir("SNotes")
else:
    os.chdir("SNotes")


def ceil(num):
    l = str(num).split(".")
    if "." in str(num):
        if int(l[1]) != 0:
            return int(l[0])+1
    return int(l[0])


def func():
    global info
    ent = fnam.get()
    fnam.delete(0, END)
    iss = os.path.isdir(str(ent))
    if not iss:
        os.mkdir(ent)
        info.set(ent + " is created.")
        labelinf.config(fg="green")

    else:
        info.set(ent + " already exists.")
        labelinf.config(fg="gold")


def next():
    root.withdraw()
    global top
    top = Toplevel()
    top.title("SNotes")
    top.iconphoto(False, icon)

    label = Label(top, bg="gray3")
    label.place(x=0, y=0, relwidth=1, relheight=1)

    def opendir():
        pa = v.get()

        today = str(date.today())
        if (os.getcwd().split('\\'))[-1] == today:
            os.chdir("../..")


        isd = os.path.isdir(pa)
        if isd:
            os.chdir(pa)
        else:
            os.mkdir(pa)
            os.chdir(pa)


        isT = os.path.isdir(today)
        isT1 = os.path.isdir("../" + today)
        if not isT and not isT1:
            os.mkdir(today)
            os.chdir(today)
        else:
            os.chdir(today)


    target = os.path.normpath(path+"/SNotes/")
    subjectListScan = [f.name for f in os.scandir(target) if f.is_dir()]
    v = StringVar()
    rbframe = Frame(top, bg="gray3")
    rbframe.pack(padx=6, pady=6)
    num = 0
    col = 0
    for i in subjectListScan:
        name = Radiobutton(rbframe, text=i, variable=v, bg="gray3", fg="cyan", value=i, command=opendir, wraplength=100,
                           activebackground="gray3", activeforeground="white", font=("Helvetica", 11), selectcolor="black")
        if num == 4:
            num = 0
            col += 1
        name.grid(row=num, column=col, pady=5, padx=5, sticky='w')
        num += 1

    def take_ss():
        top.withdraw()
        top.after(200)
        isT = os.path.isdir("../" + today)
        if not isT:
            pass
        else:
            image = ImageGrab.grab()
            noOfSS = ([name for name in os.listdir('.') if os.path.isfile(name)])
            if noOfSS:
                noOfSS = int(((noOfSS[-1]).split("."))[0])
            else:
                noOfSS = 0
                
            file_name = str(noOfSS + 1)
            image.save(file_name + ".png")
        top.deiconify()
        button2.focus()

    def web():
        webbrowser.open('https://github.com/sunnyhere65')

    def goback():
        foldername = (os.getcwd().split('\\'))[-1]

        if foldername in subjectListScan:
            os.chdir("../")

        elif foldername == today:
            os.chdir("../..")

        top.withdraw()
        root.deiconify()

    button2 = Button(top, text="Take  Screenshot", command=take_ss,
                     bg="black", border=2, fg="white", padx=20)
    button2.config(activebackground="gray8",
                   activeforeground="beige", font=("Verdana", 10))
    button2.pack(pady=(10, 0), ipady=7)
    button2.focus()

    ext = Button(top, text="Go Back", command=goback, justify="center", activebackground="gray8",
                 activeforeground="beige")
    ext.config(padx=10, bg="black", fg="white",
               border=2, relief="raised", font=("Verdana", 10))
    ext.pack(pady=(10, 8), ipady=5)

    widthCalc = ceil(len(subjectListScan)/4)*103;
    if widthCalc < 250:
        widthCalc = 250

    Topfollow = Button(top, text="Creator : @sunny", font=("Verdana", 10), bg="gray8", border=0, fg="yellow",
                       activebackground="gray8", activeforeground="gold", command=web, width=top.winfo_width())

    rbframe.update()
    padcalc = 320 -  top.winfo_height() - 34
    Topfollow.pack(pady=(padcalc,0), ipady=5)
  
    top.protocol("WM_DELETE_WINDOW", root.quit)
    top.geometry(f"{widthCalc + 50}x320")
    top.resizable(1, 0)


def web():
    webbrowser.open('https://github.com/sunnyhere65')


btn = Button(root, text="Add", command=func,
             activebackground="gray8", activeforeground="white")
btn.config(padx=20, pady=7, bg="black", fg="white",
           border=2, relief="raised", font=("Helvetica", 11))
btn.pack(pady=(14, 0))

nextb = Button(root, text="Next", command=next, justify="center", activebackground="gray8",
               activeforeground="white")
nextb.config(padx=17, pady=5, bg="black", fg="white",
             border=2, relief="raised", font=("Helvetica", 11))
nextb.pack(pady=(14, 0))


info = StringVar()

labelinf = Label(root, textvariable=info,
                 width=50, height=3, bg="gray3", fg="gray3", font=("Helvetica", 11))
labelinf.pack(pady=(5,0))


follow = Button(root, text="Creator : @sunny", font=("Verdana", 10), bg="gray8", border=0, fg="yellow",
                activebackground="gray8", activeforeground="gold", command=web,  width=root.winfo_width())
follow.pack(pady=(5, 0), ipady=5)

root.geometry("300x310")

root.resizable(0, 0)
root.mainloop()
