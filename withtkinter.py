from tkinter import *
from tkinter import messagebox
from Models import main1

database = {'admin':'1234'}
EMAIL = None
PASSWORD = None
AGE = None
root = Tk()
root.title('Smart Login System')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def signupcheck():
    if AGE >= 18:
        database[EMAIL] = PASSWORD
        signin()
    
    else:
        messagebox.showerror('Restricted','This Application is not for Minors')
    print(database)
    
def signin():
    username = user.get()
    password = code.get()
    if username in database.keys() and database[username] == password:
        age , gender = main1.predict()
        if age == None:
            messagebox.showerror("Invalid", "       Face not Detected!\nPlease place the camera properly...")
            
        elif age>= 18:
            screen = Toplevel(root)
            screen.title('Application')
            screen.geometry('925x500+300+200')
            screen.config(bg='white')
            Label(screen,text='Hello Everyone!',bg='#fff',font=('Bell Gothic Std Light',26,'bold')).pack(expand=True)
            screen.mainloop()
            
        else:
            messagebox.showerror('Restricted','This Application is not for Minor')

    elif username not in database.keys() and password not in database.values():
        messagebox.showerror("Invalid", "Invalid Username or Password")
        
    elif username not in database.keys():
        messagebox.showerror('Invalid','Invalid username')
    
    else:
        messagebox.showerror('Invalid',"Invalid password")

def signup():
    age,gender = main1.predict()
    global AGE
    global PASSWORD
    global EMAIL
    AGE=age
    
    if AGE == None:
        messagebox.showerror("Invalid", "       Face not Detected!\nPlease place the camera properly...")
        return
        
    screen = Toplevel(root)
    screen.title('Application')
    screen.geometry('925x500+300+200')
    heading = Label(screen,text='Sign up',fg='#57a1f8',bg='white',font=('Bell Gothic Std Light',23,'bold'))
    heading.place(x=400,y=5)
    ############         Name    ####################################
    def on_enter(e):
        name.delete(0,'end')
        
    def on_leave(e):
        name1 = name.get()
        if name1 == '':
            name.insert(0,'Name')
            
    name = Entry(screen,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12))
    name.place(x=90,y=80)
    name.insert(0,'Name')
    name.bind('<FocusIn>',on_enter)
    name.bind('<FocusOut>',on_leave)
    Frame(screen,width=295,height=2,bg='black').place(x=85,y=107)
    ####################     Surname      ############################
    def on_enter(e):
        surname.delete(0,'end')
        
    def on_leave(e):
        surname1 = surname.get()
        if surname1 == '':
            surname.insert(0,'Surname')
            
    surname = Entry(screen,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12))
    surname.place(x=520,y=80)
    surname.insert(0,'Surname')
    surname.bind('<FocusIn>',on_enter)
    surname.bind('<FocusOut>',on_leave)
    Frame(screen,width=295,height=2,bg='black').place(x=515,y=107)
    ##################     Mobile No.    ##############################
    def on_enter(e):
        mobile.delete(0,'end')
        
    def on_leave(e):
        No = mobile.get()
        if No == '':
            mobile.insert(0,'Mobile No.')
            
    mobile = Entry(screen,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12))
    mobile.place(x=90,y=150)
    mobile.insert(0,'Mobile No.')
    mobile.bind('<FocusIn>',on_enter)
    mobile.bind('<FocusOut>',on_leave)
    Frame(screen,width=295,height=2,bg='black').place(x=85,y=177)   
    ###################     Address     #############################
    def on_enter(e):
        address.delete(0,'end')
        
    def on_leave(e):
        add = address.get()
        if add == '':
            address.insert(0,'Address')
            
    address = Entry(screen,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12))
    address.place(x=520,y=150)
    address.insert(0,'Address')
    address.bind('<FocusIn>',on_enter)
    address.bind('<FocusOut>',on_leave)
    Frame(screen,width=295,height=2,bg='black').place(x=515,y=177)   
    ##################      Email      ##############################
    def on_enter(e):
        Email.delete(0,'end')
        
    def on_leave(e):
        global EMAIL  
        mail = Email.get()
        EMAIL = mail
        if mail == '':
            Email.insert(0,'Email')
            
    Email = Entry(screen,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12))
    Email.place(x=90,y=220)
    Email.insert(0,'Email')
    Email.bind('<FocusIn>',on_enter)
    Email.bind('<FocusOut>',on_leave)
    Frame(screen,width=295,height=2,bg='black').place(x=85,y=247)
    ###################       Password     #############################
    def on_enter(e):
        password.delete(0,'end')
        
    def on_leave(e):
        global PASSWORD   
        passw = password.get()
        PASSWORD = passw
        if passw == '':
            password.insert(0,'Password')
            
    password = Entry(screen,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12))
    password.place(x=520,y=220)
    password.insert(0,'Password')
    password.bind('<FocusIn>',on_enter)
    password.bind('<FocusOut>',on_leave)
    Frame(screen,width=295,height=2,bg='black').place(x=515,y=247)
    #####################       Age         ###########################
    Label(screen,text=f"Age : {age}",width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12)).place(x=90,y=290)
    Frame(screen,width=295,height=2,bg='black').place(x=85,y=317)
    ######################      Gender       ###########################
    Label(screen,text=f"Gender : {gender}",width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12)).place(x=520,y=290)
    Frame(screen,width=295,height=2,bg='black').place(x=515,y=317)
    
    ######################  Submit   #########################
    Button(screen,width=39,pady=7,text='Submit',bg='#57a1f8',fg='white',border=0,font=('Bell Gothic Std Light',9),command=signupcheck).place(x=330,y=360) 
    print(database)
    screen.mainloop()

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)
label = Label(root,text="Smart Login System",fg='green',bg='white',font=('Bell Gothic Std Light',26,'bold'))
label.place(x=400,y=10)
frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)
################################################
heading = Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Bell Gothic Std Light',23,'bold'))
heading.place(x=100,y=5)

#################################################
def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')
        
user = Entry(frame,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

################################################
def on_enter(e):
    code.delete(0,'end')
    
def on_leave(e):
    password = code.get()
    if password == '':
        code.insert(0,'Password')
        
code = Entry(frame,width=30,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',12))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#################################################
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,font=('Bell Gothic Std Light',9),command=signin).place(x=35,y=204)
label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Bell Gothic Std Light',9,'bold'))
label.place(x=75,y=270)

signup = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',font=('Bell Gothic Std Light',9,'bold'),command=signup)
signup.place(x=210,y=270)
root.mainloop()