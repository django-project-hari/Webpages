from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

# def concat(request):
#     fn=request.POST['fname']
#     ln=request.POST['lname']
#     ff=fn+ln
#     return render(request,"display.html",{'display':ff})
# testing for merging
