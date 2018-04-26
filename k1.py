import csv
import datetime

import random
import string
bfield = ['sub','b_id','b_title','b_auth','b_quantity','b_status','b_baranch']
bfile = "book.csv"
sfield=['name','clg_id','cards','b1','p1','d1_is','d1_re','b2','p2','d2_is','d2_re','p3','b3','d3_is','d3_re']
sfile="st.csv"
def issue():
    st=[]
    now = datetime.datetime.now()
    student={}
    sid=student['clg_id']=input("college id ")
    n=check(sid)
    #print("n is ",n)
    if n==0:#entry
        bid=input("id of book  :")
        c = show_status(bid)
        if c==0:
            print("no such book present ")
        else:
            student['name']=input("name : ")
            student['cards']=2
            student['b1']=bid
            student['d1_is']=now.date()
            re_issue_date =now.date()+ datetime.timedelta(days=14)
            student['d1_re']=re_issue_date
            st.append(student)
            data_entry(st)
    elif n==-1:#no issue
        print("you are out of cards")
        return
    elif n==1:#edit
        bid = input("id of book  :")
        c = show_status(bid)
        if c:
            set(bid,sid)
        else:
            print("no such book present ")
# defining function for random
# string id with parameter
def check(sid):
    n=size()
    data=[]
    if n>0:
        with open(sfile,'r',newline='') as f:
            reader =csv.DictReader(f)
            for row in reader:
                data.append(row['clg_id'])
            f.close()
            if sid in data:
                with open(sfile, 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row['clg_id']==sid:
                            if int(row['cards']):
                                f.close()
                                print("he can issue")
                                return 1 #if he can issue
                            else:
                                f.close()
                                print("no cards")
                                return -1  #no cards
                f.close()
            else:
                print("new entry")
                return 0#no entry

    else:
        print("new entry")
        return 0 #new entry

def size():
    n=0
    with open(sfile, 'r', newline='') as csvfile:
        # creating a csv dict writer object
        reader = csv.DictReader(csvfile, fieldnames=bfield)
        for row in reader:
            data = list(reader)
            n = len(data)

        return n
def show_status(bid):
    book=[]
    with open(bfile,'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            book.append(row[1])
    csvfile.close()
    if bid in book:
        return 1
    else:
       return 0

def data_entry(myrec):
    with open(sfile, 'a',newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=sfield)

        #writing headers (field names)
        with open(sfile,'r',newline='') as csvinput:
            reader=csv.reader(csvinput)
            data=list(reader)
            no_lines=len(data)
        if no_lines ==0:
              writer.writeheader()
        # writing data rows
        writer.writerows(myrec)
    csvfile.close()
def set(bid,sid):
    s={}
    b={}
    st=[]
    bk=[]
    now = datetime.datetime.now()
    st=return_data(sid,sfile)
    for i in range(0, len(st)):
        s[sfield[i]] = st[i]
    bk=return_data(bid,bfile)
    for i in range(0, len(bk)):
        b[bfield[i]] = bk[i]
    re_issue_date=now.date() + datetime.timedelta(days=14)
    x = int(s['cards'])
    if x==2:
        s['b2'] = bid
        s['d2_is'] = now.date()
        s['d2_re'] = re_issue_date

    elif x==1:
        s['b3'] = bid
        s['d3_is'] = now.date()
        s['d3_re'] = re_issue_date

    elif x==0:
        print("you are you  of cards ")
        return

    s['cards'] = int(s['cards']) - 1
    b['b_status'] = int(b['b_status']) - 1
    st.append(s)
    bk.append(b)
    delete_entry(bid,bfile)
    delete_entry(sid,sfile)

    update(b,bfile,bfield)
    update(s,sfile,sfield)
    print("updated")
def return_data(id,file):
    with open(file, 'r', newline='') as csvinput:
            names=[]
            for row in csv.reader(csvinput):
                names.append(row[1])
            csvinput.close()
            if id in names:
                with open(file, 'r', newline='') as csvinput:
                    for row in csv.reader(csvinput):
                        if row[1]==id:
                            return row
            else:
                return "name"
def delete_entry(n,f):
    input = open(f, 'r',newline='')
    output = open('kb.csv', 'w',newline='')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[1]!=n:
            writer.writerow(row)
    input.close()
    output.close()
    move(f)
def move(f):
    input = open('b.csv', 'r',newline='')
    output = open(f, 'w',newline='')
    writer = csv.writer(output)
    for row in csv.reader(input):
            writer.writerow(row)
    input.close()
    output.close()


def update(x,file,field):
    with open(file, 'a',newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=field)

        #writing headers (field names)
        with open(file,'r',newline='') as csvinput:
            reader=csv.reader(csvinput)
            data=list(reader)
            no_lines=len(data)
        if no_lines ==0:
              writer.writeheader()
        # writing data rows
        writer.writerows([x])
    csvfile.close()
def reissue():
    s = {}
    b = {}
    st = []
    bk = []
    i=0
    sid=input("enter the college id")
    st=return_data(sid,sfile)
    if st=='name':
        print("you have to issue first")
        return
    else:
        for i in range(0, len(st)):
            s[sfield[i]] = st[i]
        bid=input("enter the book id")
        bk=return_data(bid,bfile)
        if bk=='name':
            print("no such book")
            return
        else:
            for i in range(0, len(bk)):
                b[bfield[i]] = bk[i]
            if s['b1']==bid:a= 1
            if s['b2']==bid:a= 2
            if s['b3']==bid:a= 3
            if a!=0:
                x = datetime.datetime.strptime(str(s['d'+str(a)+'_re']), '%Y-%m-%d')
                now = (datetime.datetime.now())
                p=(now.date()-x.date())
                p=p.days
                s['d' + str(a) + '_is'] = now.date()
                s['d' + str(a) + '_re'] = now.date() + datetime.timedelta(days=14)
                if p>0:
                    s['p'+str(a)]=p
                    print("penalty is : ",p , " rupees")
                delete_entry(sid,sfile)
                update(s,sfile,sfield)
            else:
                print("book is not issued")
def submit():
    s = {}
    b = {}
    st = []
    bk = []
    a = 0
    sid = input("enter the college id")
    st = return_data(sid, sfile)
    if st == 'name':
        print("you have to issue first")
        return
    else:
        for i in range(0, len(st)):
            s[sfield[i]] = st[i]
        bid = input("enter the book id")
        bk = return_data(bid, bfile)
        if bk == 'name':
            print("no such book")
            return
        else:
            for i in range(0, len(bk)):
                b[bfield[i]] = bk[i]
            b['b_status']=int(b['b_status'])+1
            if s['b1'] == bid: a = 1
            if s['b2'] == bid: a = 2
            if s['b3'] == bid: a = 3
            if a!=0:
                x = datetime.datetime.strptime(str(s['d' + str(a) + '_re']), '%Y-%m-%d')
                now = (datetime.datetime.now())
                p = (now.date() - x.date())
                p = p.days
                s['cards']=int(s['cards'])+1
                s['p' + str(a)] = ''
                s['b' + str(a)] = ''
                s['d' + str(a) + '_is'] = ''
                s['d' + str(a) + '_re'] = ''
                if p > 0:
                    print("penalty is : ", p, " rupees")
                delete_entry(sid, sfile)
                delete_entry(bid,bfile)
                update(s, sfile, sfield)
                update(b,bfile,bfield)
            else:
                print("book is not issued")
choice=1
print("[1] WANT TO issue")
print("[2] WANT TO reissue")
print("[3] WANT TO SUBMIT")
print("[4] EXIT")
myclient={}
while choice!=0:
    while True:
        try:
            choice = int(input("\nENTER THE CHOICE : "))
            break
        except:
            print("\n\tINVALID INPUT..")
    if choice==1:
        issue()
    elif choice==2:
        reissue()
    elif choice==3:
        submit()
    elif choice==4:
        choice=0
