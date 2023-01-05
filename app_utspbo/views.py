from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from app_utspbo.forms import formJurnal, formpeta
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from utspbo.serializers import koorSerialzer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Di buat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        ctx = {
            'form' : form,
        }
    return render(request, 'signup.html',ctx)

@login_required(login_url=settings.LOGIN_URL)
def RelawanPage(request):
    return render(request, 'halamandetail.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    
    return render (request,'signup.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url=settings.LOGIN_URL)
def halamanjurnal(request):
        return render(request, "halamanjurnal.html")
@login_required(login_url=settings.LOGIN_URL)
def halamandetail(request):
        return render(request, "halamandetail.html")
@login_required(login_url=settings.LOGIN_URL)
def halamanjurnal(request):
    homes = home.objects.all()
    koors = koor.objects.all()
    data = {
        'Title' : "Data Jurnal",
        'Heading' : "DATA JURNAL IKAN TAWAR",
        'homes' : homes,
        'koors' : koors,
    }
    return render(request, 'halamanjurnal.html' , data)
@login_required(login_url=settings.LOGIN_URL)
@api_view(['GET'])
def koorApi(request,*args, **kwargs):
    koors = koor.objects.all()
    data = koorSerialzer(koors, many=True).data
    return Response(data)
@login_required(login_url=settings.LOGIN_URL)
def detail(request, id):
    Jurnalikantawar = Jurnal.objects.get(pk=id)
    data = {
        'Title' : "DATA JURNAL IKAN TAWAR",
        'Jurnal' : Jurnalikantawar,
    }
    return render(request, 'detail.html', data)
@login_required(login_url=settings.LOGIN_URL)
def halamandetail(request):
    Jurnals = Jurnal.objects.all()
    data = {
        'Title' : "Data Jurnal",
        'Heading' : "DATA JURNAL IKAN TAWAR",
        'Jurnals' : Jurnals,
    }
    return render(request, 'halamandetail.html' , data)

@login_required(login_url=settings.LOGIN_URL)
def tambahjurnal(request, *args, **kwargs):
    if request.method == 'POST':
        form = formJurnal(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = formJurnal()
        pesan = "Data Berhasil Ditambahkan!"
        judul = 'Tambah Data Jurnal'
        ctx = {
            'title' : judul,
            'heading' : judul,
            'form' : form,
            'pesan' : pesan
        }
        return render(request, 'tambahjurnal.html', ctx)
    else:
        form = formJurnal()
        ctx = {
            'form' : form,
        }
        print(form.errors)    
        return render(request, 'tambahjurnal.html', ctx)
@login_required(login_url=settings.LOGIN_URL)
def tambahpeta(request, *args, **kwargs):
    if request.method == 'POST':
        form = formpeta(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = formpeta()
        pesan = "Data Berhasil Ditambahkan!"
        ctx = {
            'form' : form,
            'pesan' : pesan
        }
        return render(request, 'tambahpeta.html', ctx)
    else:
        form = formpeta()
        ctx = {
            'form' : form,
        }
        print(form.errors)    
        return render(request, 'tambahpeta.html', ctx)
@login_required(login_url=settings.LOGIN_URL)
def updatejurnal(request, id_home):
    homes = home.objects.get(id = id_home)
    judul = "Update Data Jurnal"
    template = "updatejurnal.html"
    if request.POST:
        form = formJurnal(request.POST,request.FILES, instance=homes)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate!"
            data ={
            'title' : judul,
            'heading' : judul,
            'pesan' : pesan,
            'homes' : homes,
        }
        return render(request, template, data)
    else:
        form = formJurnal( request.FILES,instance=homes)
        data ={
        'title' : judul,
        'heading' : judul,
        'form' : form,
        'homes' : homes,
    }
    return render(request, template, data)
@login_required(login_url=settings.LOGIN_URL)
def deletejurnal(request, id_home):
    homes = home.objects.get(id = id_home)
    homes.delete()

    return redirect('/halamanjurnal/')

# Create your views here.
