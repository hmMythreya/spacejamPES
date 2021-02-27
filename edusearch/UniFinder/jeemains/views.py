from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"jeemains.html")

collegeDict = {"NIT Warangal":[2341,2919,10209,8152],"NIT Surathkal":[3181,5608,11788,6801],"MNIT Jaipur":[3831,7868,11426,9179],"MNIT Allahabad":[4051,7128,11145,8790],
                "NIT Kurukshetra":[6170,12067,18115,16273],"NIT Rourkela":[9420,12009,20304,19168],"NIT Calicut":[10222,14769,20480,18966],
                "NIT Durgapur":[12095,16098,22753,19325],"NIT Silchar":[23882,40841,49215,56958]}

def checkCollegeCSE(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][0]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList,"course":"CSE"})
    return render(request,"NoResult.html",{"result":"No colleges found"})

def checkCollegeECE(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][1]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList,"course":"ECE"})
    return render(request,"NoResult.html",{"result":"No colleges found"})
    
def checkCollegeME(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][2]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList,"course":"ME"})
    return render(request,"NoResult.html",{"result":"No colleges found"})

def checkCollegeEE(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][3]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList,"course":"EE"})
    return render(request,"NoResult.html",{"result":"No colleges found"})