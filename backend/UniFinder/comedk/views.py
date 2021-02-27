from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello World")

collegeList = ["R.V.College","BMS College of Engineering","Ms Ramaiah","SJCE College of Engineering",
                "Bangalore Institute of Technology","Sir M.Visvesvaraya Institute of Technology",
                "Dayananda Sagar College of Engineering","The National Institute of Engineering, Mysore",
                "RNS Institute of Technology","BNM Institute of Technology","JSS Academy Bangalore"]

collegeDictCse = {"R.V.College":450,"BMS College of Engineering":1000,"Ms Ramaiah":1100,"SJCE College of Engineering":2500,"Bangalore Institute of Technology":2700
                ,"Sir M.Visvesvaraya Institute of Technology":3300,"Dayananda Sagar College of Engineering":4300,"The National Institute of Engineering, Mysore":4500
                ,"RNS Institute of Technology":5800,"BNM Institute of Technology":7700,"JSS Academy Bangalore":9000,"CMR Institute of Technology":10000}

def checkCollegeCSE(rank):
    for x in collegeDictCse:
        if rank < collegeDictCse[x]:
            return collegeList[collegeList.index(x):]

def checkCollegeECE(rank):
    pass
    