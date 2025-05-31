from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .models import Student
from .forms import StudentForm,changedata
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        student=Student.objects.all()
        return render(request,'list_student.html',{'student': student})
    else:
        return redirect('login')

def Edit_Student(request,id):
    if request.user.is_authenticated:
        student=Student.objects.get(pk=id)
        form=StudentForm(instance=student)
        if request.method =="POST":
            form=StudentForm(request.POST,instance=student)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form=StudentForm(instance=student)
        return render(request,'edit_student.html',{'form': form})
    else:
        return redirect('login')

def Add_Student(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = StudentForm()
        return render(request, 'add_student.html', {'form': form})
    else:
        return redirect('login')    

def deletedata(request ,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            student=Student.objects.get(pk=id)
            student.delete()
            return HttpResponseRedirect("/")
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = changedata(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = changedata(instance=request.user)
            
        return render(request, 'profile.html', {'form': form, 'user': request.user})
    else:
        return redirect('login')


def Register(request):
    if not request.user.is_authenticated:
        if request.method=="POST":  
            form=RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form=RegisterForm()
        return render(request,'register.html',{'form':form})
    else:
        return redirect('profile')
    
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':   
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect ('profile')
        else:
            form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')

def passwchange(request):
    if request.user.is_authenticated:
        if request.method=='POST':  
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user) 
        return render(request,'passwordchange.html',{'form':form})
    else:
        return redirect('login')

def passwordchange(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'passwordchangee.html',{'form':form})
    else:
        return redirect('login')

