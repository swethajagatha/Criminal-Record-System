from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1280x690+0+0')
        self.root.title('CRIMINAL RECORD SYSTEM')

        #variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar() 
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()

        lbl_title=Label(self.root,text="CRIMINAL RECORD SYSTEM SOFTWARE",font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1370,height=60)
         
        #ncr logo
        img_logo=Image.open('images/ncr.jpg')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=40,y=3,width=60,height=60)

        # Img_Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=60,width=1365,height=100)
        
        #1st 
        img1=Image.open('images/police1.jpg')
        img1=img1.resize((500,100),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=500,height=100)

        #2nd
        img_2=Image.open('images/police2.jpg')
        img_2=img_2.resize((500,100),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=500,y=0,width=500,height=100)

        #3rd
        img_3=Image.open('images/police1.jpg')
        img_3=img_3.resize((500,100),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=900,y=0,width=500,height=100)

        #Main frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=160,width=1345,height=530)
        
        #upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Criminal Information",font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1320,height=250)

        #labels entry

        #case id
        caseid=Label(upper_frame,text='Case ID:',font=('arial',10,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        # Criminal no
        lbl_criminal_no=Label(upper_frame,text='Criminal NO:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_no.grid(row=0,column=2,padx=2,sticky=W,pady=7)

        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,sticky=W,pady=7)

        # Criminal Name
        lbl_Name=Label(upper_frame,text='Criminal Name:',font=('arial',11,'bold'),bg='white')
        lbl_Name.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,sticky=W,pady=7)

        # Nickname
        lbl_nickname=Label(upper_frame,text='Nickname:',font=('arial',11,'bold'),bg='white')
        lbl_nickname.grid(row=1,column=2,padx=2,sticky=W,pady=7)

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
        txt_nickname.grid(row=1,column=3,padx=2,sticky=W,pady=7)

        # Arrest Date
        lbl_arrestDate=Label(upper_frame,text='Arrest Date:',font=('arial',11,'bold'),bg='white')
        lbl_arrestDate.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('arial',11,'bold'))
        txt_arrestDate.grid(row=2,column=1,padx=2,sticky=W,pady=7)

        # Date of Crime
        lbl_dateofCrime=Label(upper_frame,text='Date of Crime:',font=('arial',11,'bold'),bg='white')
        lbl_dateofCrime.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        txt_dateofCrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',11,'bold'))
        txt_dateofCrime.grid(row=2,column=3,padx=2,sticky=W,pady=7)

        # Address
        lbl_address=Label(upper_frame,text='Address:',font=('arial',11,'bold'),bg='white')
        lbl_address.grid(row=3,column=0,padx=2,sticky=W,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=3,column=1,padx=2,sticky=W,pady=7)

        # Age
        lbl_age=Label(upper_frame,text='Age:',font=('arial',11,'bold'),bg='white')
        lbl_age.grid(row=3,column=2,padx=2,sticky=W,pady=7)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        txt_age.grid(row=3,column=3,padx=2,sticky=W,pady=7)

        # Occupation
        lbl_occupation=Label(upper_frame,text='Occupation:',font=('arial',11,'bold'),bg='white')
        lbl_occupation.grid(row=4,column=0,padx=2,sticky=W,pady=7)

        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        txt_occupation.grid(row=4,column=1,padx=2,sticky=W,pady=7)

        # birthMark
        lbl_birthMark=Label(upper_frame,text='Birth Mark:',font=('arial',11,'bold'),bg='white')
        lbl_birthMark.grid(row=4,column=2,padx=2,sticky=W,pady=7)

        txt_birthMark=ttk.Entry(upper_frame,textvariable=self.var_birthmark,width=22,font=('arial',11,'bold'))
        txt_birthMark.grid(row=4,column=3,padx=2,sticky=W,pady=7)

        # Crime type
        lbl_crimeType=Label(upper_frame,text='Crime Type:',font=('arial',11,'bold'),bg='white')
        lbl_crimeType.grid(row=0,column=4,padx=2,sticky=W,pady=7)

        txt_crimeType=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('arial',11,'bold'))
        txt_crimeType.grid(row=0,column=5,padx=2,sticky=W,pady=7)
        
        # Father Name
        lbl_fatherName=Label(upper_frame,text='Father Name:',font=('arial',11,'bold'),bg='white')
        lbl_fatherName.grid(row=1,column=4,padx=2,sticky=W,pady=7)

        txt_fatherName=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('arial',11,'bold'))
        txt_fatherName.grid(row=1,column=5,padx=2,sticky=W,pady=7)

         # gender
        lbl_gender=Label(upper_frame,text='Gender:',font=('arial',11,'bold'),bg='white')
        lbl_gender.grid(row=2,column=4,padx=2,sticky=W,pady=7)
 

        # wanted
        lbl_wanted=Label(upper_frame,text='Most Wanted:',font=('arial',11,'bold'),bg='white')
        lbl_wanted.grid(row=3,column=4,padx=2,sticky=W,pady=7)

        # radio button gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=700,y=80,width=190,height=30)
        
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)
        

        # radio button wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=700,y=120,width=190,height=30)
 
        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        
       
        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)

        # buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=188,width=620,height=40)

        # add button
        btn_add=Button(button_frame,command=self.add_data,text='Record Save',font=('arial',11,'bold'),width=15,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=2,pady=3)

        # Update button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',11,'bold'),width=15,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=2,pady=3)

        # Delete button
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',11,'bold'),width=15,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=2,pady=3)

        # Clear button
        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=('arial',11,'bold'),width=15,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=2,pady=3)

        #background side image
        img_crime=Image.open('images/police3.jpg')
        img_crime=img_crime.resize((375,195),Image.ANTIALIAS)
        self.photocrime=ImageTk.PhotoImage(img_crime)

        self.img_crime=Label(upper_frame,image=self.photocrime)
        self.img_crime.place(x=920,y=25,width=300,height=175)

        #down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Criminal Information Table",font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=260,width=1320,height=250)

        #Search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text="Search Criminal Record",font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1310,height=55)

        search_by=Label(search_frame,text='Search By:',font=('arial',11, 'bold'),bg='red',fg='white')
        search_by.grid(row=0,column=0,padx=4,sticky=W)

        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',11, 'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,padx=4,sticky=W)

        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,padx=2,sticky=W,pady=7)

        # Search button
        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',11,'bold'),width=15,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        # showall button
        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',11,'bold'),width=15,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",25,"bold"),text="Police Station",bg="white",fg="crimson")
        crimeagency.grid(row=0,column=5,sticky=W,padx=150)
        

        #table frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1310,height=165)
        
        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='CrimeNo')
        self.criminal_table.heading('3',text='CriminalName')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='ArrestDate')
        self.criminal_table.heading('6',text='CrimeOfDate')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='BirthMark')
        self.criminal_table.heading('11',text='CrimeType')
        self.criminal_table.heading('12',text='Father')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=50)
        self.criminal_table.column('2',width=55)
        self.criminal_table.column('3',width=90)
        self.criminal_table.column('4',width=90)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=90)
        self.criminal_table.column('8',width=50)
        self.criminal_table.column('9',width=90)
        self.criminal_table.column('10',width=90)
        self.criminal_table.column('11',width=90)
        self.criminal_table.column('12',width=90)
        self.criminal_table.column('13',width=90)
        self.criminal_table.column('14',width=90)
        

        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

     # Add function   
        
    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','ALL Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Swetha@0104',database='mgmt1')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                           self.var_case_id.get(),
                                                                                                           self.var_criminal_no.get(),
                                                                                                           self.var_name.get(),
                                                                                                           self.var_nickname.get(),
                                                                                                           self.var_arrest_date.get(),
                                                                                                           self.var_date_of_crime.get(),
                                                                                                           self.var_address.get(),
                                                                                                           self.var_age.get(),
                                                                                                           self.var_occupation.get(),
                                                                                                           self.var_birthmark.get(), 
                                                                                                           self.var_crime_type.get(),
                                                                                                           self.var_father_name.get(),
                                                                                                           self.var_gender.get(),
                                                                                                           self.var_wanted.get()
                                                                                                           ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close() 
                messagebox.showinfo('Success','Criminal record has been added successful')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)} ')

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='Swetha@0104',database='mgmt1')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close() 

    # get cursor
    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13]) 

    #update data

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update this criminal record')
                if update>0:
                   conn=mysql.connector.connect(host='localhost',user='root',password='Swetha@0104',database='mgmt1')
                   my_cursor=conn.cursor()
                   my_cursor.execute('update criminal set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(


                                                                                                                                                                                                                                                                                                                                                                                                                                                          self.var_criminal_no.get(),
                                                                                                                                                                                                                                                  self.var_name.get(),
                                                                                                                                                                                                                                                  self.var_nickname.get(),
                                                                                                                                                                                                                                                  self.var_arrest_date.get(),
                                                                                                                                                                                                                                                  self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                  self.var_address.get(),
                                                                                                                                                                                                                                                  self.var_age.get(),
                                                                                                                                                                                                                                                  self.var_occupation.get(),
                                                                                                                                                                                                                                                  self.var_birthmark.get(), 
                                                                                                                                                                                                                                                  self.var_crime_type.get(),
                                                                                                                                                                                                                                                  self.var_father_name.get(),
                                                                                                                                                                                                                                                  self.var_gender.get(),
                                                                                                                                                                                                                                                  self.var_wanted.get(),
                                                                                                                                                                                                                                                  self.var_case_id.get()

                                                                                                                                                                                                                                             ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data
                conn.close()
                messagebox.showerror('Sucess','Criminal record sucessfully updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)} ')

    #delete data
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                delete=messagebox.askyesno('Delete','Are you sure to delete this criminal record')
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='Swetha@0104',database='mgmt1')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showerror('Sucess','Criminal record sucessfully deleted')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)} ')

    #clear data
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=="":
           messagebox.showerror('Error','All Fields are required')  
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Swetha@0104',database='mgmt1')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                   self.criminal_table.delete(*self.criminal_table.get_children())
                for i in rows:
                   self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()        
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)} ')




        

        








if __name__ == '__main__':
    root=Tk()
    obj=Criminal(root)
    root.mainloop()