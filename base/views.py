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
    return render(request,'home.html',{'rooms':rooms})

def room(request):
    return render(request,'room.html')