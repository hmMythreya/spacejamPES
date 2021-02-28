collegeList = ["R.V.College","BMS College of Engineering","Ms Ramaiah","SJCE College of Engineering",
                "Bangalore Institute of Technology","Sir M.Visvesvaraya Institute of Technology",
                "Dayananda Sagar College of Engineering",]

collegeDictCse = {"R.V.College":450,"BMS College of Engineering":1000,"Ms Ramaiah":1100,"SJCE College of Engineering":2500,"Bangalore Institute of Technology":2700
                ,"Sir M.Visvesvaraya Institute of Technology":3300,"Dayananda Sagar College of Engineering":4300}

def checkCollegeCSE(rank):
    for x in collegeDictCse:
        if rank < collegeDictCse[x]:
            return collegeList[collegeList.index(x):]

print(checkCollegeCSE(int(input("Enter Rank:"))))