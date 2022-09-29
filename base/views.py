from pickle import NONE
from django.shortcuts import render

#for httpResponse
# from django.http import HttpResponse

rooms =[
    {'id':1,'name':'Lets Learn Python'},
    {'id':2,'name':'Lets Learn HTML'},
    {'id':3,'name':'Lets Learn CSS'}

]
# Create your views here.
def home(request):
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context = {'room':room}        
    return render(request,'base/room.html',context)