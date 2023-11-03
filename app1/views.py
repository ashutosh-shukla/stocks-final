from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage, send_mail
from final import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes

def homepage(request):
      return render(request,'home.html')
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
         subject = "Welcome to Financial CAstle Created BY (ASHUTOSH SHUKLA)!!"
         message = "Hello " + myuser.first_name + "!! \n" + "Welcome to FINANCIAL CASTLE!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n ASHUTOSH SHUKLA"        
         from_email = settings.EMAIL_HOST_USER
         to_list = [myuser.email]
         send_mail(subject, message, from_email, to_list, fail_silently=True)

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