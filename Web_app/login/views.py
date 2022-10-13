
from multiprocessing import context

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import auth,User
from .forms import CreatUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def userpage(request):
  if request.user.is_authenticated:
   return render(request,'User.html')
  return redirect('loginpage')
  

def loginpage(request):
  if request.user.is_superuser:
    return redirect('adminpanel')
  
  if request.user.is_authenticated:
    return redirect('userpage')
  
  if request.method=='POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request,username=username,password=password)

    if user is not None:
      if user.is_superuser is False:
        login(request,user)
        return redirect('userpage')
      else:
        return redirect('adminlogin')
  return render(request,'Login.html')


def signup(request):
  if request.method =='POST':
    form = CreatUserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'hi {username}, your account was created succsefully')
      return redirect('loginpage')
  else:
   form = CreatUserForm()
  return render(request, 'SignUp.html',{'form':form})


def adminpanel(request):
  if request.user.is_superuser:
    person = User.objects.all()
    return render(request, "admin.html" ,{'person':person})
  return redirect( "adminlogin")


def logout1(request):
  logout(request)
  return redirect('loginpage')


def adminlogin(request):
  if request.user.is_superuser:
    return redirect('adminpanel')
  if request.method=='POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request,username=username,password=password)
    if user is not None:
      if user.is_superuser is True:
        login(request,user)
        return redirect('adminpanel')
  return render(request,'adminlogin.html')


def adminlogout(request):
  logout(request)
  return redirect('adminlogin')



def userform(request,id=0):
    form = CreatUserForm()
    if request.method =='GET':
      if id==0:
        form = CreatUserForm()

      else:
        user = User.objects.get(pk=id)
        form = CreatUserForm(instance=user)
      return render(request, "adduser.html",{'form':form})
    else:
      if id == 0:
        form = CreatUserForm(request.POST)
      else:
        user = User.objects.get(pk=id)
        form = CreatUserForm(request.POST,instance=user)
      if form.is_valid():
         form.save()
      return redirect('adminlogin')
    
    
    
def user_delete(request,id):
  user = User.objects.get(pk=id)
  user.delete()


  return redirect ('adminpanel') 
def user_list(request):
  return

def search(request):
  return HttpResponse('Search')