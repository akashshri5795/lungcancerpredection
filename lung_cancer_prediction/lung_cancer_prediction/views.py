from django.http import HttpResponse
from django.shortcuts import render, redirect
from user_account.models import userAccount
from patient_model.models import PatientModel, PatientCTScans

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
            return redirect('dashboard')
       
    else:        
        return redirect('home_page')  

def Dashboard(request):
     patient=PatientModel.objects.all()
     return render(request,'dashboard.html',{'patient':patient})

def savePatient(request):  
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        data=PatientModel(first_name=first_name, last_name=last_name, age=age, gender=gender, contact=contact, address=address)
        data.save()    
        return redirect('dashboard')
    
def uploadCTScan(request):  
    if request.method=="POST":
        patient_id=request.POST.get('patient_id')   
        upload_image = request.FILES.get('upload_ct_scan')
        data=PatientCTScans(patient_id_id=patient_id, upload_image=upload_image)
        data.save()    
        return redirect('dashboard')

def showCTScan(request):  
    ctscans=PatientCTScans.objects.select_related('patient_id').all()
    return render(request,'ctscan.html',{'ctscans':ctscans})




