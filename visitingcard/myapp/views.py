from cProfile import Profile
from django.shortcuts import render,redirect,HttpResponse
from .models import *

# Create your views here.
def Home(request):
    return render(request,'form.html')
def Details(request):
     objs = employee.objects.all()
     d= {
        'records':objs
     }
     return render(request,'read.html',d)
def submit(request):
    if request.method == 'POST':
        name = request.POST['Name']
        user = request.POST['User']
        DOB = request.POST['DOB']
        Gender = request.POST['Gender']
        #profile = request.POST['profile']
        #Profile = request.POST['used']
        obj = employee()
        obj.name =name
        obj.user = user
        obj.DOB = DOB
        obj.gender = Gender
        obj.save()
        #obj.profile = Profile
        # obj.profle =Profile
        # return HttpResponse('Record saves')
    return redirect(visit)
def visit(request):
    objs = employee.objects.all()
    d1 = {
        'cards':objs
    }
    return render(request,'card.html',d1)
def delete(request,id):
    objs =employee.objects.get(id=id)
    objs.delete()
    return redirect(visit)