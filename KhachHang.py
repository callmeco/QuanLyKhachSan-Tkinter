from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import sqlite3

class KhachHang:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý khách hàng")
        self.root.geometry("1280x460+120+255")
        self.root.resizable(False,False)
    
        #variable
        self.var_ms=StringVar()
        self.var_hoten=StringVar()
        self.var_email=StringVar()
        self.var_gioitinh=StringVar()
        self.var_sdt=StringVar()
        self.var_id=StringVar()
        self.var_quoctich=StringVar()

        #Title
        title_lb = Label(self.root, text="HỆ THỐNG QUẢN LÝ KHÁCH HÀNG",font=('Arial',15, 'bold'),fg='white',bg='#b0d46c',anchor='center').place(relx=0,y=0,width=1280,height=50)
        #LableFrame
        lableframeLeft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Thông tin khách hàng",padx=2)
        lableframeLeft.place(x=5,y=50,width=425,height=400)
        #Lable and Entry
        msKH_lb = Label(lableframeLeft,text="Mã số",padx=2,pady=6).grid(row=0,column=0,sticky=W)
        msKH_entry = Entry(lableframeLeft,width=53,textvariable=self.var_ms).grid(row=0,column=1)

        hotenKH_lb = Label(lableframeLeft,text="Họ và tên",padx=2,pady=6).grid(row=1,column=0,sticky=W)
        hotenKH_entry = Entry(lableframeLeft,width=53,textvariable=self.var_hoten).grid(row=1,column=1)

        emailKH_lb = Label(lableframeLeft,text="Email",padx=2,pady=6).grid(row=2,column=0,sticky=W)
        emailKH_entry = Entry(lableframeLeft,width=53,textvariable=self.var_email).grid(row=2,column=1)

        gtinhKH_lb = Label(lableframeLeft,text="Giới tính",padx=2,pady=6).grid(row=3,column=0,sticky=W)
        gtinhKH_cbb = Combobox(lableframeLeft,width=50,textvariable=self.var_gioitinh,state="readonly")
        gtinhKH_cbb["value"]=("Nam","Nữ","Khác")
        gtinhKH_cbb.current(0)
        gtinhKH_cbb.grid(row=3,column=1)

        sdtKH_lb = Label(lableframeLeft,text="Số điện thoại",padx=2,pady=6).grid(row=4,column=0,sticky=W)
        sdtKH_entry = Entry(lableframeLeft,width=53,textvariable=self.var_sdt).grid(row=4,column=1)

        idKH_lb = Label(lableframeLeft,text="CMND/CCCD",padx=2,pady=6).grid(row=5,column=0,sticky=W)
        idKH_entry = Entry(lableframeLeft,width=53,textvariable=self.var_id).grid(row=5,column=1)

        qtichKH_lb = Label(lableframeLeft,text="Quốc tịch",padx=2,pady=6).grid(row=6,column=0,sticky=W)
        qtichKH_entry = Entry(lableframeLeft,width=53,textvariable=self.var_quoctich).grid(row=6,column=1)
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
        tableFrame.place(x=435,y=50,width=840,height=400)

        timKiem_lb = Label(tableFrame,text="Tìm kiếm theo: ",padx=2,pady=6).grid(row=0,column=0,sticky=W)

        self.search_var = StringVar()
        timKiem_cbb = Combobox(tableFrame,width=20,state="readonly",textvariable=self.search_var)
        timKiem_cbb["value"]=("hoten","id","sodt")
        timKiem_cbb.current(0)
        timKiem_cbb.grid(row=0,column=1)
        self.search_txt = StringVar()
        timKiem_entry = Entry(tableFrame,width=53,textvariable=self.search_txt).grid(row=0,column=2,padx=3)

        btn_timKiem = Button(tableFrame, text="Tìm",bg="#b0d46c",width=10,command=self.search)
        btn_timKiem.grid(row=0,column=3,padx=10,pady=20)
        btn_resetTK = Button(tableFrame, text="F5",bg="#b0d46c",width=10,command=self.showDataInfo)
        btn_resetTK.grid(row=0,column=4,padx=10,pady=20)
        
        #dataTable
        dataTableFrame = Frame(tableFrame,bd=2,relief=RIDGE)
        dataTableFrame.place(x=0,y=70,width=830,height=305) 

        scrollx = Scrollbar(dataTableFrame,orient=HORIZONTAL)
        scrolly = Scrollbar(dataTableFrame,orient=VERTICAL)

        self.BangKhachHang=Treeview(dataTableFrame,columns=("maso","hoten","mail","gioitinh","sodt","id","quoctich"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.BangKhachHang.xview)
        scrolly.config(command=self.BangKhachHang.yview)

        self.BangKhachHang.heading("maso",text="Mã Số")
        self.BangKhachHang.heading("hoten",text="Họ Và Tên")
        self.BangKhachHang.heading("mail",text="Email")
        self.BangKhachHang.heading("gioitinh",text="Giới Tính")
        self.BangKhachHang.heading("sodt",text="Số Điện Thoại")
        self.BangKhachHang.heading("id",text="CMND/CCCD")
        self.BangKhachHang.heading("quoctich",text="Quốc Tịch")

        self.BangKhachHang["show"]="headings"
        self.BangKhachHang.pack(fill=BOTH,expand=1)
        self.BangKhachHang.bind("<ButtonRelease-1>",self.getData)
        self.showDataInfo()

    def addData(self):
        conn=sqlite3.connect("QLKS.db", timeout=20)
        if (self.var_hoten.get()=="" or self.var_email.get()=="") and (self.var_sdt.get()=="" or self.var_quoctich.get()=="" ):
            messagebox.showerror("Error","Phải điền đầy đủ thông tin!",parent=self.root)
        else:
            try:
                myCursor = conn.cursor()
                kh = (
                    self.var_ms.get(),
                self.var_hoten.get(),
                self.var_email.get(),
                self.var_gioitinh.get(),
                self.var_sdt.get(),
                self.var_id.get(),
                self.var_quoctich.get()
                )
                data_insert = f"""INSERT INTO KhachHang (maso,hoten,mail,gioitinh,sodt,id,quoctich) VALUES (?,?,?,?,?,?,?)"""
                myCursor.execute(data_insert,kh)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Đã thêm thành công khách hàng!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Có sự cố đã xảy ra {str(es)}",parent=self.root)

    def showDataInfo(self):
        conn=sqlite3.connect("QLKS.db", timeout=20) 
        myCursor = conn.execute("""SELECT * FROM KhachHang""")
        fetch = myCursor.fetchall()
        if len(fetch)!=0:
            self.BangKhachHang.delete(*self.BangKhachHang.get_children())
            for i in fetch:
                self.BangKhachHang.insert('','end',values=(i))
            conn.close()
        conn.close()
    def updateData(self):
        conn=sqlite3.connect("QLKS.db", timeout=20)
        myCursor = conn.cursor()
        kh = (
                self.var_ms.get(),
                self.var_hoten.get(),
                self.var_email.get(),
                self.var_gioitinh.get(),
                self.var_sdt.get(),
                self.var_id.get(),
                self.var_quoctich.get(),
                self.var_ms.get()
                )
        data_update = """UPDATE KhachHang SET maso=?,hoten=?,mail=?,gioitinh=?,sodt=?,id=?,quoctich=? WHERE maso=?"""
        myCursor.execute(data_update,kh)
        conn.commit()
        self.getData()
        conn.close()
        messagebox.showinfo("Update","Cap nhat thanh cong!",parent=self.root)

    def deleteData(self):
        tbXoa = messagebox.askyesno("He thong","Ban co muon xoa khach hang nay",parent=self.root)
        if tbXoa > 0:
            conn=sqlite3.connect("QLKS.db", timeout=20)
            myCursor = conn.cursor()
            kh = (
                self.var_ms.get()
            )
            data_delete = "DELETE FROM KhachHang WHERE maso=?"
            messagebox.showinfo("Thong bao","Da xoa khach hang thanh cong")
            myCursor.execute(data_delete,kh)
            conn.commit()
            self.getData()
            conn.close()

    def reset(self):
        self.var_ms.set(""),
        self.var_hoten.set(""),
        self.var_email.set(""),
        self.var_sdt.set(""),
        self.var_id.set(""),
        self.var_quoctich.set("")        

    def getData(self,envent=""):
        hang = self.BangKhachHang.focus()
        content = self.BangKhachHang.item(hang)
        row = content["values"]

        self.var_ms.set(row[0]),
        self.var_hoten.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gioitinh.set(row[3]),
        self.var_sdt.set(row[4]),
        self.var_id.set(row[5]),
        self.var_quoctich.set(row[6])

    def search(self):
        conn=sqlite3.connect("QLKS.db", timeout=20)
        myCursor = conn.cursor()
        query = "SELECT * FROM KhachHang WHERE "+str(self.search_var.get())+" LIKE '%"+str(self.search_txt.get())+"%'"
        print(query)
        myCursor.execute(query)
        fetch = myCursor.fetchall()
        if len(fetch) !=0:
            self.BangKhachHang.delete(*self.BangKhachHang.get_children())
            for i in fetch:
                self.BangKhachHang.insert("",'end',values=(i))
            conn.commit()
        conn.close()
        
if __name__ == "__main__":
    root = Tk()
    obj = KhachHang(root)
    root.mainloop() 