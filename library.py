import os
import csv

def addBook():
    print("Add a new Book Record")
    print("******************************")
    f=open('library.csv','a',newline='\r\n')
    s=csv.writer(f)
    bookid=int(input('Enter book id='))
    bookname=input('Enter book name=')
    bookauthor=input('Enter author name=')
    price=float(input('Enter price='))
    copies=float(input('Enter number of copies='))
    rec=[bookid,bookname,bookauthor,price,copies]
    s.writerow(rec)
    f.close()
    print("Book Record Saved")
    input("Press any key to continue..")

def modifyBook():
    print("Modify a Book Record")
    print("<<<<<<<<<<=======>>>>>>>>>>>")
    f=open('library.csv','r',newline='\r\n')
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter bookid whose record you want to modify=')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("-------------------------------")
            print("Book id=",rec[0])
            print("Book Name=",rec[1])
            print("Author=",rec[2])
            print("Price=",rec[3])
            print("Number of copies=",rec[4])
            print("-------------------------------")
            choice=input("Do you want to modify this Book Record(y/n)=")
            if choice=='y' or choice=='Y':
                bookid=int(input('Enter new book id='))
                bookname=input('Enter new book name=')
                bookauthor=input('Enter new author name=')
                price=float(input('Enter new price='))
                copies=float(input('Enter new number of copies='))
                rec=[bookid,bookname,bookauthor,price,copies]
                s1.writerow(rec)
                print("Book Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("library.csv")
    os.rename("temp.csv","library.csv")
    input("Press any key to continue..")

def deleteBook():
    f=open('library.csv','r',newline='\r\n')
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter bookid whose record you want to delete')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("-------------------------------")
            print("Book id=",rec[0])
            print("Book Name=",rec[1])
            print("Author=",rec[2])
            print("Price=",rec[3])
            print("Number of copies=",rec[4])
            print("-------------------------------")
            choice=input("Do you want to delete this Book Record(y/n)")
            if choice=='y' or choice=='Y':
                pass
                print("Book Record Deleted....")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("library.csv")
    os.rename("temp.csv","library.csv")
    input("Press any key to continue..")

def listallbooks():
    print("List of All Books")
    print("<<<<<<<<<<<<=========>>>>>>>>>>>>>>")
    f=open('library.csv','r',newline='\r\n')
    s=csv.reader(f)
    i=1
    print("bookid",end="\t\t\t")
    print("bookname",end="\t\t\t")
    print("bauthor",end="\t\t\t\t")
    print("price",end="\t\t\t\t")
    print("copies",end="\t\t\t\t\t\n")
    for rec in s:
        print(rec[0],end="\t\t\t")
        print(rec[1],end="\t\t\t\t")
        print(rec[2],end="\t\t\t\t")
        print(rec[3],end="\t\t\t\t")
        print(rec[4],end="\n")
        i+=1
    f.close()
    print("-------------------------------")
    input("Press any key to continue..")

def mainmenu():
    choice=0
    while choice!=6:
        print("\n")
        print("|****************************|")
        print("| Libary Management System |")
        print("|****************************|")
        print('\n')
        print("########################")
        print(" Main Menu")
        print("########################")
        print("1. Add a new Book Record")
        print("2. Modify Existing Book Record")
        print("3. Delete Existing Book Record")
        print("4. List all Books")
        print("5.Exit")
        print("-------------------------------")
        choice=int(input('Enter your choice'))
        if choice==1:
            addBook()
        elif choice==2:
            modifyBook()
        elif choice==3:
            deleteBook()
        elif choice==4:
            listallbooks()
        elif choice==5:
            print("Software Terminated.......")
            break

mainmenu()
