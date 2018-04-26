import csv
import datetime
import random
import string

# field names
fields = ['sub','b_id','b_title','b_auth','b_quantity','b_status','b_baranch']
filename = "book.csv"



# defining function for random
# string id with parameter
def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
# function call for random string
# generation with size 4 and string
#print(ran_gen(4, "jics"))
def size():
    n=0
    with open(filename, 'r', newline='') as csvfile:
        # creating a csv dict writer object
        reader = csv.DictReader(csvfile, fieldnames=fields)
        for row in reader:
            data = list(reader)
            n = len(data)

        return n
def last_id():
    id=0
    n=0
    n = size()
    if n>0:
        with open(filename,'r',newline='') as csvfile:
            # creating a csv dict writer object
            reader = csv.DictReader(csvfile, fieldnames=fields)
            for row in  reader:
                id = row['b_id']
                #print(row['b_id'])
            csvfile.close()
            #c = 1
            c = id[-3:].strip()
            k = str(int(c) + 1).zfill(3)
            return k
    else:
        return "000"

def new_entry():
    my = []
    mybook = {}
    mybook['sub']=input("Enter Subject             : ")
    mybook['b_title']=input("Enter book title          : ")
    myclient['b_auth']=input("Enter auther of book      : ")
    mybook['b_status']=mybook['b_quantity']=input("Enter the  no of books    : ")
    mybook['b_id']=ran_gen(4,"jics")+str(last_id())
    print("\n\t\tbook generated id is : ",mybook['b_id'],end='')
    my.append(mybook)
    with open(filename,'a',newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        with open(filename,'r',newline='') as csvinput:
            reader=csv.reader(csvinput)
            data=list(reader)
            no_lines=len(data)

        if no_lines ==0:
                 writer.writeheader()

        writer.writerows(my)
    csvfile.close()

def show_status(n):
    book=[]
    with open(filename,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book.append(row['b_id'])
    csvfile.close()
    if n in book:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['b_id']==n:
                    if row['b_status'] :
                        print(int(row['b_quantity'])-int(row['b_status'])," books are issuesd and ",int(row['b_status']),"are present",end='')
                    else:
                        print("all books are issued")
    else:
        print("no such book present ")
    csvfile.close()

def return_data(mr):
    with open(filename, 'r', newline='') as csvinput:
            names=[]
            for row in csv.reader(csvinput):
                names.append(row[0])
            csvinput.close()
            if mr in names:
                with open(filename, 'r', newline='') as csvinput:
                    for row in csv.reader(csvinput):
                        if row[0]==mr:
                           return row
            else:
                return "name"

    csvinput.close()

def move():
    input = open('kr.csv', 'r',newline='')
    output = open(filename, 'w',newline='')
    writer = csv.writer(output)
    for row in csv.reader(input):
            writer.writerow(row)
    input.close()
    output.close()

def delete_entry(n):
    input = open(filename, 'r',newline='')
    output = open('kr.csv', 'w',newline='')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[1]!=n:
            writer.writerow(row)
    input.close()
    output.close()

choice=1
print("[1] WANT TO ENTER A BOOK INTO LIBRARY")
print("[2] WANT TO REMOVE a BOOK IN STOCK")
print("[3] SEE STATUS ")
print("[4] EXIT")
myclient={}
while choice!=0:
    while True:
        try:
            choice = int(input("\n\nENTER THE CHOICE : "))
            break
        except:
            print("\n\tINVALID INPUT..")
    if choice==1:
        new_entry()
        print("ENTRY IS added INTO DATABASE")
    elif choice==2:
        id=input("\nId of book to remove       :")
        show_status(id)
        delete_entry(id)
        move()
    elif choice==3:
        id=input("enter the id of book ")
        show_status(id)
    elif choice==4:
        choice=0


