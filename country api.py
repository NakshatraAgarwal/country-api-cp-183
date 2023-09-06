from tkinter import *
import json
import requests

root = Tk()
root.geometry("500x500")
root.overrideredirect(FALSE)

name = Label(root,text="Capital City Name",font=("times",25,"bold"))
name.place(relx=0.2,rely=0.2,anchor=W)

c_entry = Entry(root)
c_entry.place(relx=0.2,rely=0.3,anchor=W)


country = Label(root)
country.place(relx=0.2,rely=0.5,anchor=W)

region = Label(root)
region.place(relx=0.2,rely=0.6,anchor=W)

lan = Label(root)
lan.place(relx=0.2,rely=0.7,anchor=W)

pop = Label(root)
pop.place(relx=0.2,rely=0.8,anchor=W)

area = Label(root)
area.place(relx=0.2,rely=0.9,anchor=W)

def details():
    api = requests.get("https://restcountries.com/v2/capital/"+ c_entry.get())
    api_json = json.loads(api.content)
    
    countryy = api_json[0]["name"]
    reg = api_json[0]["region"]
    lang = api_json[0]["languages"][0]["name"]
    popn = api_json[0]["population"]
    arean = api_json[0]["area"]
    
    country["text"] = "Country: " + str(countryy)
    region["text"] = "Region: " + str(reg)
    lan["text"] = "Language: " + str(lang)
    pop["text"] = "Population: " + str(popn)
    area["text"] = "Area: " + str(arean)
    
    
btn = Button(root,text="Show City Details",command=details)
btn.place(relx=0.2,rely=0.4,anchor=W)

root.mainloop()
    
    
    


