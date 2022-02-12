import random,os,re
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar
from datetime import datetime

def datepicker(src):
  def cal():
    def get():
      global CURR_DATE
      CURR_DATE = calender.get_date()
      screen.destroy()
    screen = Toplevel(src)
    screen.config(bg="white")
    now = datetime.now()
    day = int(now.strftime("%d"))
    mon = int(now.strftime("%m"))
    year= int(now.strftime("%Y"))
    calender = Calendar(screen, selectmode = 'day',year = year, month = mon,day = day)
    calender.pack()
    Button(screen,text="Select date", bg="crimson",fg="white",relief="flat",command=get).pack(pady=10,ipadx=5)
  screen = Frame(src)
  screen.config(bg="white")
  Label(screen,text="MM-DD-YYYY:",background="white").grid(row=0,column=0,padx=0)
  Button(screen,text="Pick date",relief="flat",bg="purple",fg="white",command=cal,width=10).grid(row=0,column=1,sticky=E,padx=13)
  return screen

def update_amount(id):
  with open("passengers/"+id+'.txt') as file:
    string = file.read()
    cut = re.search("\d+\$$",string).span()
    amount = string[cut[0]:cut[1]-1]
    with open("info/amount.log",'r') as file:
      global total_amount
      total_amount = file.readline()
    with open("info/amount.log",'w') as file:
      total_amount = int(total_amount) - int(amount)
      TOTAL_AMOUNT.config(text=str(total_amount)+'$')
      file.write(str(total_amount))

def update_passengerlist(id):
  with open("info/passengerslist.log",'r') as file:
    array = []
    for x in file:
      if not x.find(id) > 0:
        array.append(x)
    with open('info/passengerslist.log','w') as file:
        file.writelines(array)

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
    global TOTAL_BOOKING
    global TOTAL_AMOUNT
    global TOTAL_CANCELLED_FLIGHTS

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
    TOTAL_BOOKING = Label(List, text=number_of_bookings, bg="white")
    TOTAL_BOOKING.pack(side=LEFT, anchor=E,expand=True)
    List.pack(padx=25,expand=True,fill=X)

    List2 = Frame(screen,bg="white")
    Label(List2, text="Total Amount", bg="white",font=("poppins",10,"bold")).pack(side=LEFT)
    TOTAL_AMOUNT = Label(List2, text=amount+'$', bg="white")
    TOTAL_AMOUNT.pack(side=LEFT, anchor=E,expand=True)
    List2.pack(padx=25,expand=True,fill=X)

    List3 = Frame(screen,bg="white")
    Label(List3, text="Cancelled Flights", bg="white",font=("poppins",10,"bold")).pack(side=LEFT)
    TOTAL_CANCELLED_FLIGHTS = Label(List3, text=cancelled_flights, bg="white")
    TOTAL_CANCELLED_FLIGHTS.pack(side=LEFT, anchor=E,expand=True)
    List3.pack(padx=25,expand=True,fill=X)

    List4 = Frame(screen,bg="red")
    Button(List4, text="View Passengers List", bg="black",fg="White",relief="flat",font=("poppins",10,"bold"),command=listPassengers).pack(side=LEFT,fill=X,expand=True)
    List4.pack(padx=25,expand=True,fill=X,pady=30)
    return screen

def airline():
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
  screen.config(bg="white")
  Label(screen,text="Flight ID", bg="white").grid(row=0,column=0,sticky=W,padx=10)
  fi = Entry(screen, textvariable=flight)
  fi.grid(row=0,column=1)

  def cancel():
      global cancelled_flights
      Label(screen,text="Flight Cancelled",fg="red",bg="yellow")
      if os.path.isfile("passengers/"+flight.get()+'.txt'):
        with open("info/cancelled flight.log",'r') as file:
          cancelled_flights = int(file.readline())
        with open("info/cancelled flight.log",'w') as file:
          TOTAL_CANCELLED_FLIGHTS.config(text=str(cancelled_flights+1))
          file.write(str(cancelled_flights+1))
        update_passengerlist(flight.get())
        update_amount(flight.get())
        os.remove("passengers/"+flight.get()+'.txt')
        messagebox.showinfo("","Flight cancelled")
      else:
        messagebox.showinfo("","Invalid passenger ID")
  Button(screen,text="cancel booking",relief="flat",bg="#BD2130",fg="white",command=cancel).grid(row=1,column=0,pady=10,padx=10,sticky=W)

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
    if os.path.isfile("passengers/"+flight.get()+'.txt'):
      with open('passengers/'+flight.get()+'.txt','r') as file:
          y_axis = 100
          for x in file:
              Label(screen,text=x, bg="white").place(x=10,y=y_axis)
              y_axis+=30
    else:
      messagebox.showinfo("","Record not found")
  Button(screen,text="Get details",bg="purple",width=10,fg="white",relief="flat",command=flight_details).grid(row=1,column=0,pady=10,padx=10,sticky=W)

def book_flight():
  global screen3
  flight = StringVar()
  ticket_price = StringVar()
  travel_date = StringVar()
  name = StringVar()
  screen = Toplevel(screen3)
  screen.title("Book flight")
  screen.geometry("300x300")
  screen.config(bg="white")

  Label(screen,text="Select Flight",bg="white").pack(padx=55,anchor=W)
  select = ttk.Combobox(screen, width = 27, textvariable = flight)
  select["values"] = ('PIA','Emirates','Blue sea')
  select.pack(pady=10)


  Label(screen,text="Select Passenger name",bg="white").pack(padx=55,anchor=W)
  pn = Entry(screen,textvariable=name,width=30)
  pn.pack(pady=10)
    
  datepicker(screen).pack(pady=10)

  Label(screen,text="Ticket price",bg="white").pack(padx=55,anchor=W)
  tp = Entry(screen,textvariable=ticket_price,width=30)
  tp.pack(pady=10)
  Label(screen,text="",bg="white").pack()
  def book():
      global total_bookings
      global total_amount
      id = random.randint(0,100000)
      with open('passengers/'+str(id)+'.txt',"w") as file:
          file.write("ID: "+str(id)+'\n')
          file.write("Name: "+name.get()+'\n')
          file.write("Airline: "+flight.get()+'\n')
          file.write("Travel date: "+CURR_DATE+'\n')
          file.write("Cost: "+ticket_price.get()+'$')
          messagebox.showinfo("","Successful")
          
      with open("info/passengerslist.log","a") as file:
        file.write(name.get() + "\t:\t" + str(id) + '\n')

      with open("info/bookings.log","r") as file:
        total_bookings = int(file.readline())
      with open("info/bookings.log","w") as file:
        TOTAL_BOOKING.config(text=str(total_bookings+1))
        file.write(str(total_bookings+1))

      with open("info/amount.log","r") as file:
        total_amount = int(file.readline())
      with open("info/amount.log","w") as file:
        TOTAL_AMOUNT.config(text=str(total_amount+int(ticket_price.get()))+'$')
        file.write(str(total_amount+int(ticket_price.get())))
      pn.delete(0,END)
      # td.delete(0,END)
      tp.delete(0,END)
  Button(screen,text="Book",command=book,relief="flat",background="#00d9ec",width=25,fg="white").pack()

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

  if(os.path.isfile(username_info+".txt")):
    with open(username_info+".txt", "r") as file:
        if password_info == file.readline():
            airline()
        else:
            Label(screen2,text="", bg="white").pack()
            messagebox.showinfo("","Password invalid")
  else:
    messagebox.showinfo("","User invalid")

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