from audioop import add
import re
from django.shortcuts import render,HttpResponse
from .models import Donor

# Create your views here.
def index(request):
    return render(request,'index.html')

def see_donors(request):
    donor = Donor.objects.all()
    context={
        "donor":donor
    }
    return render(request,'see_donors.html',context)

def add_donors(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = int(request.POST['age'])
        address = request.POST['address']
        phone = int(request.POST['phone'])
        blood_group = request.POST['blood_group']
        new_donor = Donor(first_name=first_name,last_name=last_name,age=age,address=address,phone=phone,blood_group=blood_group)
        new_donor.save()
        return HttpResponse("Donor Added successfully!")
    elif request.method=='GET':
        return render(request,'add_donors.html')
    else:
        return HttpResponse("Not added! something is wrong")