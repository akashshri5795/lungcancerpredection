from django.http import HttpResponse
from django.shortcuts import render, redirect
from user_account.models import userAccount
from patient_model.models import PatientModel

def homePage(request):     
    return render(request,"index.html")

def saveAccount(request):  
    if request.method=="POST":
        name=request.POST.get('user_name')
        contact=request.POST.get('user_contact')
        email=request.POST.get('user_email')
        password=request.POST.get('user_passowrd')
        data=userAccount(name=name, contact=contact, email=email, password=password)
        data.save()    
        return redirect('home_page')
    
def LoginUser(request):    
    if request.method == "POST":
        user_email = request.POST.get('user_email')     
        user_password = request.POST.get('user_password')     
        reg_user = userAccount.objects.filter(email=user_email, password=user_password).first()
        if reg_user:
            patient=PatientModel.objects.all()
            return render(request,'dashboard.html',{'patient':patient})
       
    else:        
        return redirect('home_page')  

