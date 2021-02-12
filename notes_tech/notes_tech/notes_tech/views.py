from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, logout, login

def index(request):
    return render(request,'login.html')

def home1(request):
    return render(request,"home.html")

def feedback(request):
    return render(request,"feedback.html")

def sub3rd(request):
    return render(request,"subject_page.html")

def sub1st(request):
    return render(request,"sub_1st.html")

def sub2nd(request):
    return render(request,"sub_2nd.html")

def b1st(request):
    return render(request,"1st_books.html")

def n1st(request):
    return render(request,"1st_notes.html")

def v1st(request):
    return render(request,"1st_vdos.html")

def p1st(request):
    return render(request,"1st_papers.html")

def profile(request):
    return render(request,"profile.html")

def register(request):
    data={}
    if request.method == 'POST':
        # get the post parameters
        name=request.POST['name1']
        password=request.POST['password1']
        email=request.POST['email']
        contact=request.POST['contact']
        gender = request.POST['gender']
        username = request.POST['user']
        dob = request.POST['dob']
        data = {"first":name,"second":username,"third":email,'fourth':password,'fifth':dob,'sixth':contact,'seventh':gender}

        # check for erroneous input
        # username under 10 characters
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")
            return redirect('/')
        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers.")
            return redirect('/')

        # create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = name
        myuser.save()
        messages.success(request, 'Your Notes Tech account has been successfully created !!')
        # return redirect('profile', data)
        return render(request, 'profile.html', data)

    else:
        return HttpResponse('404 - Not Found')

def home(request):
    if request.method == 'POST':
        # get the post parameters
        loginpassword = request.POST['password2']
        loginusername = request.POST['loginuser']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in !!')
            return redirect('home1')
        else:
            messages.error(request, 'Invalid Credentials, Please Try Again !!')
            return redirect('/')

    return HttpResponse('404 - Not Found')

def userlogout(request):
    if request.method == 'GET':
        logout(request)
        messages.success(request, 'Successfully logged out !!')
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')




