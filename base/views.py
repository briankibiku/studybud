from atexit import register
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import  Q
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.forms import UserCreationForm


rooms = [
    {'id': 1, 'name': 'Learn python'},
    {'id': 2, 'name': 'You DONT know JS'},
    {'id': 3, 'name': 'Time for c#'},
    {'id': 4, 'name': 'Time for C++'},
    {'id': 5, 'name': 'code complete'},
    {'id': 6, 'name': 'Learn Ruby now'},
    {'id': 7, 'name': 'Django on Steroids'},
]
# Create your views here.
def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration")

    return render(request, 'base/login_register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) | 
        Q(description__icontains=q)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context =  {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated successfully')
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk) 

    if request.user != room.host:
        return HttpResponse('You are not allowed here')
        
    if request.method == 'POST':
        room.delete()
        return redirect('home') 
    return render(request, 'base/delete.html', {'obj': room})
