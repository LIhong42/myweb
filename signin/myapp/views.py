from django.shortcuts import render,HttpResponse

# Create your views here.
def myQRcode(request):
    return render(request,'QRcode.html')
def mysignin(request):
    return render(request,'signin.html')