#-------------STUDENT DATABASE MANAGEMENT-----------------------------
#------------------MADE BY ANAND-------------------------------------------

#-------------------Importing all Required libraries-------------------------------
import mysql.connector as m
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("SARASWATI HINDI HIGH SCHOOL")
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root,text="STUDENT DATABASE",bd=10,relief=RIDGE,
                    font=("times new roman",35,'bold'),bg='snow2',fg='red3')
        title.pack(side=TOP,fill='x')
        
#----------------------------------------ALL VARIABLES-------------------------------------
        
        self.student_ID=StringVar()
        self.name=StringVar()
        self.class_=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        self.address=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        
        
#-----------------------------------------MANGEMENT FRAME-----------------------------------------------
        
        Frame1=Frame(self.root,bd=4,relief=RIDGE,bg='SteelBlue3')
        Frame1.place(x=20,y=100,width=480,height=580)
        
        f1_title=Label(Frame1,text='Students Information'
                       ,bg='SteelBlue3',fg='white',font=("algerian",25,"bold"))
        f1_title.grid(row=0,columnspan=2,pady=20)
        
        lbl_ID=Label(Frame1,text="Student ID",bd=5,bg='SteelBlue3'
                     ,fg='white',font=("times now roman",15,"bold"))
        lbl_ID.grid(row=1,column=0,pady=10,padx=20,sticky='w')
        
        txt_ID=Entry(Frame1,textvariable=self.student_ID,
                     font=("times now roman",15,"bold"),bd=4,relief=GROOVE)
        txt_ID.grid(row=1,column=1,pady=10,padx=20,sticky='w')
        
        lbl_name=Label(Frame1,text="Name",bd=5,bg='SteelBlue3',
                       fg='white',font=("times now roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')
        
        txt_name=Entry(Frame1,textvariable=self.name,
                       font=("times now roman",15,"bold"),bd=4,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')
        
        lbl_class=Label(Frame1,text="Class",bd=5,bg='SteelBlue3',
                        fg='white',font=("times now roman",15,"bold"))
        lbl_class.grid(row=3,column=0,pady=10,padx=20,sticky='w')
        
        txt_class=Entry(Frame1,textvariable=self.class_,
                        font=("times now roman",15,"bold"),bd=4,relief=GROOVE)
        txt_class.grid(row=3,column=1,pady=10,padx=20,sticky='w')
        
        gender=Label(Frame1,text="Gender",bd=5,bg='SteelBlue3',
                     fg='white',font=("times now roman",15,"bold"))
        gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')
        
        combo_gender=ttk.Combobox(Frame1,textvariable=self.gender,
                                  font=("times now roman",15,"bold"),state='readonly')
        combo_gender['values']=('Male','Female','Others')
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky='w')
        
        lbl_contact=Label(Frame1,text="Contact No.",bd=5,bg='SteelBlue3',
                          fg='white',font=("times now roman",15,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky='w')
        
        txt_contact=Entry(Frame1,textvariable=self.contact,
                          font=("times now roman",15,"bold"),bd=4,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')
        
        lbl_DOB=Label(Frame1,text="D.O.B",bd=5,bg='SteelBlue3',
                      fg='white',font=("times now roman",15,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky='w')
        
        txt_DOB=Entry(Frame1,textvariable=self.dob,
                      font=("times now roman",15,"bold"),bd=4,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky='w')
        
        lbl_address=Label(Frame1,text="Address",bd=5,bg='SteelBlue3',
                          fg='white',font=("times now roman",15,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky='w')
        
        self.txt_address=Text(Frame1,width=30,height=4)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky='w')
        
#-------------------------------BUTTON FRAMES---------------------------------
        
        btn_Frame=Frame(Frame1,bd=4,relief=RIDGE,bg='brown')
        btn_Frame.place(x=15,y=500,width=450)
        
        add_btn=Button(btn_Frame,text='Add',width=11,
                       command=self.add_student).grid(row=0,
                                               column=0,pady=10,padx=10,sticky='w')
        update_btn=Button(btn_Frame,text='Update',width=11,
                          command=self.update_data).grid(row=0,
                                                  column=1,pady=10,padx=10,sticky='w')
        delete_btn=Button(btn_Frame,text='Delete',width=11,
                          command=self.delete_data).grid(row=0,
                                                  column=2,pady=10,padx=10,sticky='w')
        clear_btn=Button(btn_Frame,text='Clear',width=11
                         ,command=self.clear).grid(row=0,
                                            column=4,pady=10,padx=10,sticky='w')
        
#---------------------------------------------DATA FRAME------------------------------------
        
        Data_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='SteelBlue3')
        Data_Frame.place(x=520,y=100,width=800,height=580)
        
        lbl_search=Label(Data_Frame,text="Search By",bd=5,bg='SteelBlue3',fg='white'
                         ,font=("times now roman",15,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky='w')
        
        to_search=ttk.Combobox(Data_Frame,textvariable=self.search_by,width=10
                               ,font=("times now roman",14),state='readonly')
        to_search['values']=('Student_ID','Name','Class')
        to_search.grid(row=0,column=1,pady=10,padx=20,sticky='w')
        
        txt_search=Entry(Data_Frame,textvariable=self.search_txt,width=15
                         ,font=("times now roman",14),bd=2,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')
        
        search_btn=Button(Data_Frame,text='Search',
                          command=self.search_data,width=12).grid(row=0,
                                                           column=3,pady=10,padx=10)
        showall_btn=Button(Data_Frame,text='Show All',width=12,
                           command=self.fetch_data).grid(row=0,column=4,pady=10,padx=10)
        
#--------------------------------INFORMATION FRAME------------------------------------------        
        
        Inf_Frame=Frame(Data_Frame,bd=4,relief=RIDGE,bg='brown')
        Inf_Frame.place(x=10,y=70,width=770,height=500)
        
        scroll_x=Scrollbar(Inf_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Inf_Frame,orient=VERTICAL)
        self.Student_Table=ttk.Treeview(Inf_Frame,
                            columns=('studentID','name','class',
                                     'gender','contact','DOB','address')
                                        ,xscrollcommand=scroll_x.set,
                                        yscrollcommand=scroll_y.set)
        scroll_x.pack(side='bottom',fill='x')
        scroll_y.pack(side='right',fill='y')
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading('studentID',text='Student ID')
        self.Student_Table.heading('name',text='Name')
        self.Student_Table.heading('class',text='Class')
        self.Student_Table.heading('gender',text='Gender')
        self.Student_Table.heading('contact',text='Contact')
        self.Student_Table.heading('DOB',text='D.O.B.')
        self.Student_Table.heading('address',text='Address')
        self.Student_Table['show']='headings'
        
        self.Student_Table.column('studentID',width=100)
        self.Student_Table.column('name',width=125)
        self.Student_Table.column('class',width=125)
        self.Student_Table.column('gender',width=50)
        self.Student_Table.column('contact',width=125)
        self.Student_Table.column('DOB',width=100)
        self.Student_Table.column('address',width=150)
        
        self.Student_Table.pack(fill='both',expand=1)
        
        self.Student_Table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()
        
#---------------------------DATABASE CONNECTION-------------------------------------
        
#-----------------------Adding Students----------------------------------        
    def add_student(self):
        if self.student_ID.get()=="":
            messagebox.showerror("ERROR","Student_ID IS REQUIRED !!!")
        elif self.name.get()=="":
            messagebox.showerror("ERROR","Name IS REQUIRED !!!")
        else:
            mycon=m.connect(host='localhost',user='root',passwd='pa55word',database='CS')
            cur=mycon.cursor()
            cur.execute('INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s)'
                        ,(self.student_ID.get(),
                                                    self.name.get(),
                                                    self.class_.get(),
                                                    self.gender.get(),
                                                    self.contact.get(),
                                                    self.dob.get(),
                                                    self.txt_address.get('1.0',END)
                                                    ))
            mycon.commit()
            self.fetch_data()
            self.clear()
            mycon.close()
            messagebox.showinfo("SUCCESS","RECORD Has Been Inserted")
    
#---------------------------Fetching Data----------------------------------
            
    def fetch_data(self):
        mycon=m.connect(host="localhost",user='root',passwd='pa55word',database='CS')
        cur=mycon.cursor()
        cur.execute('SELECT * FROM STUDENT')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            mycon.commit()
        mycon.close()
        
#----------------------Clearing Data-----------------------------
        
    def clear(self):
        self.student_ID.set("")                                             
        self.name.set("")                                             
        self.class_.set("")                                             
        self.gender.set("")                                             
        self.contact.set("")                                             
        self.dob.set("")                                             
        self.txt_address.delete("1.0",END)                                             

#------------------------Getting data-----------------------------
                                                    
    def get_cursor(self,ev):
        cursor_row=self.Student_Table.focus()
        contents=self.Student_Table.item(cursor_row)
        row=contents['values']
        print(row)
        self.student_ID.set(row[0])
        self.name.set(row[1])                                             
        self.class_.set(row[2])                                             
        self.gender.set(row[3])                                             
        self.contact.set(row[4])                                             
        self.dob.set(row[5])                                             
        self.txt_address.delete("1.0",END)                                             
        self.txt_address.insert(END,row[6])
        
#---------------------Updating Data-----------------------------------        
        
    def update_data(self):
        if self.student_ID.get()=="":
            messagebox.showerror("Error","Select DATA First To UPDATE !!!")
        else:
            mycon=m.connect(host='localhost',user='root',
                            passwd='pa55word',database='CS')
            cur=mycon.cursor()
            cur.execute("""UPDATE STUDENT SET NAME=%s,CLASS=%s,GENDER=%s,
                        CONTACT=%s,DOB=%s,ADDRESS=%s WHERE STUDENT_ID=%s""",
                                                    (self.name.get(),
                                                    self.class_.get(),
                                                    self.gender.get(),
                                                    self.contact.get(),
                                                    self.dob.get(),
                                                    self.txt_address.get('1.0',END),
                                                    self.student_ID.get()
                                                    ))
            mycon.commit()
            self.fetch_data()
            self.clear()
            mycon.close()
            messagebox.showinfo("SUCCESS","DATA Updated Successfully")                                        
            
        
#--------------------------Deleting Data------------------------------------    
    
    def delete_data(self):
        if self.student_ID.get()=="":
            messagebox.showerror("ERROR","Select DATA First To DELETE !!!")
        else:
            mycon=m.connect(host="localhost",user='root',passwd='pa55word',database='CS')
            cur=mycon.cursor()
            msg=messagebox.askquestion ("CONFIRMATION",'Are you confirm to DELETE DATA?',
                                        icon = 'warning')
            if msg=='yes':
                q="DELETE FROM STUDENT WHERE STUDENT_ID=%s"
                cur.execute(q,(self.student_ID.get(),))
                mycon.commit()
                mycon.close()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("SUCCESS","DATA Deleted Successfully !")
                
#---------------------------Searching Data-------------------------------------        
        
    def search_data(self):
        if self.search_txt.get()=="":
            messagebox.showerror("ERROR","Enter Any INFORMATION First !!!")
        else:
        
            mycon=m.connect(host="localhost",user='root',passwd='pa55word',database='CS')
            cur=mycon.cursor()
            
            cur.execute("SELECT * FROM STUDENT where "+str(self.search_by.get())+
                        " LIKE '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)==0:
                messagebox.showerror("ERROR","DATA Not Present !!!")
            elif len(rows)!=0:
                self.Student_Table.delete(*self.Student_Table.get_children())
                for row in rows:
                    self.Student_Table.insert('',END,values=row)
                mycon.commit()
            mycon.close()
           

root=Tk()
ob=Student(root)
root.mainloop()
