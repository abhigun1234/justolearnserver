from django.shortcuts import render
import datetime
from  InstituteWebApp.DbHelper import DataBaseHelper
from bson import ObjectId
from bson.json_util import dumps
from bson.json_util import loads
from django.http import JsonResponse
from rest_framework.decorators import api_view
from bson import json_util
from django.core import serializers
from django.http import HttpResponse
import uuid
import  json
from django.shortcuts import render
# This view method handles the request for the root URL /
# See urls.py for the mapping.


@api_view(['GET', 'POST'])
def home(request):
    return render(request,'hello.html',{'titles':'hello','link':'http://youtube.com'})







@api_view(['GET', 'POST'])
def getStudentDetails(request):
    dbHelper = DataBaseHelper()
    db = dbHelper.get_db()
    studentList = dbHelper.getStudentDetails(db)
    # print(dumps(studentList))
    '''Dump
    loaded
    BSON
    to
    valid
    JSON
    string and reload
    it as dict'''
    responseJson = json.loads(json_util.dumps(studentList))
   # posts_serialized = serializers.serialize('json', responseJson)
    print(responseJson)
    return HttpResponse(json.dumps(responseJson), content_type="application/json")
#getMenu items from collection
@api_view(['GET', 'POST'])
def getMenuDetails(request):
    dbHelper = DataBaseHelper()
    db = dbHelper.get_db()
    menulist = dbHelper.getMenuDetails(db)
    # print(dumps(studentList))
    '''Dump
    loaded
    BSON
    to
    valid
    JSON
    string and reload
    it as dict'''
    responseJson = json.loads(json_util.dumps(menulist))
   # posts_serialized = serializers.serialize('json', responseJson)
    print(responseJson)
    return HttpResponse(json.dumps(responseJson), content_type="application/json")
@api_view(['GET', 'POST'])
def add_student(request):
    dbHelper=DataBaseHelper()
    db=dbHelper.get_db()
    studentdata=request.data
    name=studentdata['name']
    address=studentdata['address']
    phoneno = studentdata['phoneno']
    dbHelper.add_student(db,name,address,phoneno)
    print("studentdata",studentdata)
    #db = dbHelper.get_db()
    #studentList = dbHelper.getStudentDetails(db)
    # print(dumps(studentList))
    '''Dump
    loaded
    BSON
    to
    valid
    JSON
    string and reload
    it as dict'''
    #responseJson = json.loads(json_util.dumps(studentList))
   # posts_serialized = serializers.serialize('json', responseJson)
   # print(responseJson)
    return HttpResponse("saved on db")

##########################################
# add   menu api
#########################################
@api_view(['GET', 'POST'])
def add_menu(request):
    dbHelper=DataBaseHelper()
    db=dbHelper.get_db()
    menudata=request.data
    name=menudata['name']
    price=menudata['price']
    description = menudata['description']
    dbHelper.add_menu(db,name,price,description)
    print("menudata",menudata)
    # print(dumps(studentList))
    '''Dump
    loaded
    BSON
    to
    valid
    JSON
    string and reload
    it as dict'''
    return HttpResponse("saved on db")
##########################################
# add   menu api
#########################################
@api_view(['GET', 'POST'])
def  login(request):
    # dbHelper=DataBaseHelper()
    # db=dbHelper.get_db()
    # menudata=request.data
    # name=menudata['name']
    # price=menudata['price']
    # description = menudata['description']
    # dbHelper.add_menu(db,name,price,description)
    # print("menudata",menudata)
    # print(dumps(studentList))

    # data=uuid.uuid4()
    # print(data)

    responseJson = json.loads(json_util.dumps({"access_token":"01047b8060e34c38ac32aea2e0bd7f65"}))
    # posts_serialized = serializers.serialize('json', responseJson)
    print(responseJson)
    return HttpResponse(json.dumps(responseJson), content_type="application/json")
@api_view(['GET', 'POST'])
def getFacultyDetails(request):
    dbHelper = DataBaseHelper()
    db = dbHelper.get_db()
    facultylist = dbHelper.getFacultyDetails(db)
    # print(dumps(studentList))
    '''Dump
    loaded
    BSON
    to
    valid
    JSON
    string and reload
    it as dict'''
    responseJson = json.loads(json_util.dumps(facultylist))
   # posts_serialized = serializers.serialize('json', responseJson)
    print(responseJson)
    return HttpResponse(json.dumps(responseJson), content_type="application/json")
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)