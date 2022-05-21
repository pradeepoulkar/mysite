from django.shortcuts import render
from django.shortcuts import redirect
from . import views


# Create your views here.
# def home_view(request):
#     print(request.GET)
#     return render(request, "home.html")


def index_redirect(request):
    return redirect('/contact/')
