from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from QLKS import *

class LoginForm(Toplevel):
    def __init__(self,root):
        Toplevel.__init__(self, root)
        self.parent = root
        self.title("Đăng nhập")
        self.geometry("900x400+300+200")
        self.config(bg="#fff")
        self.resizable(False,False)

        self.var_user=StringVar()
        self.var_pwd=StringVar()

        imglogin = Image.open(r"login.png")
        self.imglogin = ImageTk.PhotoImage(imglogin)
        imglogin_lb = Label(self, image=self.imglogin).place(x=50,y=50)

        mainFrame = Frame(self,width=350,height=350,bg="white")
        mainFrame.place(x=480,y=70)

        title_lb = Label(mainFrame,text="Đăng nhập",fg="#b0d46c",bg="white",font=('bold',20)).place(x=100,y=0 )

        def onEnterUser(e):
            user_entry.delete(0,'end')
        
        def onLeaveUser(e):
            name = user_entry.get()
            if name =='':
                user_entry.insert(0,'Tên đăng nhập')

        user_entry = Entry(mainFrame,fg='black',border=0,bg="white",width=25,textvariable=self.var_user)
        user_entry.place(x=30,y=80)
        user_entry.insert(0,"Tên đăng nhập")
        user_entry.bind('<FocusIn>',onEnterUser)
        user_entry.bind('<FocusOut>',onLeaveUser)

        line_fr = Frame(mainFrame,width=295,height=2,bg="black").place(x=25,y=105)

        def onEnterPwd(e):
            password_entry.delete(0,'end')
        
        def onLeavePwd(e):
            pwd = password_entry.get()
            if pwd =='':
                password_entry.insert(0,'Mật khẩu')

        password_entry = Entry(mainFrame,fg='black',border=0,bg="white",width=25,textvariable=self.var_pwd,show="*")
        password_entry.place(x=30,y=150)
        password_entry.insert(0,"Mật khẩu")
        password_entry.bind('<FocusIn>',onEnterPwd)
        password_entry.bind('<FocusOut>',onLeavePwd)

        line_fr = Frame(mainFrame,width=295,height=2,bg="black").place(x=25,y=175)

        btn_dn = Button(mainFrame,width=39,pady=7,text="Đăng nhập",bg="#b0d46c",cursor='hand2',command=self.login).place(x=35,y=204)
        lb1 = Label(mainFrame,text="Bạn không có tài khoản?",fg="black",bg='white')
        lb1.place(x=105,y=270)
    def login(self):
        if self.var_user.get()=="" or self.var_pwd.get()=="":
            messagebox.showerror("Error","Phải điền đủ thông tin")
        elif self.var_user.get()=="truong" or self.var_pwd.get()=="hello":
            messagebox.showinfo("Success","Đăng nhập thành công")
            self.switchForm()
        else:
            messagebox.showerror("Error","Đăng nhập thất bại")

    def switchForm(self):
        self.destroy()
        self.parent.deiconify()

if __name__ == "__main__":
    qlks = QuanLyKhachSan()
    qlks.withdraw()

    obj = LoginForm(qlks)
    qlks.mainloop() 
     