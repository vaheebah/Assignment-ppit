from tkinter import *
import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\vahee\Desktop\Database.accdb;'
    conn=pyodbc.connect(con_string)
    print("Connected To Database")
except pyodbc.Error as e:
    print("Error in Connection", e)

cur=conn.cursor()
#CNIC FINDER
def findUser(CNIC):
    cur.execute("SELECT * FROM Table1 where CNIC=?",(CNIC))
    data=cur.fetchall()
    if(len(data)==0):
        return 0
    else :
        return 1

#ClearRecord function
def ClearRecord():
    #Write your Clear Record Code Here
    sNameValue.set("")
    fNameValue.set("")
    marksValue.set("")
    cnicValue.set("")
    cityValue.set("")
    message.config(text="Record Cleared Successfully",foreground="green")
#FirstRecord function
def FirstRecord():
    # Write your First Record Code Here
    cur.execute("SELECT * FROM Table1 ")
    data=cur.fetchall()[0]
    CNIC,StudentName, FatherName, CITY ,MARKS=data
    cnicValue.set(CNIC)
    sNameValue.set(StudentName)
    fNameValue.set(FatherName)
    cityValue.set(CITY)
    marksValue.set(MARKS)
    conn.commit()
    message.config(text="First Record Found Successfully",foreground="green")

i=0
#NextRecord function
def NextRecord():
    #Write your Next Record Code Here
    global i
    i=i+1
    cur.execute("SELECT * FROM Table1 ")
    
    data=cur.fetchall()[i]
    CNIC,StudentName,FatherName,CITY,MARKS=data
    cnicValue.set(CNIC)
    sNameValue.set(StudentName)
    fNameValue.set(FatherName)
    cityValue.set(CITY)
    marksValue.set(MARKS)
    conn.commit()
    message.config(text="Next Record Found Successfully",foreground="green")

#PreviousRecord function
def PreviousRecord():
    # Write your Previous Record Code Here
    global i
    i=i-1
    cur.execute("SELECT * FROM Table1 ")
    data = cur.fetchall()[i]
    CNIC,StudentName, FatherName,  CITY, MARKS = data
    cnicValue.set(CNIC)
    sNameValue.set(StudentName)
    fNameValue.set(FatherName)
    cityValue.set(CITY)
    marksValue.set(MARKS)
    conn.commit()
    message.config(text="Previous Record Found Successfully",foreground="green")
#LastRecord function
def LastRecord():
    # Write your Last Record Code Here
    cur.execute("SELECT * FROM Table1")
    data = cur.fetchall()[-1]
    CNIC,Student,Father,CITY,MARKS = data
    cnicValue.set(CNIC)
    sNameValue.set(Student)
    fNameValue.set(Father)
    cityValue.set(CITY)
    marksValue.set(MARKS)
    conn.commit()
    message.config(text="Last Record Found Successfully",foreground="green")
#InsertRecord function
def InsertRecord():
    # Write your Insert Record Code Here
    StudentName=sNameValue.get()
    FatherName=fNameValue.get()
    CNIC=cnicValue.get()
    CITY=cityValue.get()
    MARKS=marksValue.get()
    if(CNIC=="") or (findUser(CNIC)):
        CNIC=NONE
        try:
             cur.execute(f"INSERT INTO Table1 (StudentName,FatherName,CNIC,CITY,MARKS) Values (?,?,?,?,?);",(StudentName, FatherName, CNIC, CITY, MARKS))
             conn.commit()
        except pyodbc.Error as e:
            print("Insert err",e)
            message.config(text="DATA INVALID OR DATA ALREADY EXIST",foreground="red")

    else:
        message.config(text="DATA INSERTED SUCCESSFULLY",foreground="green")

#UpdateRecord function
def UpdateRecord():
    # Write your Update Record Code Here
    StudentName=sNameValue.get()
    FatherName=fNameValue.get()
    CNIC=cnicValue.get()
    CITY=cityValue.get()
    MARKS=marksValue.get()
    if(findUser(CNIC)):
        cur.execute("UPDATE Table1 set StudentName=?,FatherName=?,City=?,Marks=?  WHERE CNIC=? ",(StudentName,FatherName,CITY,MARKS,CNIC))
        conn.commit()
        message.config(text="Data Updated Successfully", foreground="green")
    else:
        message.config(text="FAILED TO UPDATE NO RECORD FOUND", foreground="red")
#DeleteRecord function
def DeleteRecord():
    # Write your Delete Record Code Here
     CNIC = cnicValue.get()
     if(findUser(CNIC)):
         cur.execute("DELETE * FROM Table1 where CNIC=?", (CNIC))
         conn.commit()
         ClearRecord()
         message.config(text="Data Deleted Successfully", foreground="green")
     else:
        message.config(text="NO RECORD FOUND",foreground="red")

#SearchRecord function
def SearchRecord():
    # Write your Search Record Code Here
    CNIC=cnicValue.get()
    if(findUser(CNIC)):
        cur.execute("SELECT * FROM Table1 where CNIC=?",(CNIC))
        data=cur.fetchall()[0]
        CNIC,StudentName,FatherName,CITY,MARKS=data
        cnicValue.set(CNIC)
        sNameValue.set(StudentName)
        fNameValue.set(FatherName)
        cityValue.set(CITY)
        marksValue.set(MARKS)
        conn.commit()
        message.config(text="SEARCH COMPLETED!RECORD FOUND", foreground="green")
    else:
        message.config(text="SEARCH COMPLETED!NO SUCH RECORD FOUND",foreground="red")


#Design the Student Database Form
root = Tk()
root.geometry("600x400")

#
Label(root, text = "Student Database Form", font="Arial 12 bold", foreground='blue').grid(row=0, column=0)
message = Label(root, text = "Message Will Appear Here!",foreground='red')
sname = Label(root,text='Student Name', font="ar 10 bold")
fname = Label(root,text='Father Name',font="ar 10 bold")
cnic = Label(root,text='CNIC# (P.Key)',font="ar 10 bold")
search = Label(root,text='Search Record',font="ar 10 bold")
city = Label(root,text='City',font="ar 10 bold")
marks = Label(root,text='Marks',font="ar 10 bold")

message.grid(row=0,column=1)
sname.grid(row=2,column=0)
fname.grid(row=3,column=0)
cnic.grid(row=4,column=0)
search.grid(row=4,column=2)
city.grid(row=5,column=0)
marks.grid(row=6,column=0)

sNameValue = StringVar()
fNameValue = StringVar()
cnicValue = StringVar()
cityValue = StringVar()
marksValue = IntVar()

sNameEntery = Entry(root, textvariable=sNameValue,width='30',font='ar 12 bold')
fNameEntery = Entry(root, textvariable=fNameValue,width='30',font='ar 12 bold')
cnicEntery = Entry(root, textvariable=cnicValue,width='30',font='ar 12 bold')
cityEntery = Entry(root, textvariable=cityValue,width='30',font='ar 12 bold')
marksEntery = Entry(root, textvariable=marksValue,width='30',font='ar 12 bold')

sNameEntery.grid(row=2,column=1,pady=15)
fNameEntery.grid(row=3,column=1,pady=15)
cnicEntery.grid(row=4,column=1,pady=15)
cityEntery.grid(row=5,column=1,pady=15)
marksEntery.grid(row=6,column=1,pady=15)

Button(text="CLEAR",command=ClearRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=7,column=0)
Button(text="FIRST",command=FirstRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=7,column=1)
Button(text="NEXT",command=NextRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=7,column=2)
Button(text="PREVIOUS",command=PreviousRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=9,column=0)
Button(text="LAST",command=LastRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=9,column=1)
Button(text="INSERT",command=InsertRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=9,column=2)
Button(text="UPDATE",command=UpdateRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=11,column=0)
Button(text="DELETE",command=DeleteRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=11,column=1)
Button(text="SEARCH",command=SearchRecord,background='gray',foreground='blue',font='ar 10 bold').grid(row=11,column=2)

root.mainloop()

