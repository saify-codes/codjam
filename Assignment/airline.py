import random,os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def listPassengers():
  global screen4
  screen4 = Toplevel(screen)
  screen4.geometry("600x700")
  screen4.title("Emirates")
  screen4.config(bg="white")
  screen4.resizable(False,False)
  with open("info/passengerslist.log") as file:
    for x in file:  
      Label(screen4, text=x, bg="white",font=("poppins",10,"bold")).pack(anchor=W,padx=30)

def btn():
  screen = Frame(screen3,bg="white")
  Button(screen,text = "Book flight", height = "2", width = "20", padx=10,fg="white", bg="#218838", relief="flat",command=book_flight).grid(row=2,column=0,padx=10)
  Button(screen,text = "Flight info",height = "2", width = "20", padx=10,fg="white", bg="#17A2B8", relief="flat",command=flight_info).grid(row=2,column=1,padx=10)
  Button(screen,text = "Cancel flight",height = "2", width = "20", padx=10,fg="white", bg="#BD2130", relief="flat",command=cancel_flight).grid(row=2,column=2,padx=10)
  return screen

def status():
    fp = open("info/bookings.log","r")
    number_of_bookings = fp.readline()
    fp.close()
    fp = open("info/amount.log","r")
    amount = fp.readline()
    fp.close()
    fp = open("info/cancelled flight.log","r")
    cancelled_flights = fp.readline()
    fp.close()

    screen = Frame(screen3,bg="white")
    List = Frame(screen,bg="white")
    Label(List, text="Total bookings", bg="white",font=("poppins",10,"bold")).pack(side=LEFT)
    Label(List, text=number_of_bookings, bg="white").pack(side=LEFT, anchor=E,expand=True)
    List.pack(padx=25,expand=True,fill=X)

    List2 = Frame(screen,bg="white")
    Label(List2, text="Total Amount", bg="white",font=("poppins",10,"bold")).pack(side=LEFT)
    Label(List2, text=amount+'$', bg="white").pack(side=LEFT, anchor=E,expand=True)
    List2.pack(padx=25,expand=True,fill=X)

    List3 = Frame(screen,bg="white")
    Label(List3, text="Cancelled Flights", bg="white",font=("poppins",10,"bold")).pack(side=LEFT)
    Label(List3, text=cancelled_flights, bg="white").pack(side=LEFT, anchor=E,expand=True)
    List3.pack(padx=25,expand=True,fill=X)

    List4 = Frame(screen,bg="red")
    Button(List4, text="View Passengers List", bg="black",fg="White",relief="flat",font=("poppins",10,"bold"),command=listPassengers).pack(side=LEFT,fill=X,expand=True)
    List4.pack(padx=25,expand=True,fill=X,pady=30)
    return screen

def airline(session=False):
  global screen3
  screen2.destroy()
  screen3 = Toplevel(screen)
  screen3.geometry("600x500")
  screen3.title("Emirates")
  screen3.config(bg="white")
  screen3.resizable(False,False)
  Label(screen3,text = "Dashboard", bg = "white", height = "2", font = ("poppins", 13)).pack(anchor=W,padx=25)
  btn().pack()
  Label(screen3,text = "", bg="white").pack()
  Label(screen3,text = "", bg="white").pack()
  status().pack(fill=X)

def cancel_flight():
  global screen3
  flight = StringVar()
  screen = Toplevel(screen3)
  screen.title("flight Cancellation")
  screen.geometry("300x250")
  Label(screen,text="Flight ID").grid(row=0,column=0,sticky=W,padx=10)
  fi = Entry(screen, textvariable=flight)
  fi.grid(row=0,column=1)
  def cancel():
      global cancelled_flights
      os.remove(flight.get()+'.txt')
      Label(screen,text="Flight Cancelled",fg="red",bg="yellow")
      with open("info/cancelled flight.log",'r') as file:
        cancelled_flights = int(file.readline())
      with open("info/cancelled flight.log",'w') as file:
        file.write(str(cancelled_flights+1))
  Button(screen,text="cancel booking",command=cancel).grid(row=1,column=0,pady=10,padx=10,sticky=W)

def flight_info():
  global screen3
  flight = StringVar()
  screen = Toplevel(screen3)
  screen.title("flight Info")
  screen.geometry("300x250")
  screen.config(bg="white")
  Label(screen,text="Flight ID: ",bg="white").grid(row=0,column=0,sticky=W,padx=10)
  fi = Entry(screen, textvariable=flight)
  fi.grid(row=0,column=1)
  def flight_details():
    with open('passengers/'+flight.get()+'.txt','r') as file:
        y_axis = 100
        for x in file:
            Label(screen,text=x, bg="white").place(x=10,y=y_axis)
            y_axis+=30
  Button(screen,text="Get details",bg="purple",width=10,fg="white",relief="flat",command=flight_details).grid(row=1,column=0,pady=10,padx=10,sticky=W)

def book_flight():
  global screen3
  flight = StringVar()
  ticket_price = StringVar()
  travel_date = StringVar()
  name = StringVar()
  screen = Toplevel(screen3)
  screen.title("Book flight")
  screen.geometry("300x250")
  Label(screen,text="Select Flight").pack()
  select = ttk.Combobox(screen, width = 27, textvariable = flight)
  select["values"] = ('PIA','Emirates','Blue sea')
  select.pack()
  Label(screen,text="Select Passenger name").pack()
  pn = Entry(screen,textvariable=name)
  pn.pack()
  Label(screen,text="Select Travel date").pack()
  td = Entry(screen,textvariable=travel_date)
  td.pack()
  Label(screen,text="Ticket price").pack()
  tp = Entry(screen,textvariable=ticket_price)
  tp.pack()
  def book():
      global total_bookings
      global total_amount
      id = random.randint(0,100000)
      with open('passengers/'+str(id)+'.txt',"w") as file:
          file.write("ID: "+str(id)+'\n')
          file.write("Name: "+name.get()+'\n')
          file.write("Airline: "+flight.get()+'\n')
          file.write("Travel date: "+travel_date.get()+'\n')
          file.write("Cost: "+ticket_price.get()+'$')
          messagebox.showinfo("","Successful")
          
      with open("info/passengerslist.log","a") as file:
        file.write(name.get() + "\t:\t" + str(id) + '\n')

      with open("info/bookings.log","r") as file:
        total_bookings = int(file.readline())
      with open("info/bookings.log","w") as file:
        file.write(str(total_bookings+1))

      with open("info/amount.log","r") as file:
        total_amount = int(file.readline())
      with open("info/amount.log","w") as file:
        file.write(str(total_amount+int(ticket_price.get())))
      pn.delete(0,END)
      td.delete(0,END)
      tp.delete(0,END)

  Button(screen,text="Book",command=book).pack()

def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  screen1.config(bg="white")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "" ,bg="white").pack()
  Label(screen1, text = "" ,bg="white").pack()
  Label(screen1, text = "Username * ",bg="white").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ",bg="white").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "",bg="white").pack()
  Button(screen1, text = "Register", width = 10, relief="flat", bg="#00d9ec", fg="white",font=("poppins",10),padx=20,height = 1, command = register_user).pack()

def register_user():

  username_info = username.get()
  password_info = password.get()

  file=open(username_info+".txt", "w")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11), bg="white").pack()

def login_user():

  username_info = username.get()
  password_info = password.get()

  with open(username_info+".txt", "r") as file:
      if password_info == file.readline():
          airline()
      else:
          Label(screen2,text="", bg="white").pack()
          # Label(screen2,text="Invalid password",fg="red", bg="white").pack()
          messagebox.showinfo("","Password invalid")

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.config(bg="white")
  screen2.title("Login")
  screen2.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen2, text = "",bg="white").pack()
  Label(screen2, text = "",bg="white").pack()
  Label(screen2, text = "Username * ",bg="white").pack()
  username_entry = Entry(screen2, textvariable = username)
  username_entry.pack()
  Label(screen2, text = "Password * ",bg="white").pack()
  password_entry =  Entry(screen2, textvariable = password)
  password_entry.pack()
  Label(screen2, text = "",bg="white").pack()
  Button(screen2, text = "Login", width = 10, height = 1, relief="flat", bg="#00d9ec", fg="white",font=("poppins",10),padx=20,command = login_user).pack()

def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x350")
  screen.config(bg="white")
  screen.title("Airline reservation sys")
  logo = Image.open("logo.png")
  img = ImageTk.PhotoImage(logo)
  # Label(text = "Airline reservation sys", bg = "black", fg="white", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "", bg="white").pack()
  Label(image=img, bg="white").pack()
  Label(text = "", bg="white").pack()
  Label(text = "", bg="white").pack()
  Button(text = "Login", height = 1, width = 25, command = login, bg="darkgreen",relief="flat", fg="white", font=('Poppins',10)).pack(pady=0)
  Label(text = "", bg="white").pack()
  Button(text = "Register", height = 1, width = 25, command = register, bg="red", relief="flat",fg="white", font=('Poppins',10)).pack(pady=0)
  screen.mainloop()

main_screen()
  
