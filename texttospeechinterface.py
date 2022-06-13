import tkinter as tk
from gtts import gTTS
import os
language = 'en'
class speech():
    def functions(x2):
        x=x2
        try:
            tempString="afplay -r 1.1 "+x+".mp3"
            if os.system(tempString)!=0:
                raise Exception('wrongcommand does not exist')
        except:
            myobj = gTTS(text=x, lang=language, slow=False)
            stringTemp=x+".mp3"
            myobj.save(stringTemp)
            tempString="afplay -r 1.1 "+x+".mp3"
            os.system(tempString)
window=tk.Tk()
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
window.configure(background="white")
entry1 = tk.Text (window)
entry1.grid(row=0,column=0)
x1=""
speeches=speech
def keyPressed(event):
    global x1
    key=event.char
    if(key==' '):
        if x1=="":
            return
        speeches.functions(x1)
        x1=""
    else:
        x1=x1+key
def deletePressed(event):
    new = ''
    global x1
    for item in x1:
        if item == x1[len(x1)-1]:
            continue
        else:
            new += item
    x1=new
def enterPressed(event):
    global x1
    if x1=="":
        return
    speeches.functions(x1)
    x1=""
window.bind('<Key>', keyPressed)
window.bind('<BackSpace>', deletePressed)
window.bind('<Return>', enterPressed)
window.mainloop()
