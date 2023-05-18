import urllib.request , urllib.error , urllib.parse 
from bs4 import BeautifulSoup 
import dummy_client as dc
import socket 
from tkinter import *

url = ""
def getFileContent(fileName):
    file = open(fileName, 'r')
    content = file.read()
    file.close()
    return content


def onlineServer(url):
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        content = soup.get_text()
        text = Text(second_frame )
        text.pack(fill="both", expand=True)
        text.insert(INSERT,content)
        text.config(state=DISABLED)


def offlineServer():
        
    content = getFileContent('File.txt')
    text = Text(second_frame)
    text.pack(fill="both", expand=True)
    text.insert(INSERT, content)
    text.config(state=DISABLED)
        

def handleLocalServer():
    
    if('local_server' in url):
        file1 = open("File.txt", "w")
        IP , port = dc.getUrlAddrees(url)
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((IP , port))
        order = url.split('/')[-1]
        while (True):
            s.send(order.encode())
            message = s.recv(1024)
            if 'end' in message.decode() :
                file1.close() 
                s.close()
                break
            file1.write(message.decode())


def searchButtonHandler():
    global url
    url = str(search_box.get())
    handleLocalServer()
    if 'local_server' not in url:            
        onlineServer(url)
    else :
        offlineServer()
    show_second_page()


#==================================================================================================================
#==================================================================================================================


def show_first_page():

    for widget in second_frame.winfo_children():
        widget.destroy()
    second_frame.place_forget()
    main_frame.place(relwidth=1, relheight=1)

def show_second_page():
    main_frame.place_forget()
    second_frame.place(relwidth=1, relheight=1)
    # Back button for the second page
    back_button = Button(second_frame, text="Back", font=("Arial", 15), bd=4, command=show_first_page, relief="raised", fg="darkblue")
    back_button.place(x=1400, y=740)  # Adjust the position as needed




def exit_program():
    window.destroy()
    sys.exit()



#---------------------------------------------

window = Tk()
window.title("Browser-like GUI")
window.attributes("-fullscreen", True)

# Create the main frame
main_frame = Frame(window)
main_frame.place(relwidth=1, relheight=1)

main_frame.pack(fill="both", expand=True)

# Background image
background_image = PhotoImage(file="img2.png")  # Replace with your background image path
background_canvas = Canvas(main_frame, width=1920, height=1800)  # Adjust the canvas size as needed
background_canvas.pack(fill="both", expand=True)
background_canvas.create_image(0, 0, image=background_image, anchor="nw")

#-----------------------------------------------------------------------------------------------------------------\n                 Welcome ...\nThis is a simple Browser-like GUI using Python \n You can here search on the website u want and this browser will get u that site (as a text file )\n  > if u want the local files : type ' http//local_server/file_name '\n   > if u want to search online : type the url u want 
label1 = Label(main_frame, text=" < Welcome > ", font=("century", 25) ,bd=10 ,relief="groove", highlightthickness=5, highlightbackground="gray")
label1.place(x=80, y=60)  # Adjust the position as needed


label2 = Label(main_frame, text="This is a simple Browser-like GUI using Python  ", font=("century", 20) ,bd=4 ,relief="groove", highlightthickness=1, highlightbackground="gray")
label2.place(x=80, y=150)  # Adjust the position as needed


label3 = Label(main_frame, text="\nYou can here search on the website u want and this browser will get u that site (as a text file )\n> if u want the local files : type ' http//local_server/file_name '\n> if u want to search online : type the url u want  \n   ", font=("century", 14) ,bd=1 ,relief="groove", highlightthickness=1, highlightbackground="gray" , fg="black")
label3.place(x=80, y=220)  # Adjust the position as needed


# Search box
search_box = Entry(main_frame,background ="lightgray" , width=80, font=("Arial", 16), bd=2, relief="ridge" , highlightthickness=1, highlightbackground="black" , fg="darkblue")
search_box.place(x=100, y=450)  # Adjust the position as needed

# Search button
search_button = Button(main_frame, text="  Search  ", font=("Arial", 15 , "bold") , bd=5 , command=searchButtonHandler, relief="raised", fg="darkblue" )
search_button.place(x=1100, y=442)  # Adjust the position as needed

exit_button = Button(main_frame, text=" Exit > ", font=("Arial", 18 , "bold") , bd=5 , command=exit_program, relief="raised", fg="darkred" )
exit_button.place(x=1360, y=60)


button_images = [
    PhotoImage(file="Facebook.png"),  # Replace with your button image paths
    PhotoImage(file="BBCPS.png"),
    PhotoImage(file="NG.png"),
    PhotoImage(file="NYP.png"), #https://www.nypl.org/
    PhotoImage(file="wekebedia.png"),
    PhotoImage(file="iug.png")
]

button_frames = Frame(main_frame)
button_frames.place(relx=0.5, rely=0.9, anchor="center")



def getFacebook() :
    url = "https://www.facebook.com/"
    onlineServer(url)
    show_second_page()

def getBBCPS() :
    url = "https://www.bbc.com/arabic/40739743"
    onlineServer(url)
    show_second_page()


def getNG() :
    url = "https://www.nationalgeographic.com/"
    onlineServer(url)
    show_second_page()

def getNYP() :
    url = "https://www.nypl.org/"
    onlineServer(url)
    show_second_page()


def getWekebedia() :
    url = "https://en.wikipedia.org/wiki/Main_Page"
    onlineServer(url)
    show_second_page()

def getIUG() :
    url = "https://www.iugaza.edu.ps/en/"
    onlineServer(url)
    show_second_page()





buttons = []
for i in range(6):
    match i:
        case 0:
            button = Button(button_frames, image=button_images[i], bd=0 , command=getFacebook)
            button.pack(side="left", padx=30)
            buttons.append(button)
        case 1:
            button = Button(button_frames, image=button_images[i], bd=0 , command=getBBCPS)
            button.pack(side="left", padx=30)
            buttons.append(button)
        case 2:
            button = Button(button_frames, image=button_images[i], bd=0 , command=getNG)
            button.pack(side="left", padx=30)
            buttons.append(button)
        case 3:
            button = Button(button_frames, image=button_images[i], bd=0 , command=getNYP)
            button.pack(side="left", padx=30)
            buttons.append(button)
        case 4:
            button = Button(button_frames, image=button_images[i], bd=0 , command=getWekebedia)
            button.pack(side="left", padx=30)
            buttons.append(button)
        case 5:
            button = Button(button_frames, image=button_images[i], bd=0 , command=getIUG)
            button.pack(side="left", padx=30)
            buttons.append(button)



second_frame = Frame(window)
second_frame.pack(fill="both", expand=True)


window.mainloop()
