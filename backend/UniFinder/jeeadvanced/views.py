from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"jeeadvanced.html")

collegeDict = {"Indian Institute of Technology Bombay":[63,1058],"Indian Institute of Technology Delhi":[104,469],"Indian Institute of Technology Madras":[157,722],
                "Indian Institute of Technology Kanpur":[231,994],"Indian Institute of Technology Kharagpur":[284,1417],"Indian Institute of Technology Roorkee":[421,1856],
                "Indian Institute of Technology Guwahati":[586,2028],"Indian Institute of Technology Hyderabad":[564,1868],"Indian Institute of Technology Varanasi":[865,2376],
                "Indian Institute of Technology Indore":[1194,3635],"Indian Institute of Technology Ropar":[1856,4699],"Indian Institute of Technology Gandhinagar":[1398,3299],
                "Indian Institute of Technology Bhubaneswar":[2096,4649],"Indian Institute of Technology Mandi":[2533,5366],
                "Indian Institute of Technology Jodhpur":[2760,5719],"Indian Institute of Technology Dhanbad":[2762,5495],"Indian Institute of Technology Patna":[2509,3995],
                "Indian Institute of Technology Tirupati":[3491,6966],"Indian Institute of Technology Goa":[3788,7048],"Indian Institute of Technology Palakkad":[4521,1735],
                "Indian Institute of Technology Dharwad":[4719,7596],"Indian Institute of Technology Jammu":[4995,8916],"Indian Institute of Technology Bhilai":[5026,8424]}

def checkCollegeCSE(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][0]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList})
    return render(request,"NoResult.html",{"result":"No colleges found"})

def checkCollegeEEE(request):
    collageList = []
    for x in collegeDict:
        if int(request.GET["rank"]) <= collegeDict[x][1]:
            collageList.append(x)
    if(collageList):
        return render(request,"Result.html",{"result":collageList})
    return render(request,"NoResult.html",{"result":"No colleges found"})