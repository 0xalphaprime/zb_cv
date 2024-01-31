from django.shortcuts import render

# Create your views here.

def cv(request):
    return render(request, "cv.html")

def slb(request):
    return render(request, "zb_slb.html")

def ez(request):
    return render(request, "zb_ez.html")

def sl360(request):
    return render(request, "zb_sl360.html")

def xp(request):
    return render(request, "zb_xp.html")

def wires_and_cables(request):
    return render(request, "zb_wires_cables.html")