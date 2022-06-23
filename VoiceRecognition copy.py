import tkinter
import tkinter as tk
import speech_recognition as sr


window=tk.Tk()
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
window.configure(background="white")
entry2=tk.Text (window)
entry2.grid(row=0,column=0)
r = sr.Recognizer()
class Listener():
    def __init__(self):
        print("Hi")
    def listening(self):
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:
                print(1)
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                #listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio

                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                MyText=MyText+' '
                print(MyText)
                entry2.insert(tkinter.END, MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format((e)))

        except sr.UnknownValueError:
            print("unknown error occured")


listenings=Listener()
while(True):
    window.after(10, listenings.listening())
window.mainloop()