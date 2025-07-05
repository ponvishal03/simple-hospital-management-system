from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
win=Tk()
win.state('zoomed')
win.config(bg='blue')
#--------button fn---------
def pd():
    con=None
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        try:
            con=mysql.connector.connect(host="localhost",user="root", password="ksp303132", database="mydata",auth_plugin='mysql_native_password')
            my_cursor = con.cursor()

            # Fetching values from entry widgets
            patient_id = patientid.get()
            patient_name = patientname.get()
            patient_dob = dob.get()
            patient_gender = gender.get()
            patient_blood_group = bloodgroup.get()
            patient_address = patientaddress.get()
            patient_disease = disease.get()
            tablets_name = nameoftablets.get()
            no_of_tablets = nooftablets.get()
            dose_value = dose.get()
            blood_pressure = bloodpressure.get()
            issue_date = issuedate.get()
            follow_back = followback.get()
            phone_number = phoneno.get()

            # Executing the insert query
            my_cursor.execute("INSERT INTO hospital VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                patient_id,
                patient_name,
                patient_dob,
                patient_gender,
                patient_blood_group,
                patient_address,
                patient_disease,
                tablets_name,
                no_of_tablets,
                dose_value,
                blood_pressure,
                issue_date,
                follow_back,
                phone_number
            ))

            con.commit()
            messagebox.showinfo("Success", "Record has been inserted")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error occurred: {err}")
        finally:
            if con.is_connected():
                fetch_data()
                my_cursor.close()
                con.close()
def fetch_data():
    con=mysql.connector.connect(host="localhost",user="root", password="ksp303132", database="mydata",auth_plugin='mysql_native_password')
    my_cursor = con.cursor()
    my_cursor.execute('select*from hospital')
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        table.delete(*table.get_children())
        for items in rows:
            table.insert('',END,values=items)
        con.commit()
        con.close()

def get_data(event=''):
    cursor_row=table.focus()
    data=table.item(cursor_row)
    row=data['values']
    patientid.set(row[0])
    patientname.set(row[1])
    dob.set(row[2])
    gender.set(row[3])
    bloodgroup.set(row[4])
    patientaddress.set(row[5])
    disease.set(row[6])
    nameoftablets.set(row[7])
    nooftablets.set(row[8])
    dose.set(row[9])
    bloodpressure.set(row[10])
    issuedate.set(row[11])
    followback.set(row[12])
    phoneno.set(row[13])
#------prescription data---------
def pre():
    txt_frame.insert(END,'Patient ID:\t\t\t'+patientid.get()+'\n')
    txt_frame.insert(END,'Patient Name:\t\t\t'+patientname.get()+'\n')
    txt_frame.insert(END,'DOB:\t\t\t'+dob.get()+'\n')
    txt_frame.insert(END,'Gender:\t\t\t'+gender.get()+'\n')
    txt_frame.insert(END,'Blood Group:\t\t\t'+bloodgroup.get()+'\n')
    txt_frame.insert(END,'Patient Address:\t\t\t'+patientaddress.get()+'\n')
    txt_frame.insert(END,'Disease:\t\t\t'+disease.get()+'\n')
    txt_frame.insert(END,'Name of Tablets:\t\t\t'+nameoftablets.get()+'\n')
    txt_frame.insert(END,'No of Tablets:\t\t\t'+nooftablets.get()+'\n')
    txt_frame.insert(END,'Dose:\t\t\t'+dose.get()+'\n')
    txt_frame.insert(END,'Blood Pressure:\t\t\t'+bloodpressure.get()+'\n')
    txt_frame.insert(END,'Issue Date:\t\t\t'+issuedate.get()+'\n')
    txt_frame.insert(END,'Follow Back:\t\t\t'+followback.get()+'\n')
    txt_frame.insert(END,'Phone No:\t\t\t'+phoneno.get()+'\n')
#--delete---
def delete():
    con=mysql.connector.connect(host="localhost",user="root", password="ksp303132", database="mydata",auth_plugin='mysql_native_password')
    my_cursor = con.cursor()
    querry=('DELETE FROM hospital WHERE patient_id = %s')
    value=(patientid.get(),)
    my_cursor.execute(querry,value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo('Deleted','patient data has been deleted')
#--clear--
def clear():
    patientid.set('')
    patientname.set('')
    dob.set('')
    gender.set('')
    bloodgroup.set('')
    patientaddress.set('')
    disease.set('')
    nameoftablets.set('')
    nooftablets.set('')
    dose.set('')
    bloodpressure.set('')
    issuedate.set('')
    followback.set('')
    phoneno.set('')
    txt_frame.delete(1.0,END)
#---exit---
def exit():
    confirm = messagebox.askyesno('confirmation','Are You Sure You Want To Exit')
    if confirm>0:
        win.destroy()
        return
#Heading
Label(win,text='Hospital Management System',font='impack 31 bold',bg='blue',fg='white').pack()
#frame1
frame1=Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1538,height=400.5)
#Label frame for patient info
lf1 = LabelFrame(frame1,text='Patient Information',font='ariel 10 bold',bd=10,bg='pink')
lf1.place(x=1.5,y=0,width=900,height=375)
#LABEL FOR PATIENT INFORMATION
Label(lf1,text='Patient ID :',bg='pink').place(x=5,y=10)
Label(lf1,text='Patient Name :',bg='pink').place(x=5,y=60)
Label(lf1,text='DOB :',bg='pink').place(x=5,y=110)
Label(lf1,text='Gender :',bg='pink').place(x=5,y=160)
Label(lf1,text='Blood Group :',bg='pink').place(x=5,y=210)
Label(lf1,text='Patient Address :',bg='pink').place(x=5,y=260)
Label(lf1,text='Disease :',bg='pink').place(x=5,y=310)
Label(lf1,text='Name of Tablets :',bg='pink').place(x=480,y=10)
Label(lf1,text='No of Tablets :',bg='pink').place(x=480,y=60)
Label(lf1,text='Dose :',bg='pink').place(x=480,y=110)
Label(lf1,text='Blood Pressure :',bg='pink').place(x=480,y=160)
Label(lf1,text='Issue Date :',bg='pink').place(x=480,y=210)
Label(lf1,text='Follow Back :',bg='pink').place(x=480,y=260)
Label(lf1,text='Phone No :',bg='pink').place(x=480,y=310)
#text variable for every entry field
patientid=StringVar()
patientname=StringVar()
dob=StringVar()
gender=StringVar()
bloodgroup=StringVar()
patientaddress=StringVar()
disease=StringVar()
nameoftablets=StringVar()
nooftablets=StringVar()
dose=StringVar()
bloodpressure=StringVar()
issuedate=StringVar()
followback=StringVar()
phoneno=StringVar()
#Entry Field for all Labels
e1=Entry(lf1,bd=4,textvariable=patientid)
e1.place(x=130,y=10,width=200)
e2=Entry(lf1,bd=4,textvariable=patientname)
e2.place(x=130,y=60,width=200)
e3=Entry(lf1,bd=4,textvariable=dob)
e3.place(x=130,y=110,width=200)
e4=Entry(lf1,bd=4,textvariable=gender)
e4.place(x=130,y=160,width=200)
e5=Entry(lf1,bd=4,textvariable=bloodgroup)
e5.place(x=130,y=210,width=200)
e6=Entry(lf1,bd=4,textvariable=patientaddress)
e6.place(x=130,y=260,width=200)
e7=Entry(lf1,bd=4,textvariable=disease)
e7.place(x=130,y=310,width=200)
e8=Entry(lf1,bd=4,textvariable=nameoftablets)
e8.place(x=600,y=10,width=200)
e9=Entry(lf1,bd=4,textvariable=nooftablets)
e9.place(x=600,y=60,width=200)
e10=Entry(lf1,bd=4,textvariable=dose)
e10.place(x=600,y=110,width=200)
e11=Entry(lf1,bd=4,textvariable=bloodpressure)
e11.place(x=600,y=160,width=200)
e12=Entry(lf1,bd=4,textvariable=issuedate)
e12.place(x=600,y=210,width=200)
e13=Entry(lf1,bd=4,textvariable=followback)
e13.place(x=600,y=260,width=200)
e14=Entry(lf1,bd=4,textvariable=phoneno)
e14.place(x=600,y=310,width=200)
#Label frame for prescription
lf2 = LabelFrame(frame1,text='Prescription',font='ariel 10 bold',bd=10,bg='light green')
lf2.place(x=900,y=0,width=606,height=372)
#text box for prescription
txt_frame = Text(lf2,font='impack 10 bold',width=40,height=30,bg='yellow')
txt_frame.pack(fill=BOTH)
#frame2
frame2=Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=455,width=1538,height=289.5)
#button
#delete button
delete_btn = Button(win,text='Delete',font='ariel 15 bold',bg='brown',fg='white',bd=6,cursor='hand2',command=delete)
delete_btn.place(x=0,y=745,width=280)
#prescription Button
p_btn = Button(win,text='Prescription',font='ariel 15 bold',bg='purple',fg='white',bd=6,cursor='hand2',command=pre)
p_btn.place(x=280,y=745,width=280)
#save prescription data
pd_btn = Button(win,text='Save Prescription Data',font='ariel 15 bold',bg='Green',fg='white',bd=6,cursor='hand2',command=pd)
pd_btn.place(x=559,y=745,width=310)
#clear Button
c_btn = Button(win,text='Clear',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=clear)
c_btn.place(x=868,y=745,width=300)
#Exit Button
exit_btn = Button(win,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2',command=exit)
exit_btn.place(x=1169,y=745,width=370)
#Scroll Bar for Preciption data
scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')
scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')
table=ttk.Treeview(frame2,columns=('pid','pn','dob','ge','blg','pa','dis','not','nt','dd','bp','id','fb','po'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)
#heading for prescription data
table.heading('pid',text='Patient ID')
table.heading('pn',text='Name of Patient')
table.heading('dob',text='DOB')
table.heading('ge',text='Gender')
table.heading('blg',text='Blood Group')
table.heading('pa',text='Patient Address')
table.heading('dis',text='Disease')
table.heading('not',text='Name of Tablet')
table.heading('nt',text='No of Tablets')
table.heading('dd',text='Dose')
table.heading('bp',text='Blood Pressure')
table.heading('id',text='Issue Date')
table.heading('fb',text='Follow Back')
table.heading('po',text='Phone No')
table['show']='headings'
table.pack(fill=BOTH,expand=1)
#-----------------------------
table.column('pid',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('ge',width=100)
table.column('blg',width=100)
table.column('pa',width=100)
table.column('dis',width=100)
table.column('not',width=100)
table.column('nt',width=100)
table.column('dd',width=100)
table.column('bp',width=100)
table.column('id',width=100)
table.column('fb',width=100)
table.column('po',width=100)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()
