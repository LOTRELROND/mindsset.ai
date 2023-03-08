from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import CustomUser
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
import ssl
import smtplib
from django.contrib import messages
from core.models import Visiter

# Create your views here.

def register(request):
    if request.method == 'POST':
       
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]

        if password and confirm and password != confirm:
            raise ValueError("Parolalar Eşleşmiyor")

        newUser = CustomUser(email =email)
        newUser.set_password(password)

        newUser.save()
        
        new = Visiter.objects.create(user=newUser, username=email)
        new.save()

        current_site = get_current_site(request)
        email_body = render_to_string('activate.html', {
            'newUser': newUser,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(newUser.pk)),
            'token': generate_token.make_token(newUser)
        })


        email= EmailMultiAlternatives(
            'Activate your account',email_body,
            'mehmetkemalkayam@gmail.com',
            [newUser.email]
        )

        email.content_subtype = 'html'


        email.send()

        messages.success(request, "Hesabınız oluşturuldu. Lütfen mail adresinizi onaylayın.")
        return redirect("login")
    context = {}

    return render(request,"register.html",context)
  
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
        #if request.method == 'POST':
            
            email = request.POST['email']
            password = request.POST['password']

            

            CustomUser = authenticate(email = email,password = password)



            if CustomUser is None:
                messages.info(request, "Kullanıcı adı veya şifre hatalı")
                return render(request,"login.html",context)

            if not CustomUser.is_email_verified:
                messages.info(request, "E-postanızı doğrulamadınız.")
                return render(request, 'login.html',context)

            login(request,CustomUser)
            return redirect("index")
    return render(request,"login.html",context)

@login_required
def logoutUser(request):
    logout(request)
    return redirect('index')

def activate(request,uidb64,token):

    #try except bloğunu kaldırdım 
    uid = force_str(urlsafe_base64_decode(uidb64))
    newUser = CustomUser.objects.get(pk=uid)

    #############################################################
    if newUser and generate_token.check_token(newUser,token):
        newUser.is_email_verified = True

        newUser.save()
        return redirect(reverse('login'))
    return render(request, 'activatefail.html', {'newUser': newUser})
