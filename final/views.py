from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
#for django forms

#models.py form
from .forms import createuser

#flash message
from django.contrib import messages

#for aunthentication
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage, send_mail
from final import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes

#email 
from django.conf import settings
 #for contact data
# for authentication


def home(request):
     return render(request,"home.html")
def foreign(request):
     return render(request,"foreign.html")
def mf(request):
     return render(request,"mf.html")
def bonds(request):
     return render(request,"bonds.html")
def etfs(request):
     return render(request,"etf.html")
def stocks(request):
     return render(request,"stocks.html")


# analysis
def funds(request):
     return render(request,"funds.html")
def gdp(request):
     return render(request,"gdp.html")

def importing(request):
     return render(request,"importing.html")
def inflation(request):
     return render(request,"inflation.html")
def intrest(request):
     return render(request,"intrest.html")
def manu(request):
     return render(request,"manu.html")


# government policy
def fis(request):
     return render(request,"fis.html")
def gov(request):
     return render(request,"gov.html")

def mon(request):
     return render(request,"mon.html")

# personal income
def literacy(request):
     return render(request,"literacy.html")
def per(request):
     return render(request,"per.html")

def ret(request):
     return render(request,"ret.html")
def sav(request):
     return render(request,"sav.html")
def tax(request):
     return render(request,"tax.html")
def loan(request):
     return render(request,"loan.html")

# news
def comp(request):
     return render(request,"comp.html")
def  eco(request):
     return render(request," eco.html")

def gov(request):
     return render(request,"gov.html")
def mar(request):
     return render(request,"mar.html")
def poli(request):
     return render(request,"poli.html")
def world(request):
     return render(request,"world.html")

# learning
def f(request):
     return render(request,"f.html")
def ic(request):
     return render(request,"ic.html")

def inc(request):
     return render(request,"in.html")
def tc(request):
     return render(request,"tc.html")

#contact

def contact(request):
     return render(request,"contact.html")

# for authentication



def homepage(request):
      return render(request,'homepage.html')
def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
         
        if pass1 != pass2:
         return HttpResponse("Your password and confirm password are not the same!!")
        else:
         myuser = user = User.objects.create_user(username = uname, email=email)
         myuser.set_password(pass1)
         myuser.save()

         # Welcome Email
         subject = "Welcome to FINANCE CASTLE - Devloped By ASHUTOSH SHUKLA!!"
         message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Finance Castle!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nASHUTOSH SHUKLA"        
         from_email = settings.EMAIL_HOST_USER
         to_list = [myuser.email]
         send_mail(subject, message, from_email, to_list, fail_silently=False)

         return redirect('login')

      

    return render (request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')

