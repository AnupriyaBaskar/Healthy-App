from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import mysql.connector as sql




def home(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['confirmpassword']
       
        na=name
        em1=email
        pwd=password
        pwd1=password2
        

       
        



        if password==password2:
            con=sql.connect(host="localhost",user="root",passwd='anupriya17',port="3308",database="healthyapp")
            cursor=con.cursor()
            cursor.execute("insert into command(name,email,password,password2) values('{}','{}','{}','{}')".format(na,em1,pwd,pwd1))
            cursor.execute('commit')
            con.close

            dict1={'name':name}
            html_template='emessage.html'
            html_message=render_to_string(html_template,context=dict1)
            subject='Welcome to Healthybowl'
            email_from = settings.EMAIL_HOST_USER
            recipient_list=[email]
            message= EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            return redirect('form')

            
        
        else:
            messages.warning(request,'password mismatching')
            return redirect('Home')
    else:
         return render(request,'nutriapp.html')
    
def video(request):
    return render(request,"video.html")

def client(request):
    if request.method=='POST':  
             name1=request.POST['name1']
             email1=request.POST['email1']
             password1=request.POST['password1']
             password21=request.POST['confirmpassword1']

             na1=name1
             em11=email1
             pwd12=password1
             pwd11=password21
             if password1==password21:
              con=sql.connect(host="localhost",user="root",passwd='anupriya17',port="3308",database="healthyapp")
              cursor=con.cursor()
              cursor.execute("insert into users4(name1,email1,password1,password21) values('{}','{}','{}','{}')".format(na1,em11,pwd12,pwd11))
              cursor.execute('commit')
              con.close()
              dict1={'email':email1}
              html_template='emessage2.html'
              html_message=render_to_string(html_template,context=dict1)
              subject='Welcome to Healthybowl'
              email_from = settings.EMAIL_HOST_USER
              recipient_list=[email1]
              message= EmailMessage(subject, html_message,
                                   email_from, recipient_list)
             message.content_subtype = 'html'
             message.send()

             return render(request,'clientform.html')
    else:
            return render(request,'nutriapp.html')


   


def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        em1=email
        pwd1=password
        con=sql.connect(host="localhost",user="root",passwd='anupriya17',port="3308",database="healthyapp")
        cursor=con.cursor()
        cursor.execute("select * from command where email='{}' and password='{}'".format(em1,pwd1))
        row=cursor.fetchone()
        if row==None:
            return render(request,'error.html')
        else:
            con=sql.connect(host="localhost",user="root",passwd='anupriya17',port="3308",database="healthyapp")
            cursor=con.cursor()
            cursor.execute("select * from dietplan6 where email='"+email+"'")
            test1=dictfetchall(cursor)
            print(test1)
            context={'test1':test1}
            return render(request,'result1.html',context)
           
    return render(request,'nutriapp.html')



def login2(request):
   if request.method=='POST':
        email1=request.POST['email1']
        password1=request.POST['password1']
       
        em4=email1
        pwd4=password1
    
   
        con=sql.connect(host="localhost",user="root",passwd='anupriya17',port="3308",database="healthyapp")
        cursor=con.cursor()
        cursor.execute("select * from users6 where email1='{}' and password1='{}'".format(em4,pwd4))
        row=cursor.fetchone()
        if row==None:
            return render(request,'error.html')
        else:
           return render(request,'client.html') 
   
     
   return render(request,'nutriapp.html')
         
   
        
    


    
def form(request):
    return render(request,'form.html')
def aboutus(request):
    return render(request,'aboutus.html')
def important(request):
         if request.method=="POST": 
            email2=request.POST['email']
            date=request.POST['age']
            gender=request.POST['gender']
            worker=request.POST['worker']
            height=request.POST['height']
            weight=request.POST['weight']
            bmi=request.POST['bmi']
            disease=request.POST['disease']
            allergy=request.POST['allergy']
            yes=request.POST['yes']
            em=email2
            d=date
            ge=gender
            wo=worker
            he1=height
            we=weight
            bm=bmi
            di=disease
            all=allergy
            ye=yes
            if email2==email2:
                con=sql.connect(host='localhost',user='root',passwd='anupriya17',port='3308',database='healthyapp')
                cursor=con.cursor()
                cursor.execute("insert into commandform(email2,date,gender,worker,height,weight,bmi,disease,allergy,yes) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(em,d,ge,wo,he1,we,bm,di,all,ye))
                cursor.execute('commit')
                con.close()
                
                dict1={'email':email2}
                html_template='emessage4.html'
                html_message=render_to_string(html_template,context=dict1)
                subject='Welcome to Healthybowl'
                email_from = settings.EMAIL_HOST_USER
                recipient_list=[email2]
                message= EmailMessage(subject, html_message,
                                   email_from, recipient_list)
                message.content_subtype = 'html'
                message.send()
                return redirect('final')
            else:
              return redirect('error')
         else:
          return render(request,"final.html")

def tips(request):
    return render(request,'tips.html')

def error(request):
    return render(request,'error.html')

def final(request):
    return render(request,'final.html')


def diet3(request):
    if request.method=='POST':
        email1=request.POST['email']
        Diet=request.POST['diet']
        Age=request.POST['age']
        lifestyle=request.POST['lifestyle']
        un=email1
        di=Diet
        ag=Age
        lie=lifestyle
        con=sql.connect(host='localhost',user='root',passwd='anupriya17',port='3308',database='healthyapp')
        cursor=con.cursor()
        cursor.execute("insert into dietplan6(email,diet,age,lifestyle) values('{}','{}','{}','{}')".format(un,di,ag,lie))
        cursor.execute('commit')
        con.close()
        return render(request,'nutriapp.html')
   
        


    
   


def normal(request):
    return render(request,"normal.html")

def weightloss(request):
    return render(request,"weightloss.html")

def weightgain(request):
    return render(request,"weightgain.html")

def diabetic(request):
    return render(request,"diabetic.html")

def videochol(request):
    return render(request,"videochol.html")


def video2dia(request):
    return render(request,"video2dia.html")


def high(request):
    return render(request,"High.html")


def videoweightgai(request):
    return render(request,"videoweightgai.html")

def videoweightloss(request):
    return render(request,"videoweightloss.html")


def pages(request):
    if request.method=='POST':
        email1=request.POST['email']
        Diet=request.POST['diet']
        Age=request.POST['age']
        lifestyle=request.POST['lifestyle']
        di=Diet
        ag=int(Age)
        lifestyle=lifestyle
        em1=email1
        if di=='Weight loss' and ag>20 and lifestyle=='Working':
            return render(request,"weightloss.html")
        elif di=='Weight loss' and ag>30 and lifestyle=='Working':
            return render(request,"weightloss.html")
        elif di=='Weight loss' and ag>40 and lifestyle=='Working':
            return render(request,"weightloss.html")
        elif di=='Weight loss' and ag>20 and lifestyle=='House wife':
            return render(request,"weightloss.html")
        elif di=='Weight loss' and ag>30 and lifestyle=='House wife':
            return render(request,"weightloss.html")
        elif di=='Weight loss' and ag>40  and lifestyle=='House wife':
            return render(request,"weightloss.html")
        elif di=='Weight loss' and ag>20 and lifestyle=='College':
            return render(request,"weightloss.html")
        elif di=='Weight loss' and ag>30 and lifestyle=='College':
            return render(request,"weightloss.html")
        elif di=='Weight loss' and ag>40 and lifestyle=='College':
            return render(request,"weightloss.html")
        


        elif di=='Normal' and ag>20 and lifestyle=='Working':
            return render(request,"normal.html")
        elif di=='Normal' and ag>30  and lifestyle=='Working':
            return render(request,"normal.html")
        elif di=='Normal' and ag>40 and lifestyle=='Working':
            return render(request,"normal.html")
        elif di=='Normal' and ag>20 and lifestyle=='College':
            return render(request,"normal.html")
        elif di=='Normal' and ag>30 and lifestyle=='College':
            return render(request,"normal.html")
        elif di=='Normal' and ag>40 and lifestyle=='College':
            return render(request,"normal.html")
        elif di=='Normal' and ag>20 and lifestyle=='House wife':
            return render(request,"normal.html")
        elif di=='Normal' and ag>30 and lifestyle=='House wife':
            return render(request,"normal.html")
        elif di=='Normal' and ag>40 and lifestyle=='House wife':
            return render(request,"normal.html")
        

        elif di=='Type 2 diabetic' and ag>20 and lifestyle=='Working':
            return render(request,"diabetic.html")
        elif di=='Type 2 diabetic' and ag>30 and lifestyle=='Working':
            return render(request,"diabetic2.html")
        elif di=='Type 2 diabetic' and ag>40 and lifestyle=='Working':
            return render(request,"diabetic.html")
        elif di=='Type 2 diabetic' and ag>20 and lifestyle=='College':
            return render(request,"diabetic.html")
        elif di=='Type 2 diabetic' and ag>30 and lifestyle=='College':
            return render(request,"diabetic.html")
        elif di=='Type 2 diabetic' and ag>40 and lifestyle=='College':
            return render(request,"diabetic.html")
        elif di=='Type 2 diabetic' and ag>20 and lifestyle=='House wife':
            return render(request,"diabetic.html")
        elif di=='Type 2 diabetic' and ag>30 and lifestyle=='House wife':
            return render(request,"diabetic.html")
        elif di=='Type 2 diabetic' and ag>40 and lifestyle=='House wife':
            return render(request,"diabetic.html")
        


        elif di=='Weight gain' and ag>20  and lifestyle=='Working':
            return render(request,"weightgain.html")
        elif di=='Weight gain' and ag>30 and lifestyle=='Working':
            return render(request,"weightgain.html")
        elif di=='Weight gain' and ag>40 and lifestyle=='Working':
            return render(request,"weightgain.html")
        elif di=='Weight gain' and ag>20 and lifestyle=='College':
            return render(request,"weightgain.html")
        elif di=='Weight gain' and ag>30 and lifestyle=='College':
            return render(request,"weightgain.html")
        elif di=='Weight gain' and ag>40 and lifestyle=='College':
            return render(request,"weightgain.html")
        elif di=='Weight gain' and ag>20 and lifestyle=='House wife':
            return render(request,"weightgain.html")
        elif di=='Weight gain' and ag>30 and lifestyle=='House wife':
            return render(request,"weightgain.html")
        elif di=='Weight gain' and ag>40 and lifestyle=='House wife':
            return render(request,"weightgain.html")
        


        elif di=='High cholesterol' and ag>20  and lifestyle=='Working':
            return render(request,"High.html")
        elif di=='High cholesterol'and ag>30 and lifestyle=='Working':
            return render(request,"High.html")
        elif di=='High cholesterol' and ag>40 and lifestyle=='Working':
            return render(request,"High.html")
        elif di=='High cholesterol' and ag>20 and lifestyle=='College':
            return render(request,"High.html")
        elif di=='High cholesterol'and ag>30 and lifestyle=='College':
            return render(request,"High.html")
        elif di=='High cholesterol' and ag>40 and lifestyle=='College':
            return render(request,"High.html")
        elif di=='High cholesterol' and ag>20 and lifestyle=='House wife':
            return render(request,"High.html")
        elif di=='High cholesterol' and ag>30 and lifestyle=='House wife':
            return render(request,"High.html")
        elif di=='High cholesterol' and ag>40 and lifestyle=='House wife':
            return render(request,"High.html")
        
        else:
            return render(request,"nutriapp.html")

        
def dictfetchall(cursor):
    """0
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]





def clientdetails(request):
    if request.method=='POST':
        email=request.POST['email']
        dietwanted=request.POST['want']
        age=request.POST['group']
        people=request.POST['number']
        time=request.POST['time']
        unm=email
        dw=dietwanted
        agw=age
        po=people
        tm=time
        con=sql.connect(host='localhost',user='root',passwd='anupriya17',port='3308',database='healthyapp')
        cursor=con.cursor()
        cursor.execute("insert into usersdetails7(email,dietwanted,age,people,timing) values('{}','{}','{}','{}','{}')".format(unm,dw,agw,po,tm))
        cursor.execute('commit')
        con.close()
        return redirect('Home')
    else:
            return render(request,'nutriapp.html')

def update(request):
           if request.method=='POST':
               email=request.POST['email']
               diet= request.POST['diet']
               age=request.POST['age']
               lifestyle=request.POST['lifestyle']
               em=email
               di=diet
               aggg=age
               life=lifestyle
               con=sql.connect(host='localhost',user='root',passwd='anupriya17',port='3308',database='healthyapp')
               cursor=con.cursor()
               cursor.execute("update dietplan6 set diet='{}',age='{}',lifestyle='{}' where email='{}'".format(di,aggg,life,em))
               cursor.execute('commit')
               con.close()
               return render(request,"nutriapp.html")
           else:
               return render(request,"error.html")
               

   
# Create your views here.
