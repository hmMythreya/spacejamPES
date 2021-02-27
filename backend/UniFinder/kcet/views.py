from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"kcet.html")

collegeDict = {"RV College of Engineering":[239,651],"MS Ramaiah Institute of Technology":[868,3245],"BMS College of Engineering":[809,2686],
               "Dr. Ambedkar Institute Of Technology":[11130,30012],"Dayananda Sagar College of Engineering":[6644,22851],
               "Bangalore Institute of Technology":[5751,27305],"P E S University (Electronic City Campus)":[3880,11284],
               "Sir M.Visveswaraya Institute of Technology":[10290,32686]}

def checkCollegeCSE(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][0]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList,"course":"CSE"})
    return render(request,"NoResult.html",{"result":"No colleges found"})

def checkCollegeEEE(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][1]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList,"course":"EEE"})
    return render(request,"NoResult.html",{"result":"No colleges found"})