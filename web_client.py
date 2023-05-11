import urllib.request , urllib.error , urllib.parse 
from bs4 import BeautifulSoup 
import dummy_client as dc
import socket 
from tkinter import *

url = ""
def getFileContent(fileName):
        file = open(fileName , 'r')
        current_chunck = file.readline()
        content = ""
        while (current_chunck != ""):
            content += current_chunck
            current_chunck = file.readline()
        file.close()
        return content 
def onlineServer(url):
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        content = soup.get_text()
        text = Text(window )
        text.pack()
        text.insert(INSERT,content)
        frame.destroy()

def offlineServer():
        text = Text(window )
        text.config()
        text.insert(INSERT,getFileContent('File.txt'))
        text.config(state=DISABLED)
        text.pack()
        frame.destroy()

def handleLocalServer():
    if('local_server' in url):
        file1 = open("File.txt", "w")
        IP , port = dc.getUrlAddrees(url)
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((IP , port))
        print(f"This has been excuted({IP},{port})")
        order = url.split('/')[-1]
        print(order)
        while (True):
            s.send(order.encode())
            message = s.recv(1024)
            if 'end' in message.decode() :
                file1.close() 
                break;
            file1.write(message.decode())

def searchButtonHandler():
    url = str(E1.get())
    handleLocalServer()
    if ('local_server' not in url):            
        onlineServer(url)
    else :
        offlineServer()

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
button = Button(frame , command=searchButtonHandler , text="search")
button.pack(side=TOP)
window.mainloop()


