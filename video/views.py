from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import Chat
import cv2
import smtplib, ssl
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User
# Create your views here.
import cv2
import numpy as np
import random
  
def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            return HttpResponseRedirect('waiting')
        return render(request,'index1.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login')


def sendMail(useremail, link):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "abhijeetnegi21@gmail.com"
    receiver_email = useremail
    password = "zhilrtqnhevxguco"
    message = f"""\
    Subject: Hi there
    Link: {link}
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def waiting(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            cap = cv2.VideoCapture(0)
            fgbg=cv2.createBackgroundSubtractorMOG2(300,400, False)
            m=0
            while(True):
                success, frame = cap.read()
                fgmask=fgbg.apply(frame)

                cv2.imshow("fgbg", fgmask)
                count=np.count_nonzero(fgmask)
                if count>5000:
                    print("xyz")
                    m+=1

                if m>=50:
                    cap.release()
                    cv2.destroyAllWindows()
                    
                    return HttpResponseRedirect('videocall')

                key=cv2.waitKey(1) & 0xff
                if key==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        return render(request,'waiting.html')

    else:
        return HttpResponseRedirect('/login')


def videocall(request):
    if request.user.is_authenticated:
        room=str(request.user)+str(random.randint(0, 9999))

        get_room = Chat.objects.filter(room_name=room)
        link=f"http://127.0.0.1:8000/video/{room}/join/"
        useremail=request.user.email
        print(useremail)
        sendMail(useremail, link)
        print("mail sent")
        print(f"link is {link}")
        if get_room:
            c = get_room[0]
            number = c.allowed_users
            if int(number) < 2:
                number = 2
                return redirect(f'/video/{room}/join/')
        else:
            create = Chat.objects.create(room_name=room,allowed_users=1)
            if create:
                return redirect(f'/video/{room}/created/')
        return render(request,'index1.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login')



def video(request,room,created):
    return render(request,'video.html',{'room':room,'created':created})

def signup(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,"User Successfully created")
            fm.save()
    else:
        fm=SignupForm()
    return render(request,'signup.html',{'form':fm})

def login_function(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:
            fm=LoginForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/')

def logout_function(request):
    logout(request)
    return HttpResponseRedirect('/login')

def room(request,room_name):
    if request.user.is_authenticated:
        return render(request,'chatroom.html',{
            'room_name': room_name,
        })
    else:
        return HttpResponseRedirect('/login')
    