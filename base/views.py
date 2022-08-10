from django.shortcuts import render
from django.http import HttpResponse


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
    context =  {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

