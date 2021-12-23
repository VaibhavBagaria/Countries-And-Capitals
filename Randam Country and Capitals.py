from tkinter import *
import random
root=Tk()
root.title("Countries and Capitals")
root.geometry("400x400")
root.configure(background="lightblue")

title=Label(root,text="Countries and Capitals")
textinput=Entry(root,text="Countries")
textinput2=Entry(root, text="Capital")
Countrylist=Label(root)
Capitallist=Label(root)
label1=Label(root,text="The Country and Capital Has Been Chosen: ")
listCountries=[]
listCapitals=[]

def luckyfriend():
    length1=len(listCountries)
    random_country=random.randint(0,length1-1)
    Country=listCountries[random_country]
    Capital=listCapitals[random_country]
    label1["text"]="The Country and Capital Has Been Chosen: "+str(Country)+" and "+str(Capital)
    

def addfriend():
    x=textinput.get()
    y=textinput2.get()
    listCountries.append(x)
    listCapitals.append(y)
    Countrylist["text"]="Countries: "+str(listCountries)
    Capitallist["text"]="Capital: "+str(listCapitals)
    textinput.delete(0,END)
    textinput2.delete(0,END)

button1=Button(root,text="Choose Random Country and Capital", command=luckyfriend)
btn2=Button(root,text="Add Names To the List", command=addfriend)

title.place(relx=0.5, rely=0.1, anchor=CENTER)
textinput.place(relx=0.3, rely=0.2, anchor=CENTER)
textinput2.place(relx=0.7, rely=0.2, anchor=CENTER)
btn2.place(relx=0.5, rely=0.3, anchor=CENTER)
Countrylist.place(relx=0.3, rely=0.4, anchor=CENTER)
Capitallist.place(relx=0.7, rely=0.4, anchor=CENTER)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()