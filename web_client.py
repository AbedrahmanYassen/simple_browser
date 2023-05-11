import urllib.request , urllib.error , urllib.parse 
from bs4 import BeautifulSoup 
import dummy_client as dc
import socket 
url = ""

from tkinter import *
 
window = Tk()
window.config(bg='white')
frame = Frame(window)
frame.place(x=200 , y=200)
window.title("IUGoogle")
width= window.winfo_screenwidth() * 0.5
height= window.winfo_screenheight() * .5
#setting tkinter window size
window.geometry("%dx%d" % (width, height))

E1 = Entry(frame, bd = 5 , width=200)
E1.pack(side = RIGHT)
url = ""
def searchButtonHandler():
    url = str(E1.get())
    if('local_server' in url):
        file1 = open("File.txt", "w")
        IP , port = dc.getUrlAddrees(url)
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((IP , port))
        print(f"This has been excuted({IP},{port})")
        order = url.split('/')[-1]
        print(order)
        while (True):
            print("I am stuck in here")
            s.send(order.encode())
            message = s.recv(1024)
            if 'end' in message.decode() :
                file1.close() 
                break;
            file1.write(message.decode())

    if ('local_server' not in url):            
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        print(soup.prettify())
        content = soup.get_text()
        print(content)
        text = Text(window )
        text.pack()
        text.insert(INSERT,content)
        frame.destroy()
    else :
        text = Text(window )
        text.config()
        file = open('File.txt' , 'r')
        current_chunck = file.readline()
        content = ""
        while (current_chunck != ""):
            content += current_chunck
            print(current_chunck)
            current_chunck = file.readline()
        file.close()
        text.insert(INSERT,content)
        text.config(state=DISABLED)
        text.pack()
        frame.destroy()
button = Button(frame , command=searchButtonHandler , text="search")
button.pack(side=TOP)
window.mainloop()


