from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm


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
def home(request):
    rooms = Room.objects.all()
    context =  {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk) 
    if request.method == 'POST':
        print(room)
        room.delete()
        return redirect('home') 
    return render(request, 'base/delete.html', {'obj': room})


