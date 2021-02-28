from django.shortcuts import render

# Create your views here.
def getpage(request):
    if request.GET["page"].lower()=="pes":
        return render(request,"pes.html")
    elif request.GET["page"].lower()=="msrit":
        return render(request,"msrit.html")
    elif request.GET["page"].lower()=="rv":
        return render(request,"rvce.html")
    elif request.GET["page"].lower()=="bms":
        return render(request,"bms.html")
    else:
        return render(request,"./")

