#------------------------------------------------------------------------------------------
from tabulate import tabulate
import mysql.connector
import datetime 
#_________mysql.connector module for database connectivity__________________
conn=mysql.connector.connect(host="localhost",user="root",password="",database="library")
mycursor=conn.cursor()

#----------------to clear the screen-------------------------------------------
from os import system, name
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
#----------------To Display Data from BOOK table ------------------------------------------
def show_book():
    mycursor.execute("select * from book")
    book_data=list()
    inr=[]
    for i in mycursor:
        inr=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
        book_data.append(inr)
    #print(tabulate(book_data,headers=["Book_id","Title","Author","Publisher","Pages","Price","Edition","Copies"]))
    print(tabulate(book_data,headers=["Book_id","Title","Author","Publisher","Pages","Price","Edition","Copies"],tablefmt="github"))
    a=input()
#----------------To Display Data from MEMBER table ---------------------------------
def show_member():
    mycursor.execute("select * from member")
    member_data=list()
    inr=[]
    for i in mycursor:
        inr=[i[0],i[1],i[2],i[3],i[4],i[5]]
        member_data.append(inr)
    #print(tabulate(member_data,headers=["Member_id","Name","Class","Address","Mobile_number","Email"]))
    print(tabulate(member_data,headers=["Member_id","Name","Class","Address","Mobile_number","Email"],tablefmt="github"))
    a=input()
#----------------To Display Data from TRANSACTION table ---------------------------------
def show_transactions():
    mycursor.execute("select * from transactions")
    trans_data=list()
    inr=[]
    for i in mycursor:
        inr=[i[0],i[1],i[2],i[3],i[4]]
        trans_data.append(inr)
    print(tabulate(trans_data,headers=["Trans_id","Book_id","Member_id","Date of issue","Date of return"],tablefmt="github"))
    a=input()
#------------------status of book----------------
def book_status(bid):
    sql="select*from book where book_id=%s"%(bid)
    mycursor.execute(sql)
    result=mycursor.fetchone()
    return result[7]
#------------------status of member issue----------------
def mem_issue_status(mid):
    sql='select * from transactions where member_id=%s and dor IS NULL'%(mid)
    mycursor.execute(sql)
    results=mycursor.fetchall()
    return results

#*************************************************************************************************************************    
#****************************************************************************************

#-------------------MAIN MENU------------------------        
while (True):
    clear()
    print("\n")
    print("************Library Management*************")
    print()
    print("     Enter 1  :  ADD BOOK RECORD")
    print("     Enter 2  :  ADD MEMBER DETAILS")
    print("     Enter 3  :  UPDATE BOOKS")
    print("     Enter 4  :  UPDATE MEMBERS")
    print("     Enter 5  :  ISSUE BOOK")
    print("     Enter 6  :  RETURN BOOK")
    print("     Enter 7  :  SEARCH MENU")
    print("     Enter 8  :  DISPLAY MENU")
    print("     Enter 9  :  STATUS MENU")
    print("     Enter 10 :  EXIT")
    print()
    print("********************************************")
    ch=int(input("enter your choice  :  "))
    print("\n")

#____________1. ADD BOOK RECORD_____________________
    
    if ch==1:
        clear()
        print()
        print("****************Enter BOOK Details***************")
        print()
        title=input("   Enter Book Title\t:\t")
        author=input("   Enter Book Author\t:\t")
        pub=input("   Enter Book Publisher\t:\t")
        pg=int(input("   Enter Book Pages\t:\t"))
        price=float(input("   Enter Book Price\t:\t"))
        edi=int(input("   Enter Book Edition\t:\t"))
        copies=int(input("   Enter no. of copies\t:\t"))
        cmd="insert into book(title,author,publisher,pages,price,edition,copies)values(%s,%s,%s,%s,%s,%s,%s)"
        val=(title,author,pub,pg,price,edi,copies)
        mycursor.execute(cmd,val)
        conn.commit()
        print("\n\nNew Book added successfully")

#____________2.ADD MEMBER RECORD_____________________
        
    elif ch==2:
        clear()
        print()
        print("****************Enter MEMBER Details***************")
        print()
        n=input("   Enter Member Name\t:\t")
        cls=input("   Enter Member class\t:\t")
        add=input("   Enter Member address\t:\t")
        mob=int(input("   Enter Member mobile number\t:\t"))
        email=input("   Enter Member email id\t:\t")
        cmd="insert into member(name,class,address,mobile,email)values(%s,%s,%s,%s,%s)"
        val=(n,cls,add,mob,email)
        mycursor.execute(cmd,val)
        conn.commit()
        print("\n\nNew Member added successfully")

#____________3. UPDATE BOOK DETAILS_____________________
    elif ch==3:
        clear()
        print()
        print("******** Update BOOK Details ************")
        print()
        show_book()
        print()
        bid=int(input("Enter Book ID to change data   :   "))
        print("\n\n")
        print("Press 1. Title")
        print("Press 2. Author")
        print("Press 3. Publisher")
        print("Press 4. Pages")
        print("Press 5. Price")
        print("Press 6. Edition")
        print("Press 7. Copies")
        print()
        c2=int(input("\n\n Enter your choice    :    "))
        if c2==1:
            t=input("Enter new Title   :   ")
            query="Update book SET Title='%s' where Book_id=%s"%(t,bid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_book()
        elif c2==2:
            a=input("Enter new Author  :   ")
            query="Update book SET Author='%s' where Book_id=%s"%(a,bid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_book()
        elif c2==3:
            p=input("Enter new Publisher   :   ")
            query="Update book SET Publisher='%s' where Book_id=%s"%(p,bid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_book()
        elif c2==4:
            pg=input("Enter new number of pages   :   ")
            query="Update book SET Pages='%s' where Book_id=%s"%(pg,bid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_book()
        elif c2==5:
            pr=input("Enter new price   :   ")
            query="Update book SET Price='%s' where Book_id=%s"%(pr,bid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_book()
        elif c2==6:
            ed=input("Enter new Edition   :   ")
            query="Update book SET Edition='%s' where Book_id=%s"%(ed,bid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_book()
        elif c2==7:
            cp=input("Enter new no.of copies   :   ")
            query="Update book SET Copies='%s' where Book_id=%s"%(cp,bid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_book()
        else:
            print("sorry invalid option")
#____________4. UPDATE MEMBER DETAILS_____________________
    elif ch==4:
        clear()
        print()
        print("******** Update MEMBER Details ************")
        print()
        show_member()
        print()
        mid=int(input("Enter Member ID to change data   :   "))
        print("\n\n")
        print("Press 1. Name")
        print("Press 2. Class")
        print("Press 3. Address")
        print("Press 4. Mobile")
        print("Press 5. Email")
        print()
        c3=int(input("\n\n Enter your choice    :    "))
        if c3==1:
            n=input("Enter new Name   :   ")
            query="Update member SET Name='%s' where Member_id=%s"%(n,mid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_member()
        elif c3==2:
            c=input("Enter new Class  :   ")
            query="Update member SET Class='%s' where Member_id=%s"%(c,mid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_member()
        elif c3==3:
            ad=input("Enter new Address   :   ")
            query="Update member SET Address='%s' where Member_id=%s"%(ad,mid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_member()
        elif c3==4:
            mob=input("Enter new Mobile   :   ")
            query="Update member SET Mobile='%s' where Member_id=%s"%(mob,mid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_member()
        elif c3==5:
            e=input("Enter new Email   :   ")
            query="Update member SET Email='%s' where Member_id=%s"%(e,bid)
            mycursor.execute(query)
            conn.commit()
            print("\n\n Data Successfully Updated\n\n")
            show_member()
        else:
            print("sorry invalid option")
#__________5. ISSUE BOOK ______________________
    elif ch==5:
        clear()
        print()
        print("*************BOOK ISSUE SCREEN*************")
        print()
        bid=int(input("     Enter Book ID\t:\t"))
        mid=int(input("     Enter Member ID\t:\t"))
        result=book_status(bid)
        results=mem_issue_status(mid)
        if len(results)==0:
            if result==0:
                print('\n\nBook is not available for ISSUE...')
            else:
                today=input("enter date of issue   :   ")
                sql="insert into transactions(book_id,member_id,doi) values(%s,%s,'%s')"%(bid,mid,today)
                book="update book set copies=copies-1 where book_id=%s"%(bid)
                mycursor.execute(sql)
                mycursor.execute(book)
                conn.commit()
                print("\n\n book issued successfully")
                print()
            
            
        else:
            print('\n\nMember already have book from the Library')
            print()
            

#__________6. RETURN BOOK ______________________
    elif ch==6:
        clear()
        print()
        print("*************BOOK Return SCREEN*************")
        print()
        bid=int(input("     Enter Book ID\t:\t"))
        mid=int(input("     Enter Member ID\t:\t"))
        
        sql = 'select * from transactions where book_id =%s and member_id =%s and dor is NULL'%(bid,mid)
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result==None:
            print('Book was not issued...Check Book Id and Member ID again..')
            print()
        else:
            r=input("     Enter date of return (in YYYY-MM-DD)   :\t")
            sql='update book set copies =copies+1 where book_id =%s'%(bid)
            sql1 ='update transactions set dor="%s" where book_id=%s and member_id=%s'%(r,bid,mid) 
            mycursor.execute(sql)
            mycursor.execute(sql1)
            conn.commit()
            print('\n\nBook returned successfully')
            print()
        
#__________7. SEARCH MENU ______________________
    elif ch==7:
        clear()
        print()
        print("************* SEARCH  MENU ******************")
        print()
        print("         1. Search in BOOK Record")
        print("         2. Search in MEMBER Record")
        s=int(input(" enter your choice\t:\t"))
        if s==1:
            while True:
                b=input("enter book title   :   ")
                found=0
                query="select * from book where title='%s'"%b
                mycursor.execute(query)
                data=mycursor.fetchall()
                for i in data:
                    print('\n')
                    print(i)
                    print("\n")
                    found=1
                if found==0:
                    print("no records found......")
                c=input("Do you want to search for more records (y/n)  : ")
                if c in 'Nn':
                    break
        if s==2:
            while True:
                n=input("enter name   :   ")
                found=0
                query="select * from member where name='%s'"%n
                mycursor.execute(query)
                data=mycursor.fetchall()
                for i in data:
                    print(i)
                    found=1
                if found==0:
                    print("no records found......")
                c=input("Do you want to search for more records (y/n)  : ")
                if c in 'Nn':
                    break
        else:
            print("invalid choice")
            
#____________8. DISPLAY MENU____________
    elif ch==8:
        clear()
        print()
        print("*************REPORT DISPLAY SCREEN******************")
        print()
        print("        Press 1. Display BOOK Record")
        print("        Press 2. Display MEMBER Record")
        dis=int(input(" enter your choice\t:\t"))
        if dis==1:
            show_book()
        elif dis==2:
            show_member()
        else:
            print("invalid choice")
#_______________9. STATUS MENU______________
    elif ch==9:
        clear()
        print()
        cc=input("\n  DO YOU WANT TO SEE CURRENT STATUS OF BOOKS ISSUED? (Y,N)   ")
        if cc in 'Yy':
            show_transactions()
        else:
            clear()
#_____________10. EXIT______________
    elif ch==10:
        print("thank you for using LIBRARY MANAGEMENT SOFTWARE")
        a=input("  ")
        break


    else:
        print(" Invalid option")
        
#------------------------------------------------------------------------------------------------------------------------
        
        
