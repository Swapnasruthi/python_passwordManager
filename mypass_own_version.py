#this program stores the passwords of different websites with emails

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
window=Tk()
window.title("login page")
window.config(padx=100,pady=50)
window.minsize(width=500,height=300)

#creating a password"
def generating_password():
    letters=['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r',
         's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K'
         ,'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers=['1','2','3','4','5','7','8','9']
    symbols=['@','!','$','%','^','&','*']

    random_letters=random.randint(6,8)
    random_numbers=random.randint(2,4)
    random_symbols=random.randint(2,4)

    password_list=[]
    for i in range(random_letters):
        password_list.append(random.choice(letters))

    for i in range(random_numbers):
        password_list.append(random.choice(numbers))

    for i in range(random_symbols):
        password_list+=random.choice(symbols)

    random.shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



#adding passwords to txt file:
def button_clicked():

    entered_password=password_entry.get()
    entered_email=email_entry.get()
    entered_website=website_entry.get()
    if len(entered_website)==0 or len(entered_password)==0:
        empty=messagebox.showinfo(title="Oops",message="please enter valid website/password")
    else:
        is_ok=messagebox.askokcancel(title="title",message=f"These are the details entered: \nEmail: "
                                                    f"{entered_email} \nPassword: {entered_password} \n"
                                                    f"Is it ok to save?")
        if is_ok:
            with open("password_file.txt","a") as file:
                file.write(f"\n{entered_website} | {entered_email} | {entered_password}")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

            successfull_label.config(text="DONE!")


#page design
login_label=Label(text="MY PASS",font=("Times New Roman",25,"bold"), fg="red")
login_label.grid(row=0,column=1)
login_label.config(pady=30)


website_label=Label(text="Website",font=("Times New Roman",10,"normal"))
website_label.grid(row=1,column=0)

website_entry=Entry(width=45)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()


email_label=Label(text="Email",font=("Times New Roman",10,"normal"))
email_label.grid(row=2,column=0)

email_entry=Entry(width=45)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"swapnasruthi2005@gmail.com")
# email_entry.focus()

password_label=Label(text="Password",font=("Times New Roman",10,"normal"))
password_label.grid(row=3,column=0)

password_entry=Entry(width=25)
password_entry.grid(row=3,column=1)

generate_password=Button(text="Generate Password",width=16,command=generating_password)
generate_password.grid(row=3,column=2)

submit_button=Button(text="Add",command=button_clicked,width=40)
submit_button.grid(row=4,column=1,columnspan=2)



successfull_label=Label(text="",font=("Time New Roman",13,"bold"),fg="green")
successfull_label.grid(row=6,column=1)

window.mainloop()