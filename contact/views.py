from django.shortcuts import render
from .forms import FormContactForm
import mysql.connector
from django.shortcuts import render, redirect, HttpResponse
from .models import Member
from .forms import FormContactForm
from .forms import UserForm

def validate(request):
   if request.method == 'POST':
      username= request.POST["user"]
      password = request.POST["pass"]
      dict = {
         'username': username,
         'password': password
      }
      return render(request, 'validate.html', dict)


from .models import Details


def home_view(request):
    # print(request.GET)
    # print(request.GET.get('user'))
    error_message = None
    if request.method == 'POST':
        userna = request.POST['user']
        passwo = request.POST['pass']
        error_message=None
        if (not  userna):
            error_message="first name Required"
        elif len(userna)<4:
            error_message="first name must be 4 char long"
        else:
          obj = Details()
          obj.username = userna
          obj.password = passwo
          obj.save()
          return render(request, 'homev_view.html')


    #     context = {
    #         'data': data,
    #     }
    # from django.core import serializers
    data = Details.objects.all()

    return render(request, 'homev_view.html',{'error': error_message})

def showform(request):

    form = FormContactForm(request.POST)
    if  form.is_valid():
        form.save()
    data={
        'data1':"data2"
      }

    # context = {'form': form}

    return render(request, 'contactform1.html', {'form': form})

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        member = Member(username=request.POST['username'], password=request.POST['password'],
                        firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        if Member.objects.filter(username=username).count() > 0:
            return HttpResponse('Username already exists.');
        else:
            member.save()
            return redirect('ind/')
    else:
        return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def home(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            request.session['member'] =request.POST['username']
            if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
                member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
                member=request.POST['username']

                if 'member' in request.session:
                    member= request.session['member']
                    current_user = request.session['member']
                    print("member    ", member)

            return render(request, 'home.html', {'member': member,'current_user': current_user})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)


def logout(request):
    try:
        del request.session['member']
    except:
        return redirect('login')
    return redirect('login')


def home_viewvalidate(request):
 if 'member' in request.session:
   # cheking the request
   if request.method == 'POST':

      # passing the form data to LoginForm
      user_details = UserForm(request.POST)

      # validating the user_details with is_valid() method
      if user_details.is_valid():

         # writing data to the database
         user_details.save()

         # redirect to another page with success message
         return HttpResponse("Data submitted successfully")

      else:

         # redirect back to the user page with errors
          return render(request, 'validation.html', {'form':user_details})
   else:

         form = UserForm(None)
         return render(request, 'validation.html', {'form':form})