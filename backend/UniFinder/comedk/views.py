from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "comedk.html")

collegeDict = {"R.V.College":[450,918],"BMS College of Engineering":[1000,1500],"Ms Ramaiah":[1100,2000],"SJCE College of Engineering":[2500,6000],"Bangalore Institute of Technology":[2700,5300]
                ,"Sir M.Visvesvaraya Institute of Technology":[3300,6100],"Dayananda Sagar College of Engineering":[4300,8300],"The National Institute of Engineering, Mysore":[4500,7000]
                ,"RNS Institute of Technology":[5800,12200],"BNM Institute of Technology":[7700,15000],"JSS Academy Bangalore":[9000,17000],"CMR Institute of Technology":[10000,23000],
                "NITTE Meenakshi Institute of Technology":[11000,19000],"NMAM Institute of Technology":[21800,30000]}

def checkCollegeCSE(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][0]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList})
    return render(request,"Result.html",{"result":"No colleges found"})

def checkCollegeECE(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][1]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList})
    return render(request,"NoResult.html",{"result":"No colleges found"})