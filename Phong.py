from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from datetime import datetime
import sqlite3
import locale

class Phong:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý phòng")
        self.root.geometry("1280x460+120+255")
        self.root.resizable(False,False)
        
        #variable
        self.var_dtkh=StringVar()
        self.var_den=StringVar()
        self.var_di=StringVar()
        self.var_loaiphong=StringVar()
        self.var_phong=StringVar()
        self.var_ngayo=StringVar()
        self.var_tongbill=StringVar()
        #Title
        title_lb = Label(self.root, text="HỆ THỐNG QUẢN LÝ PHÒNG",font=('Arial',15, 'bold'),fg='white',bg='#b0d46c',anchor='center').place(relx=0,y=0,width=1280,height=50)
        #LableFrame
        lableframeLeft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Thông tin phòng",padx=2)
        lableframeLeft.place(x=5,y=50,width=425,height=400)

        #Lable and Entry
        sodt_lb = Label(lableframeLeft,text="Số điện thoại",padx=2,pady=6).grid(row=0,column=0,sticky=W)
        sodt_entry = Entry(lableframeLeft,width=25,textvariable=self.var_dtkh).grid(row=0,column=1,sticky=W)
        btn_xacnhan = Button(lableframeLeft,text="Tìm",bg="#b0d46c",width=10,command=self.selectCus)
        btn_xacnhan.place(x=250, y=4)

        checkin_lb = Label(lableframeLeft,text="Check-in",padx=2,pady=6).grid(row=1,column=0,sticky=W)
        checkin_entry = Entry(lableframeLeft,width=53,textvariable=self.var_den).grid(row=1,column=1)

        checkout_lb = Label(lableframeLeft,text="Check-out",padx=2,pady=6).grid(row=2,column=0,sticky=W)
        checkout_entry = Entry(lableframeLeft,width=53,textvariable=self.var_di).grid(row=2,column=1)

        loaiphong_lb = Label(lableframeLeft,text="Loại phòng",padx=2,pady=6).grid(row=3,column=0,sticky=W)
        loaiphong_cbb = Combobox(lableframeLeft,width=50,textvariable=self.var_loaiphong,state="readonly")
        loaiphong_cbb["values"]=("Đơn","Đôi","VIP","Nhóm đông")
        loaiphong_cbb.current(0)
        loaiphong_cbb.grid(row=3,column=1)

        phong_lb = Label(lableframeLeft,text="Phòng",padx=2,pady=6).grid(row=4,column=0,sticky=W)
        phong_cbb = Combobox(lableframeLeft,width=50,textvariable=self.var_phong,state="readonly")
        phong_cbb["value"]=("101","102","103","201","202","203","301","302","303")
        phong_cbb.current(0)
        phong_cbb.grid(row=4,column=1)

        songay_lb = Label(lableframeLeft,text="Số ngày ở",padx=2,pady=6).grid(row=5,column=0,sticky=W)
        songay_entry = Entry(lableframeLeft,width=53,textvariable=self.var_ngayo).grid(row=5,column=1)

        tong_lb = Label(lableframeLeft,text="Tổng tiền",padx=2,pady=6).grid(row=6,column=0,sticky=W)
        tong_entry = Entry(lableframeLeft,width=53,textvariable=self.var_tongbill).grid(row=6,column=1)

        bill_timKiem = Button(lableframeLeft, text="In hoá đơn",bg="#b0d46c",width=10,command=self.bill)
        bill_timKiem.grid(row=7,column=0)

        #button
        buttonFrame = Frame(lableframeLeft,bd=2,relief=RIDGE)
        buttonFrame.place(x=0,y=250,width=415,height=125)

        btn_them = Button(buttonFrame, text="Thêm",bg="#b0d46c",width=20,command=self.addData)
        btn_them.grid(row=0,column=0,padx=30,pady=20)

        btn_luu = Button(buttonFrame, text="Lưu",bg="#b0d46c",width=20,command=self.updateData)
        btn_luu.grid(row=1,column=0,padx=30,pady=20)

        btn_xoa = Button(buttonFrame, text="Xoá",bg="#b0d46c",width=20,command=self.deleteData)
        btn_xoa.grid(row=0,column=1,padx=30,pady=20)

        btn_reset = Button(buttonFrame, text="F5",bg="#b0d46c",width=20,command=self.reset)
        btn_reset.grid(row=1,column=1,padx=30,pady=20)

        #tableframe
        tableFrame = LabelFrame(self.root,bd=2,relief=RIDGE,text="Bảng thông tin",padx=2)
        tableFrame.place(x=435,y=200,width=840,height=250)

        timKiem_lb = Label(tableFrame,text="Tìm kiếm theo: ",padx=2,pady=6).grid(row=0,column=0,sticky=W)

        self.search_var = StringVar()
        timKiem_cbb = Combobox(tableFrame,width=20,state="readonly",textvariable=self.search_var)
        timKiem_cbb["value"]=("LienLac","phong")
        timKiem_cbb.current(0)
        timKiem_cbb.grid(row=0,column=1)
        self.search_txt = StringVar()
        timKiem_entry = Entry(tableFrame,width=53,textvariable=self.search_txt).grid(row=0,column=2,padx=3)

        btn_timKiem = Button(tableFrame, text="Tìm",bg="#b0d46c",width=10,command=self.search)
        btn_timKiem.grid(row=0,column=3,padx=10,pady=20)
        btn_resetTK = Button(tableFrame, text="F5",bg="#b0d46c",width=10,command=self.showData)
        btn_resetTK.grid(row=0,column=4,padx=10,pady=20)
        
        #dataTable
        dataTableFrame = Frame(tableFrame,bd=2,relief=RIDGE)
        dataTableFrame.place(x=0,y=70,width=830,height=150) 

        scrollx = Scrollbar(dataTableFrame,orient=HORIZONTAL)
        scrolly = Scrollbar(dataTableFrame,orient=VERTICAL)

        self.BangPhong=Treeview(dataTableFrame,columns=("dtkh","den","di","loaiphong","tinhtrang","ngayo","tongbill"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.BangPhong.xview)
        scrolly.config(command=self.BangPhong.yview)

        self.BangPhong.heading("dtkh",text="Liên lạc")
        self.BangPhong.heading("den",text="Check-in")
        self.BangPhong.heading("di",text="Check-out")
        self.BangPhong.heading("loaiphong",text="Loại phòng")
        self.BangPhong.heading("tinhtrang",text="Phòng")
        self.BangPhong.heading("ngayo",text="Ngày ở")

        self.BangPhong["show"]="headings"
        self.BangPhong.pack(fill=BOTH,expand=1)
        self.BangPhong.bind("<ButtonRelease-1>",self.getData)
        self.showData()

    def selectCus(self):
        if self.var_dtkh.get()=="":
            messagebox.showerror("Error","Nhập số điện thoại khách hàng!",parent=self.root)
        else:
            conn=sqlite3.connect("QLKS.db", timeout=20)
            myCursor = conn.cursor()
            p = (
                self.var_dtkh.get(),
                )
            check_data = "SELECT hoten FROM KhachHang WHERE sodt = ?" 
            myCursor.execute(check_data,p)
            fetch = myCursor.fetchone()
            if fetch ==None:
                messagebox.showerror("Error","Không tìm thấy số điện thoại này", parent = self.root)
            else:
                conn.commit()
                conn.close()

                thongTinFrame=Frame(self.root,bd=2,relief=RIDGE,padx=2)
                thongTinFrame.place(x=435,y=50,width=840,height=150)

                ten_lb = Label(thongTinFrame,text="Tên:",pady=20).place(x=0,y=0)
                lbl_rong = Label(thongTinFrame,text=fetch,pady=20).place(x=50,y=0)

                conn=sqlite3.connect("QLKS.db", timeout=20)
                myCursor = conn.cursor()
                p = (
                    self.var_dtkh.get(),
                    )
                check_data = "SELECT gioitinh FROM KhachHang WHERE sodt = ?" 
                myCursor.execute(check_data,p)
                fetch = myCursor.fetchone()
                gioitinh_lb = Label(thongTinFrame,text="Giới tính:",pady=20).place(x=300,y=0)
                lbl_rong1 = Label(thongTinFrame,text=fetch,pady=20).place(x=400,y=0)

                conn=sqlite3.connect("QLKS.db", timeout=20)
                myCursor = conn.cursor()
                p = (
                    self.var_dtkh.get(),
                    )
                check_data = "SELECT quoctich FROM KhachHang WHERE sodt = ?" 
                myCursor.execute(check_data,p)
                fetch = myCursor.fetchone()
                quoctich_lb = Label(thongTinFrame,text="Quốc tịch:",pady=20).place(x=600,y=0)
                lbl_rong2 = Label(thongTinFrame,text=fetch,pady=20).place(x=700,y=0)

                conn=sqlite3.connect("QLKS.db", timeout=20)
                myCursor = conn.cursor()
                p = (
                    self.var_dtkh.get(),
                    )
                check_data = "SELECT mail FROM KhachHang WHERE sodt = ?" 
                myCursor.execute(check_data,p)
                fetch = myCursor.fetchone()
                email_lb = Label(thongTinFrame,text="Email:",pady=20).place(x=0,y=60)
                lbl_rong3 = Label(thongTinFrame,text=fetch,pady=20).place(x=50,y=60)

                conn=sqlite3.connect("QLKS.db", timeout=20)
                myCursor = conn.cursor()
                p = (
                    self.var_dtkh.get(),
                    )
                check_data = "SELECT id FROM KhachHang WHERE sodt = ?" 
                myCursor.execute(check_data,p)
                fetch = myCursor.fetchone()
                id_lb = Label(thongTinFrame,text="CMND:",pady=20).place(x=300,y=60)
                lbl_rong4 = Label(thongTinFrame,text=fetch,pady=20).place(x=400,y=60)

    def addData(self):
        conn=sqlite3.connect("QLKS.db", timeout=20)
        if self.var_dtkh.get()=="" or self.var_den.get()=="":
            messagebox.showerror("Error","Phải điền đầy đủ thông tin!",parent=self.root)
        else:
            try:
                myCursor = conn.cursor()
                p = (
                    self.var_dtkh.get(),
                self.var_den.get(),
                self.var_di.get(),
                self.var_loaiphong.get(),
                self.var_phong.get(),
                self.var_ngayo.get()
                )
                data_insert = f"""INSERT INTO Phong (LienLac,checkin,checkout,loaiPhong,Phong,ngayo) VALUES (?,?,?,?,?,?)"""
                myCursor.execute(data_insert,p)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Đã thêm thành công phòng!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Có sự cố đã xảy ra {str(es)}",parent=self.root)

    def showData(self):
        conn=sqlite3.connect("QLKS.db", timeout=20) 
        myCursor = conn.execute("""SELECT * FROM Phong""")
        fetch = myCursor.fetchall()
        if len(fetch)!=0:
            self.BangPhong.delete(*self.BangPhong.get_children())
            for i in fetch:
                self.BangPhong.insert('','end',values=(i))
            conn.close()
        conn.close()

    def getData(self,envent=""):
        hang = self.BangPhong.focus()
        content = self.BangPhong.item(hang)
        row = content["values"]

        self.var_dtkh.set(row[0]),
        self.var_den.set(row[1]),
        self.var_di.set(row[2]),
        self.var_loaiphong.set(row[3]),
        self.var_phong.set(row[4]),
        self.var_ngayo.set(row[5])

    def updateData(self):
        conn=sqlite3.connect("QLKS.db", timeout=20)
        myCursor = conn.cursor()
        p = (
                self.var_dtkh.get(),
                self.var_den.get(),
                self.var_di.get(),
                self.var_loaiphong.get(),
                self.var_phong.get(),
                self.var_ngayo.get(),
                self.var_dtkh.get()
                )
        data_update = """UPDATE Phong SET LienLac=?,checkin=?,checkout=?,loaiPhong=?,Phong=?,ngayo=? WHERE LienLac=?"""
        myCursor.execute(data_update,p)
        conn.commit()
        self.getData()
        conn.close()
        messagebox.showinfo("Update","Cap nhat thanh cong!",parent=self.root)

    def deleteData(self):
        tbXoa = messagebox.askyesno("He thong","Ban co muon xoa phong nay",parent=self.root)
        if tbXoa > 0:
            conn=sqlite3.connect("QLKS.db", timeout=20)
            myCursor = conn.cursor()
            p = (
                self.var_dtkh.get()
            )
            data_delete = "DELETE FROM Phong WHERE LienLac=?"
            messagebox.showinfo("Thong bao","Da xoa phong thanh cong")
            myCursor.execute(data_delete,p)
            conn.commit()
            self.getData()
            conn.close()

    def reset(self):
        self.var_dtkh.set(""),
        self.var_den.set(""),
        self.var_di.set(""),
        self.var_loaiphong.set(""),
        self.var_phong.set(""),
        self.var_ngayo.set("")

    def search(self):
        conn=sqlite3.connect("QLKS.db", timeout=20)
        myCursor = conn.cursor()
        query = "SELECT * FROM Phong WHERE "+str(self.search_var.get())+" LIKE '%"+str(self.search_txt.get())+"%'"
        print(query)
        myCursor.execute(query)
        fetch = myCursor.fetchall()
        if len(fetch) !=0:
            self.BangPhong.delete(*self.BangPhong.get_children())
            for i in fetch:
                self.BangPhong.insert("",'end',values=(i))
            conn.commit()
        conn.close()
    
    def bill(self):
        inDate = self.var_den.get()
        outDate = self.var_di.get()
        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_ngayo.set(abs(outDate-inDate).days)
        if self.var_loaiphong.get()=="VIP":
            n = int(self.var_ngayo.get())
            total =(n * int(1000000))
            self.var_tongbill.set("{:,.2f}".format(total) +" VND")
        elif self.var_loaiphong.get()=="Đơn":
            n = int(self.var_ngayo.get())
            total =(n * int(100000))
            self.var_tongbill.set("{:,.2f}".format(total) +" VND")
        elif self.var_loaiphong.get()=="Đôi":
            n = int(self.var_ngayo.get())
            total =(n * int(300000))
            self.var_tongbill.set("{:,.2f}".format(total) +" VND")
        else:
            n = int(self.var_ngayo.get())
            total =(n * int(1000000))
            self.var_tongbill.set("{:,.2f}".format(total) +" VND")
if __name__ == "__main__":
    root = Tk()
    obj = Phong(root)
    root.mainloop() 