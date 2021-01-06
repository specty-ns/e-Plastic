from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import *

# Create your views here.
def IndexPage(request):
    return render(request,"eplastic/index.html")
def CustomerSignUp(request):
    return render(request,"eplastic/customer_signup.html")
def AdminSignUp(request):
    return render(request,"eplastic/admin_signup.html")
def Register(request):
    if request.POST['role']=="customer":
        role = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        address = request.POST['address']
    
        user=Master.objects.filter(email=email)
        if user:
            message = "User already exist! "
            return render(request,"eplastic/index.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(10000,99999)
                newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                newCust=Customer.objects.create(master_id=newMaster,fname=fname,lname=lname,contact=contact,address=address)
                return render(request,"eplastic/index.html")
            else:
                message= "Password doesn't match!"
                return render(request,"eplastic/customer_signup.html",{'msg':message})
    else:
        if request.POST['role']=="RecyclingCompany":
            role = request.POST['role']
            name=request.POST['name']
            email=request.POST['email']
            contact=request.POST['phone']
            address=request.POST['address']
            password = request.POST['password']
            cpassword = request.POST['cpassword']

            user=Master.objects.filter(email=email)
            if user:
                message = "User already exist! "
                return render(request,"eplastic/index.html",{'msg':message})
            else:
                if password==cpassword:
                    otp = randint(10000,99999)
                    newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                    newCust=Company.objects.create(master_id=newMaster,comp_name=name,comp_address=address,comp_contact=contact)
                    return render(request,"eplastic/index.html")
                else:
                    message= "Password doesn't match!"
                    return render(request,"eplastic/admin_signup.html",{'msg':message})
    
        if request.POST['role']=="PlasticCollector":
            role = request.POST['role']
            name=request.POST['name']
            email=request.POST['email']
            contact=request.POST['phone']
            address=request.POST['address']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            user=Master.objects.filter(email=email)
            if user:
                message = "User already exist! "
                return render(request,"eplastic/index.html",{'msg':message})
            else:
                if password==cpassword:
                    otp = randint(10000,99999)
                    newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                    newCust=PlasticC.objects.create(master_id=newMaster,pc_fname=name,pc_address=address,pc_contact=contact)
                    return render(request,"eplastic/index.html")
                else:
                    message= "Password doesn't match!"
                    return render(request,"eplastic/admin_signup.html",{'msg':message})
            























        #if request.POST['role']=="Re-cycling Company"
 
    
