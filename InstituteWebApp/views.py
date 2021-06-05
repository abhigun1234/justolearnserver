from rest_framework.decorators import api_view
from django.shortcuts import render
from bson import json_util
import  json
from django.http import HttpResponse
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.RestaurentDb
    return db


@api_view(['GET', 'POST'])
def about(request):
    return render(request,'aboutus.html',{'titles':'hello','link':'http://youtube.com'})
@api_view(['GET', 'POST'])
def contactus(request):
    return render(request,'contact.html',{'titles':'hello','link':'http://youtube.com'})

@api_view(['GET', 'POST'])
def getMenu(request):

    db=get_db()
    result=db.menuDetails.find()
    mylist=[]
    print("result",result)
    for data in result:
        print("data",data)
        mylist.append(data)
    responseJson = json.loads(json_util.dumps(mylist))
    return HttpResponse(json.dumps(responseJson), content_type="application/json")