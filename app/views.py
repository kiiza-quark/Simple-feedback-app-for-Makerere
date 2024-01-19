from django.shortcuts import render, redirect
from .models import Feedback
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth import get_user_model, login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# User = get_user_model()

def index(request):
    return render(request, 'index.html')

def send_feedback(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        regno = request.POST.get('regno')
        stno = request.POST.get('stno')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        message = request.POST.get('message')

        feedback = Feedback(
            name=fullname,
            email=email,
            registration_number=regno,
            student_number=stno,
            dob=dob,
            address=address,
            message=message
        )
        feedback.save()

        return render(request, 'sent.html')

    return render(request, 'send.html')

@login_required(login_url="")
def view_feedback(request):
    feedback_data=Feedback.objects.all()
    count = Feedback.objects.all().count()
    admins = User.objects.all().count()
    total_students = Feedback.objects.values('student_number').distinct().count()
    
    return render(request, 'admin.html', {"feedback_data": feedback_data, 
                                          "count":count, 
                                          "total_students": total_students,
                                          "total_admins":admins,})



def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'The entered username does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('view_feedback')
        else:
            messages.error(request, 'Username or Password does not exist!')

    context = {}

    return render(request, 'index.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')


def register_user(request):
    err = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")

        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required")

        if password1 != password2:
            messages.error(request, "Passwords are not matching")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")

        user = User.objects.create_user(username=username, email=email, password=password1)

        login(request, user)

        return redirect('index')
    
    return render(request, 'index.html')
