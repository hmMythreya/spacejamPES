from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
all_colleges = {'nit warangal': [2341, 2919, 10209, 8152], 'nit surathkal': [3181, 5608, 11788, 6801], 'mnit jaipur': [3831, 7868, 11426, 9179], 
                'mnit allahabad': [4051, 7128, 11145, 8790], 'nit kurukshetra': [6170, 12067, 18115, 16273], 'nit rourkela': [9420, 12009, 20304, 19168], 
                'nit calicut': [10222, 14769, 20480, 18966], 'nit durgapur': [12095, 16098, 22753, 19325], 'nit silchar': [23882, 40841, 49215, 56958], 
                'r.v.college': [450, 918], 'bms college of engineering': [1000, 1500], 'ms ramaiah': [1100, 2000], 'sjce college of engineering': [2500, 6000], 
                'bangalore institute of technology': [2700, 5300], 'sir m.visvesvaraya institute of technology': [3300, 6100], 
                'dayananda sagar college of engineering': [4300, 8300], 'the national institute of engineering, mysore': [4500, 7000], 
                'rns institute of technology': [5800, 12200], 'bnm institute of technology': [7700, 15000], 'jss academy bangalore': [9000, 17000], 
                'cmr institute of technology': [10000, 23000], 'nitte meenakshi institute of technology': [11000, 19000], 
                'nmam institute of technology': [21800, 30000], 'indian institute of technology bombay': [63, 1058], 
                'indian institute of technology delhi': [104, 469], 'indian institute of technology madras': [157, 722], 
                'indian institute of technology kanpur': [231, 994], 'indian institute of technology kharagpur': [284, 1417], 
                'indian institute of technology roorkee': [421, 1856], 'indian institute of technology guwahati': [586, 2028], 
                'indian institute of technology hyderabad': [564, 1868], 'indian institute of technology varanasi': [865, 2376],
                'indian institute of technology indore': [1194, 3635], 'indian institute of technology ropar': [1856, 4699], 
                'indian institute of technology gandhinagar': [1398, 3299], 'indian institute of technology bhubaneswar': [2096, 4649],
                'indian institute of technology mandi': [2533, 5366], 'indian institute of technology jodhpur': [2760, 5719],
                'indian institute of technology dhanbad': [2762, 5495], 'indian institute of technology patna': [2509, 3995], 
                'indian institute of technology tirupati': [3491, 6966], 'indian institute of technology goa': [3788, 7048], 
                'indian institute of technology palakkad': [4521, 1735], 'indian institute of technology dharwad': [4719, 7596], 
                'indian institute of technology jammu': [4995, 8916], 'indian institute of technology bhilai': [5026, 8424]}

def bms(request):
        return render(request,"bms.html")
def rvce(request):
        return render(request,"rvce.html")
def msrit(request):
        return render(request,"msrit.html")
def pes(request):
        return render(request,"pes.html")