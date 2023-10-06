from tkinter import *
from PIL import Image, ImageTk
from KhachHang import KhachHang
from Phong import Phong

class QuanLyKhachSan(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Hệ thống quản lý khách sạn")
        self.geometry("1280x720+120+0")
        self.resizable(False,False)

        imgbanner = Image.open(r"imglable.png")
        self.imgbanner=ImageTk.PhotoImage(imgbanner)
        imglogo = Image.open(r"DLULogo.png")
        self.imglogo = ImageTk.PhotoImage(imglogo)

        imgbanner_lb = Label(self, image=self.imgbanner,background="#b0d46c").place(x=0,y=0,width=1280,height=119)
        imglogo_lb = Label(self, image=self.imglogo, bd=0,background="#b0d46c").place(x=0,y=0,width=115,height=115)
        title_lb = Label(self, text="HỆ THỐNG QUẢN LÝ KHÁCH SẠN",font=('Arial',25, 'bold'),fg='white',bg='#b0d46c',anchor='center').place(relx=0,y=119,width=1280,height=50)
        
        mainFrame = Frame(self,bd=4,relief=RIDGE).place(x=0,y=220,width=1280,height=500)
        buttonFrame = Frame(self,bd=4,relief=RIDGE).place(x=0,y=170,width=1280,height=50)

        khachhang_btn = Button(buttonFrame,text="Khách Hàng", width=300,bg='#b0d46c',fg='white',bd=0,cursor='hand2',command=self.showCusInfo).place(x=20,y=180,width=300,height=25)
        phong_btn = Button(buttonFrame,text="Phòng", width=300,bg='#b0d46c',fg='white',bd=0,cursor='hand2',command=self.showRoomInfo).place(x=490,y=180,width=300,height=25)
        dangxuat_btn = Button(buttonFrame,text="Đăng xuất", width=300,bg='#b0d46c',fg='white',bd=0,cursor='hand2',command=self.closeForm).place(x=960,y=180,width=300,height=25)

    def showCusInfo(self):
        self.newForm = Toplevel(self)
        self.app = KhachHang(self.newForm)
    
    def showRoomInfo(self):
        self.newForm = Toplevel(self)
        self.app = Phong(self.newForm)

    def closeForm(self):
        self.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = QuanLyKhachSan(root)
    root.mainloop()