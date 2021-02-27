from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "comedk.html")

collegeList = ["R.V.College","BMS College of Engineering","Ms Ramaiah","SJCE College of Engineering",
                "Bangalore Institute of Technology","Sir M.Visvesvaraya Institute of Technology",
                "Dayananda Sagar College of Engineering","The National Institute of Engineering, Mysore",
                "RNS Institute of Technology","BNM Institute of Technology","JSS Academy Bangalore",
                "NITTE Meenakshi Institute of Technology","NMAM Institute of Technology"]

collegeDictCse = {"R.V.College":450,"BMS College of Engineering":1000,"Ms Ramaiah":1100,"SJCE College of Engineering":2500,"Bangalore Institute of Technology":2700
                ,"Sir M.Visvesvaraya Institute of Technology":3300,"Dayananda Sagar College of Engineering":4300,"The National Institute of Engineering, Mysore":4500
                ,"RNS Institute of Technology":5800,"BNM Institute of Technology":7700,"JSS Academy Bangalore":9000,"CMR Institute of Technology":10000,
                "NITTE Meenakshi Institute of Technology":11000,"NMAM Institute of Technology":21800}

collegeDictECE = {"R.V.College":918,"BMS College of Engineering":1500,"Ms Ramaiah":2000,"Bangalore Institute of Technology":5300
                ,"SJCE College of Engineering":6000,"Sir M.Visvesvaraya Institute of Technology":6100,"The National Institute of Engineering, Mysore":7000,
                "Dayananda Sagar College of Engineering":8300,"RNS Institute of Technology":12200,"BNM Institute of Technology":15000,
                "JSS Academy Bangalore":17000,"NITTE Meenakshi Institute of Technology":19000,"CMR Institute of Technology":23000,
                "NMAM Institute of Technology":30000}


def checkCollegeCSE(request):
    for x in collegeDictCse:
        if int(request.GET["rank"]) < collegeDictCse[x]:
            return render(request,"comedkResult.html" ,{"result":collegeList[collegeList.index(x):]})
    return render(request,"comedkNoResult.html",{"result":"No colleges found"})

def checkCollegeECE(request):
    for x in collegeDictECE:
        if int(request.GET["rank"]) < collegeDictECE[x]:
            return render(request,"comedkResult.html" ,{"result":collegeList[collegeList.index(x):]})
    return render(request,"comedkNoResult.html",{"result":"No colleges found"})
    