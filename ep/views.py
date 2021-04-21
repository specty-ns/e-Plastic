from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from random import *
import datetime
from django.conf import settings
from .paytm import generate_checksum, verify_checksum
from .utils import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .filters import *
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.
def IndexPage(request):
    report_i=CustomerData.objects.all()
    totalcollection_i = 0
    totalusage_i = 0
    totalwastage_i = 0
    count_i =0
    for s in enumerate(report_i): 
        count_i=count_i+1
    for e in report_i:
        totalcollection_i += e.total_collection
    for x in report_i:
        totalusage_i+=x.usage
    for y in report_i:
        totalwastage_i+=y.wastage
    return render(request,"ep/index-2.html",{"report_i":report_i,"totalcollection_i":totalcollection_i,"count_i":count_i,"t_usage_i":totalusage_i,"t_waste_i":totalwastage_i})
def AboutUs(request):
    return render(request,"ep/about.html")
def FAQ(request):
    return render(request,"ep/faq.html")

def CompanyIndexPage(request):
    if "email" in request.session and "password" in request.session:
        user = Master.objects.get(id=request.session['id'])
        comp = Company.objects.get(master_id=user)
        return render(request,"ep/company_index.html",{'image':comp.comp_image})
    else:
        return redirect('adminin')
def CollectorIndexPage(request,pk):
    if "email" in request.session and "password" in request.session:
        user = Master.objects.get(id=pk)
        plast = PlasticC.objects.get(master_id=user)
        report_r=PlasticData.objects.all().filter(plastic_id=plast)
        totalcollection_r = 0
        totalusage_r = 0
        totalwastage_r = 0
        count_r =0
        for c in enumerate(report_r): 
            count_r=count_r+1
        for i in report_r:
            totalcollection_r += i.total_collection
        for u in report_r:
            totalusage_r+=u.usage
        for w in report_r:
            totalwastage_r+=w.wastage
        return render(request,"ep/plasticCollector_index.html",{"report_r":report_r,"totalcollection_r":totalcollection_r,"count_r":count_r,"t_usage_r":totalusage_r,"t_waste_r":totalwastage_r})
    else:
        return redirect('adminin')
def Index2Page(request):
    if "email" in request.session and "password" in request.session:
        user= Master.objects.get(id=request.session['id'])
        cust = Customer.objects.get(master_id=user)
        report_s=CustomerData.objects.all().filter(cust_id=cust)
        totalcollection_s = 0
        totalusage_s = 0
        totalwastage_s = 0
        count_s =0
        for b in enumerate(report_s): 
            count_s=count_s+1
            print(count_s)
        for s in report_s:
            totalcollection_s += s.total_collection
        for d in report_s:
            totalusage_s+=d.usage
        for k in report_s:
            totalwastage_s+=k.wastage
        return render(request,"ep/index-2.html",{"report_s":report_s,"totalcollection_s":totalcollection_s,"count_s":count_s,"t_usage_s":totalusage_s,"t_waste_s":totalwastage_s})
    else:
        return redirect('signin')
def CustomerSignUp(request):
    return render(request,"ep/customer_signup.html")
def CustomerSignIn(request):
    return render(request,"ep/customer_signin.html")
def AdminSignUp(request):
    return render(request,"ep/admin_signup.html")
def AdminSignIn(request):
    return render(request,"ep/admin_signin.html")
def CustomerProfile(request):
    if "email" in request.session and "password" in request.session:
        return render(request,"ep/customer_profile.html")
    else:
        return redirect('adminin')
def CompanyOrderDl(request):
    if "email" in request.session and "password" in request.session:
        return render(request,"ep/company_orders_dl.html",{'cust':Customer.objects.all()})
    else:
        return redirect('adminin')
def CompanyProfile(request):
    if "email" in request.session and "password" in request.session:
        return render(request,"ep/company_profile.html")
    else:
        return redirect('adminin')
def PlasticCollectorProfile(request):
    if "email" in request.session and "password" in request.session:
        return render(request,"ep/plasticCollector_profile.html")
    else:
        return redirect('adminin')
def PlasticDataDl(request):
    if "email" in request.session and "password" in request.session:
        return render(request,"ep/plastic_data_dl.html",{'rc':Company.objects.all()})
    else:
        return redirect('adminin')
def PProduct(request):
    if "email" in request.session and "password" in request.session:
        return render(request,"ep/addpproduct.html")
    else:
        return redirect('adminin')
def RProduct(request):
    if "email" in request.session and "password" in request.session:
        return render(request,"ep/addrproduct.html")
    else:
        return redirect('adminin')
def AdminLogin(request):
    return render(request,"ep/admin/login.html")
    
def Dashboard(request):
    if "Role" in request.session and "password" in request.session:
        return render(request,"ep/admin/aindex.html")
    else:
        return redirect('alogin')
def CustData(request):
    if "email" in request.session and "password" in request.session:
        return render(request,"ep/customer_data.html",{"cust":Customer.objects.all()})
    else:
        return redirect('adminin')
def RCData(request):
    if "email" in request.session and "password" in request.session:
        comp = Company.objects.get(master_id=request.session['id'])
        return render(request,"ep/rc_data.html",{"rc":PlasticC.objects.all(),'image':comp.comp_image})
    else:
        return redirect('adminin')
def invoice(request,pk):
    if "email" in request.session and "password" in request.session:
        invoice = AddToCart.objects.get(id=pk)
        return render(request,"ep/invoice.html",{"invoice":invoice})
    else:
        return redirect('signin')

def OTP(request):
    return render(request,"ep/otpverify.html")

def download(request):
    if "email" in request.session and "password" in request.session:
        return render(request,"ep/download.html",{'plast':PlasticC.objects.all()})
    else:
        return redirect('signin')
def AdminCustDataDl(request):
    if "Role" in request.session and "password" in request.session:
        return render(request,"ep/admin/customer_data_dl.html",{'cust':Customer.objects.all()})
    else:
        return redirect('alogin')
def AdminRCDataDl(request):
    if "Role" in request.session and "password" in request.session:
        return render(request,"ep/admin/company_data_dl.html",{'rc':Company.objects.all()})
    else:
        return redirect('alogin')
def AdminPCDataDl(request):
    if "Role" in request.session and "password" in request.session:
        return render(request,"ep/admin/collector_data_dl.html",{'plast':PlasticC.objects.all()})
    else:
        return redirect('alogin')
def Register(request):
    try:
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
                return render(request,"ep/customer_signup.html",{'msg':message})
            else:
                if password==cpassword:
                    otp = randint(10000,99999)
                    newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                    newCust=Customer.objects.create(master_id=newMaster,fname=fname,lname=lname,contact=contact,address=address)
                    email_subject = "Customer Verification"
                    sendmail(email_subject,'mail_template',email,{'name':fname,'otp':otp})
                    mail = email
                    request.session['email']=newMaster.email

                    return render(request,"ep/otpverify.html",{'email':mail})
                else:
                    message= "Password doesn't match!"
                    return render(request,"ep/customer_signup.html",{'msg':message})
           
        
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
                return render(request,"ep/admin_signup.html",{'msg':message})
            else:
                if password==cpassword:
                    otp = randint(10000,99999)
                    newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                    newComp=Company.objects.create(master_id=newMaster,comp_name=name,comp_address=address,comp_contact=contact)
                    email_subject = "Recycling Company Verification"
                    sendmail(email_subject,'mail_template',email,{'name':name,'otp':otp})
                    mail = email
                    request.session['email']=newMaster.email

                    return render(request,"ep/otpverify.html",{'email':mail})
                    
                else:
                    message= "Password doesn't match!"
                    return render(request,"ep/admin_signup.html",{'msg':message})
        
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
                return render(request,"ep/index.html",{'msg':message})
            else:
                if password==cpassword:
                    otp = randint(10000,99999)
                    newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                    newPlastic=PlasticC.objects.create(master_id=newMaster,pc_name=name,pc_address=address,pc_contact=contact)
                    email_subject = "Plastic Collector Verification"
                    sendmail(email_subject,'mail_template',email,{'name':name,'otp':otp})
                    mail = email
                    request.session['email']=newMaster.email

                    return render(request,"ep/otpverify.html",{'email':mail})    
                else:
                    message= "Password doesn't match!"
                    return render(request,"ep/admin_signup.html",{'msg':message})
    except Exception as e1:
        print("RegistrationException---------------------->",e1)

def VerifyOtp(request):
    print("------------1--------------")
    try:
        email=request.session['email']
        eotp=int(request.POST['eotp'])
        print("Eotp--------------->",eotp)
        user = Master.objects.get(email=email)
        if user.otp==eotp and user.role =="customer":
            message = "otp verified successfully"
            return render(request,"ep/customer_signin.html",{'msg2':message})
        elif user.otp==eotp and user.role=="RecyclingCompany":
            message = "otp verified successfully"
            return render(request,"ep/admin_signin.html",{'msg2':message})
        elif user.otp==eotp and user.role=="PlasticCollector":
            message = "otp verified successfully"
            return render(request,"ep/admin_signin.html",{'msg2':message})
        else:
            message = "Enter Correct OTP "
            return render(request,"ep/otpverify.html",{'email':email, 'msg3':message})
    except Exception as e:
        print("OTP Verify Exception-------------->",e)
        
def LoginUser(request):
    try:
        if request.POST['role']=="customer":
            email = request.POST['email']
            password= request.POST['password']
            user = Master.objects.get(email=email)
            if user:
                if user.password==password and user.role=="customer":
                    cust = Customer.objects.get(master_id=user)
                    print("Customer------------------------->",cust)
                    request.session['email']=user.email
                    request.session['password'] = user.password
                    request.session['Role']=user.role
                    request.session['Firstname'] = cust.fname
                    request.session['Lastname'] = cust.lname
                    request.session['Gender'] = cust.gender
                    request.session['State'] = cust.state
                    request.session['id'] = user.id
                    return HttpResponseRedirect(reverse('index2'))      
                else:
                    message = "Password Doesn't match!"
                    return render(request,"ep/customer_signin.html",{'msg':message})
            else:
                message = "User Email or Password Doesnot match"
                return render(request,"ep/customer_signin.html",{'msg3':message})
    except Exception as cust:
            message = "Email doesn't match"
            print("CustLogin---------------------->",cust)
            return render(request,"ep/customer_signin.html",{'msg3':message})
    try:
        if request.POST['role']=="RecyclingCompany":
            email = request.POST['email']
            password= request.POST['password']
            user = Master.objects.get(email=email)
            if user:
                if user.password==password and user.role=="RecyclingCompany":
                    comp = Company.objects.get(master_id=user)
                    request.session['email']=user.email
                    request.session['password'] = user.password
                    request.session['id']=user.id
                    request.session['Role']=user.role
                    request.session['Cname']=comp.comp_name
                    request.session['Cadd']=comp.comp_address
                    request.session['Ccon']=comp.comp_contact
                    request.session['Cfb']=comp.comp_fb
                    request.session['Cins']=comp.comp_insta
                    request.session['Clin']=comp.comp_linkedin
                    request.session['Ctwit']=comp.comp_twitter
                    request.session['Cweb']=comp.comp_website
                    request.session['Ofname']=comp.owner_fname
                    request.session['Olname']=comp.owner_lname
                    request.session['Ogen']=comp.owner_gender
                    request.session['Ocon']=comp.owner_contact
                    request.session['Oemail']=comp.owner_email
                    return HttpResponseRedirect(reverse('companyindex'))
                else:
                    message= "Role or Password doesn't match!"
                    return render(request,"ep/admin_signin.html",{'msg':message})
    except Exception as rc:
            message = "Email doesn't match"
            print("RcLogin---------------------->",rc)
            return render(request,"ep/admin_signin.html",{'msg9':message})
    try:
        if request.POST['role']=="PlasticCollector":
            email = request.POST['email']
            password= request.POST['password']
            user = Master.objects.get(email=email)
            if user:
                if user.password==password and user.role=="PlasticCollector":
                    pc = PlasticC.objects.get(master_id=user)
                    request.session['email']=user.email
                    request.session['password'] = user.password
                    request.session['id']=user.id
                    request.session['Role']=user.role
                    request.session['Pcname']=pc.pc_name
                    request.session['Pcadd']=pc.pc_address
                    request.session['Pccon']=pc.pc_contact
                    request.session['Pcfb']=pc.pc_fb
                    request.session['Pcins']=pc.pc_insta
                    request.session['Pclin']=pc.pc_linkedin
                    request.session['Pctwit']=pc.pc_twitter
                    request.session['Pcweb']=pc.pc_website
                    request.session['Ofname']=pc.owner_fname
                    request.session['Olname']=pc.owner_lname
                    request.session['Ogen']=pc.owner_gender
                    request.session['Ocon']=pc.owner_contact
                    request.session['Oemail']=pc.owner_email
                    pc = request.session['id']
                    url = f'/collectorindex/{pc}'
                    return redirect(url)  
                else:
                    message= "Role or Password doesn't match!"
                    return render(request,"ep/admin_signin.html",{'msg':message})
    except Exception as pc:
            message = "Email doesn't match"
            print("Pccccc---------------------->",pc)
            return render(request,"ep/admin_signin.html",{'msg5':message})

                
def CustomerProfileData(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="customer":
            cust = Customer.objects.get(master_id=udata)
            return render(request,"ep/customer_profile.html",{'key3':cust})
    else:
        return redirect('signin')

def UpdateButtonClick(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="customer":
            cust = Customer.objects.get(master_id=udata)
            return render(request,"ep/customer_update.html",{"key4":cust})
    else:
        return redirect('signin')

def CompanyProfileData(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="RecyclingCompany":
            comp = Company.objects.get(master_id=udata)
            return render(request,"ep/company_profile.html",{'key5':comp})
    else:
        return redirect('adminin')
def CompanyUpdateClick(request,pk):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=pk)
        if udata.role=="RecyclingCompany":
            comp = Company.objects.get(master_id=udata)
            return render(request,"ep/company_update.html",{"key6":comp})
    else:
        return redirect('adminin')


def PlasticCollectorProfileData(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="PlasticCollector":
            pc = PlasticC.objects.get(master_id=udata)
            return render(request,"ep/plasticCollector_profile.html",{'key8':pc})
    else:
        return redirect('adminin')
def PlasticCollectorUpdateButtonClick(request,pk):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=pk)
        if udata.role=="PlasticCollector":
            pc = PlasticC.objects.get(master_id=udata)
            return render(request,"ep/plasticCollector_update.html",{"key7":pc})
    else:
        return redirect('adminin')

def UpdateData(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="customer":
            cust = Customer.objects.get(master_id=udata)
            cust.fname = request.POST['fname']
            cust.lname = request.POST['lname']
            cust.gender = request.POST['gender']
            udata.email = request.POST['email'] 
            cust.contact = request.POST['contact']
            cust.address = request.POST['address']
            cust.state = request.POST['state']
            cust.city = request.POST['city']
            cust.postalcode = request.POST['postcode']
            udata.save()
            cust.save()
            url = f'/profiledata/{pk}'
            return redirect(url)    
    else:
        return redirect('signin')

def CompanyUpdateData(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="RecyclingCompany":
            comp = Company.objects.get(master_id=udata)
            udata.email = request.POST['email']
            comp.comp_name= request.POST['cname']
            comp.comp_contact = request.POST['ccontact']
            comp.comp_address = request.POST['caddress']
            comp.comp_website = request.POST['cwebsite']
            comp.comp_image = request.FILES['cimage']
            comp.comp_insta = request.POST['cinsta']
            comp.comp_linkedin = request.POST['clinkedin']
            comp.comp_twitter = request.POST['ctwitter']
            comp.comp_fb = request.POST['cfb']
            comp.owner_fname = request.POST['cofname']
            comp.owner_lname = request.POST['colname']
            comp.owner_gender = request.POST['cogender']
            comp.owner_email = request.POST['coemail']
            comp.owner_contact = request.POST['cocontact']
            udata.save()
            comp.save()
            url = f'/companydata/{pk}'
            return redirect(url)
    else:
        return redirect('adminin')

def PlasticCollectorUpdateData(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        
        if udata.role=="PlasticCollector":
            pc = PlasticC.objects.get(master_id=udata)
            udata.email = request.POST['email']
            pc.pc_name = request.POST['pcname']
            pc.pc_address = request.POST['pcaddress']
            pc.pc_contact = request.POST['pccontact']
            pc.pc_image = request.FILES['pcimage']
            pc.pc_fb = request.POST['pcfb']
            pc.pc_insta = request.POST['pcinsta']
            pc.pc_linkedin = request.POST['pclinkedin']
            pc.pc_twitter = request.POST['pctwitter']
            pc.pc_website = request.POST['pcwebsite']
            pc.owner_fname = request.POST['pcofname']
            pc.owner_lname = request.POST['pcolname']
            pc.owner_gender = request.POST['pcogender']
            pc.owner_email = request.POST['pcoemail']
            pc.owner_contact = request.POST['pcocontact']
            udata.save()
            pc.save()   
            url = f'/plasticCollectordata/{pk}'
            return redirect(url)
    else:
        return redirect('adminin')    

def AddPProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            udata = Master.objects.get(id=pk)
            if udata.role=="PlasticCollector":
                pc = PlasticC.objects.get(master_id=udata)
                pro_name = request.POST['pname']
                pro_price = request.POST['pprice']
                pro_image = request.FILES['pimage']
                pro_quantity = request.POST['pqty']

                newProduct=PlasticProduct.objects.create(plasticc_id=pc,pproduct_name=pro_name,pproduct_price=pro_price,pproduct_image=pro_image,pproduct_quantity=pro_quantity)
                message= "Product Added Successfully"
                return render(request,"ep/addpproduct.html",{'msg':message})
        except Exception as ae:
            print("Add P Product--------->",ae)
    else:
        return redirect('adminin')
def GetAllPProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="PlasticCollector":
            pc = PlasticC.objects.get(master_id=udata)
            allpproduct= PlasticProduct.objects.all().filter(plasticc_id=pc)
            search = request.GET.get('search')
            if search !='' and search is not None:
                allpproduct=allpproduct.filter(pproduct_name__icontains=search) | allpproduct.filter(pproduct_date__icontains=search)
            p = Paginator(allpproduct,5)
            page_num = request.GET.get('page')
            try:
                page = p.page(page_num)
            except PageNotAnInteger:
                page= p.page(1)
            except EmptyPage:
                page = p.page(p.num_pages)
            return render(request,"ep/allpproducts.html",{'key9':page,"page":p})
    else:
        return redirect('adminin')
def PPUpdateButton(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            pp = PlasticProduct.objects.get(id=pk)
            print("IDt--------->",id)
            return render(request,"ep/pproduct_update.html",{"key10":pp})
        except Exception as r:
            print("Button Product--------->",r)
    else:
        return redirect('adminin')


def UpdateProduct(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            pro = PlasticProduct.objects.get(pk=pk)
            pro.pproduct_name = request.POST['pname']
            pro.pproduct_price = request.POST['pprice']
            pro.pproduct_image = request.FILES['pimage']
            pro.pproduct_quantity = request.POST['pqty']
            pro.save()
            pp = request.session['id']
            url = f"/allpproducts/{pp}"
            return redirect(url)
        except Exception as i:
            print("Image Product--------->",i)
    else:
        return redirect('adminin')
def DeleteProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            ddata = PlasticProduct.objects.get(pk=pk)
            ddata.delete()
            pp = request.session['id']
            url = f"/allpproducts/{pp}"
            return redirect(url)
        except Exception as ok:
            print("------------>delete error",ok)
    else:
        return redirect('adminin')
def RPAllStatus(request):

    if "email" in request.session and "password" in request.session:
        all_show = PlasticRequest.objects.all()
        search = request.GET.get('search')
        if search !='' and search is not None:
            all_show= all_show.filter(pproduct_id__pproduct_name__icontains= search) 
        status = request.GET.get('status')
        if status !='' and status is not None:
            all_show= all_show.filter(status=status)
        p = Paginator(all_show,5)
        page_num = request.GET.get('page',1)
        try:
            page = p.page(page_num)
        except PageNotAnInteger:
            page = p.page(1)
        except EmptyPage:
            page = p.page(p.num_pages)
        num =p.num_pages
        print(p.count)
        return render(request,"ep/rp_allprostatus.html",{'status':page,'count':p})
    else:
        return redirect('adminin')
def RPAllProduct(request):
    if "email" in request.session and "password" in request.session:

        all_pro = PlasticProduct.objects.all() 
        search = request.GET.get('search')
        if search !='' and search is not None:
            all_pro= all_pro.filter(pproduct_name__icontains= search) | all_pro.filter(plasticc_id__pc_name__icontains=search) | all_pro.filter(pproduct_date__icontains=search)
        p = Paginator(all_pro,5)
        page_num = request.GET.get('page',1)
        try:
            page = p.page(page_num)
        except PageNotAnInteger:
            page = p.page(1)
        except EmptyPage:
            page = p.page(p.num_pages)
        num =p.num_pages
        print(p.count)
        return render(request,"ep/rp_allproducts.html",{'key11':page,'count':p})
    else:
        return redirect('adminin')
def RPButtonClick(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            pc = PlasticProduct.objects.get(pk=pk)
            return render(request,"ep/requestpproduct.html",{'key12':pc})
        except Exception as k:
            print("------------>Click error",k)
    else:
        return redirect('adminin')

def CompanyCheckOut(request):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=request.session['id'])
        total = 0
        if udata.role == "RecyclingCompany":
            cdata = Company.objects.get(master_id=udata)
            cartdata = PlasticRequest.objects.get(id=request.POST['pro_id'])
            total = cartdata.request_quantity*cartdata.pproduct_id.pproduct_price
            return render(request,"ep/company_checkout.html",{"key26":cartdata,"total":total,"key27":cdata})
    else:
        return redirect('signin')

def RPButton(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            udata = Master.objects.get(id=pk)
            if udata.role == "RecyclingCompany":
                rcdata = Company.objects.get(master_id=udata)
                email = rcdata.master_id.email
                rcname = rcdata.comp_name
                pc_id = request.POST['pc_id']
                pla_id = PlasticC.objects.get(id=pc_id)
                pc_email = pla_id.master_id.email
                pcname= pla_id.pc_name
                pc_date = request.POST['rdate']
                pc_qty = request.POST['rqty']
                pid = request.POST['pid']
                pro_id = PlasticProduct.objects.get(id=pid)
                plasticname= pro_id.pproduct_name
                newRequest=PlasticRequest.objects.create(comp_id=rcdata,plasticc_id=pla_id,pproduct_id=pro_id,request_date=pc_date,request_quantity=pc_qty)
                email_subject = "Plastic Request"
                sendreq(email_subject,'mail_template',email,{'pcname':pcname,'requestqty':pc_qty,'productname':plasticname,'requestdate':pc_date})
                showreq(email_subject,'mail_template',pc_email,{'rcname':rcname,'requestqty':pc_qty,'productname':plasticname,'requestdate':pc_date})
                message= "Request Sent Successfully"
                pro_id.pproduct_quantity-=int(pc_qty)
                pro_id.save()
                return HttpResponseRedirect(reverse('rpallpro'),{'msg':message})
        except Exception as e11:
            print("Req Button ----------------------------->",e11)
    else:
        return redirect('adminin')

def ShowPReq(request):
    if "email" in request.session and "password" in request.session:
        try:
            udata = Master.objects.get(id=request.session['id'])
            if udata.role=="PlasticCollector":
                pc = PlasticC.objects.get(master_id=udata)
                allpproduct = PlasticRequest.objects.all().filter(plasticc_id=pc)
                status = request.GET.get('status')
                search = request.GET.get('search')

                if status !='' and status is not None and status !="All":
                    allpproduct =allpproduct.filter(status=status)
                if search !='' and search is not None:
                    allpproduct = allpproduct.filter(comp_id__comp_name__icontains=search) | allpproduct.filter(id__icontains=search) |allpproduct.filter(pproduct_id__id__icontains=search) | allpproduct.filter(request_date__icontains=search)

                p = Paginator(allpproduct,5)
                page_num = request.GET.get('page')
                try:
                    page = p.page(page_num)
                except PageNotAnInteger:
                    page= p.page(1)
                except EmptyPage:
                    page = p.page(p.num_pages)
            return render(request,"ep/showplasticreq.html",{'key13':page,'page':p,'allproduct':allpproduct})
        except Exception as s:
            print("Show ----------------------------->",s)
            return render(request,"ep/showplasticreq.html")
    else:
        return redirect('adminin')


def reqaccept(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            pc_id = request.session['id'] 
            print("iddddd>>>>>>>>>>>>>>>.",pc_id)  
            plastic_id =PlasticC.objects.get(master_id=pc_id)
            pcname = plastic_id.pc_name
            all_preq = PlasticRequest.objects.get(pk=pk,plasticc_id=plastic_id)
            reqqty = all_preq.request_quantity
            pproductname = all_preq.pproduct_id.pproduct_name
            reqdate = all_preq.request_date
            email = request.POST['email']
            print("emaillll",email)
            email_subject = "Plastic Request Accepted"
            acceptreq(email_subject,'mail_template',email,{'pcname':pcname,'requestqty':reqqty,'productname':pproductname,'requestdate':reqdate})
            all_preq.status = request.POST['acceptreq']
            all_preq.save()
            message="Request Accepted"
            return HttpResponseRedirect(reverse('showpreq'))
        except Exception as reee:
            print("Acc ----------------------------->",reee)
    else:
        return redirect('adminin')    
def RejectProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            pc_id = request.session['id'] 
            print("iddddd>>>>>>>>>>>>>>>.",pc_id)  
            plastic_id =PlasticC.objects.get(master_id=pc_id)
            pcname = plastic_id.pc_name
            all_preq = PlasticRequest.objects.get(pk=pk,plasticc_id=plastic_id)
            reqqty = all_preq.request_quantity
            pproductname = all_preq.pproduct_id.pproduct_name
            reqdate = all_preq.request_date
            email = request.POST['email']
            print("emaillll",email)
            email_subject = "Plastic Request Rejected"
            rejectreq(email_subject,'mail_template',email,{'pcname':pcname,'requestqty':reqqty,'productname':pproductname,'requestdate':reqdate})
            all_preq.status = request.POST['rejectreq']
            all_preq.pproduct_id.pproduct_quantity+=reqqty
            all_preq.pproduct_id.save()
            all_preq.save()
            return HttpResponseRedirect(reverse('showpreq'))
        except Exception as rr:
            print("------------>delete error",rr)
    else:
        return redirect('adminin')

def AddRProduct(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            udata = Master.objects.get(id=pk)
            if udata.role=="RecyclingCompany":
                rc = Company.objects.get(master_id=udata)
                rpro_name = request.POST['rpname']  
                rpro_price = int(request.POST['rpprice'])
                rpro_image = request.FILES['rpimage']
                rpro_quantity = int(request.POST['rpqty'])
                rpro_desc = request.POST['rpdesc']
                if rpro_quantity<=0:
                    message= "Invalid quantity"
                    return render(request,"ep/addrproduct.html",{'qty':message})
                elif rpro_price<=0:
                    message= "Invalid price"
                    return render(request,"ep/addrproduct.html",{'qty':message})
                else:
                    newRProduct=RecycleProduct.objects.create(company_id=rc,rproduct_name=rpro_name,rproduct_price=rpro_price,rproduct_image=rpro_image,rproduct_quantity=rpro_quantity,rproduct_desc=rpro_desc)
                    message= "Product Added Successfully"
                    return render(request,"ep/addrproduct.html",{'msg':message})   
        except Exception as asp:
            print("------------>Add R Product",asp)
    else:
        return redirect('adminin')

def GetAllRProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="RecyclingCompany":
            pc = Company.objects.get(master_id=udata)
            allpproduct= RecycleProduct.objects.all().filter(company_id=pc)
            search = request.GET.get('search')
            if search !='' and search is not None:
                allpproduct= allpproduct.filter(rproduct_name__icontains= search)
            p = Paginator(allpproduct,5)
            page_num = request.GET.get('page',1)
            try:
                page = p.page(page_num)
            except PageNotAnInteger:
                page = p.page(1)
            except EmptyPage:
                page = p.page(p.num_pages)
            num =p.num_pages
            print(p.count)
            return render(request,"ep/allrproducts.html",{'key14':page,'count':p})
    else:
        return redirect('adminin')


def ShopProduct(request):
    try:
        all_preq = RecycleProduct.objects.all() 
        search = request.GET.get('search')
        sort = request.GET.get('sort')
        if sort !="" and sort is not None:
            if sort=="lth":
                print("FFFFFFFFFFFFFFFFFFEEEEEEEEEEEEEEEE")
                all_preq = all_preq.order_by('rproduct_price')
            elif sort =="htl":
                all_preq = all_preq.order_by('-rproduct_price')
        if search !='' and search is not None:
            all_preq = all_preq.filter(rproduct_name__icontains=search)
        p = Paginator(all_preq,5)
        page_num = request.GET.get('page',1)
        try:
            page = p.page(page_num)
        except PageNotAnInteger:
            page = p.page(1)
        except EmptyPage:
            page = p.page(p.num_pages)
        return render(request,"ep/shop-right.html",{'key15':page,'page':p})
    
    except Exception as saa:
        print("Show ----------------------------->",saa)
    
def DeleteRProduct(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            rdata = RecycleProduct.objects.get(pk=pk)
            rdata.delete()
            rp = request.session['id']
            url = f"/allrproducts/{rp}"
            return redirect(url)
        except Exception as okes:
            print("------------>delete error",okes)
    else:
        return redirect('adminin')

def RPUpdateButton(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            rp = RecycleProduct.objects.get(id=pk)
            print("IDt--------->",id)
            return render(request,"ep/rproduct_update.html",{"key16":rp})
        except Exception as rsa:
            print("Button Product--------->",rsa)
    else:
        return redirect('adminin')

def UpdateRProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            pro = RecycleProduct.objects.get(pk=pk)
            pro.rproduct_name = request.POST['pname']
            pro.rproduct_date = request.POST['pdate']
            pro.rproduct_price = request.POST['pprice']
            pro.rproduct_image = request.FILES['pimage']
            pro.rproduct_quantity = request.POST['pqty']
            pro.rproduct_desc = request.POST['pdesc']
            pro.save()
            pp = request.session['id']
            url = f"/allrproducts/{pp}"
            return redirect(url)
        except Exception as i:
            print("Image Product--------->",i)
    else:
        return redirect('adminin')
def ShowPro(request,pk):
    if "email" in request.session and "password" in request.session:

        pro_id = RecycleProduct.objects.get(id=pk)
        return render(request,"ep/shop-product-right.html",{'key17':pro_id})
    else:
        return redirect('adminin')
def ALogin(request):
    try:
        username = request.POST['username']
        password= request.POST['password']
        if username == "admin" and password == "admin":
            request.session['Role']=username
            request.session['password']=password
            return render(request,"ep/admin/aindex.html")
        else:
            message = "Invalid Username or Password"
            return render(request,"ep/admin/login.html",{'msg':message})
    except Exception as ll:
        print("Admin Login-------------------------------.",ll)
def SAdmin(request):
    if "Role" in request.session and "password" in request.session:
        all_preq = Master.objects.all()     
        return render(request,"ep/admin/tables.html",{'key18':all_preq})
    else:
        return redirect('alogin')       
def AButton(request,pk):
    if "Role" in request.session and "password" in request.session:
        try:
            ab = Master.objects.get(id=pk)
            print("IDt--------->",id)
            return render(request,"ep/admin/aupdate.html",{"key19":ab})
        except Exception as rsa:
            print("Button Product--------->",rsa)
    else:
        return redirect('alogin')
def AUpdate(request,pk):
    if "Role" in request.session and "password" in request.session:
        try:
            udata = Master.objects.get(id=pk)
            udata.is_verified = request.POST['verification'] 
            udata.is_active = request.POST['active'] 
            udata.is_updated = datetime.datetime.now()  
            udata.save()
            url = f"/showadmin/"
            return redirect(url)
        except Exception as au:
            print("Verify nai tha tu------------------->",au)
    else:
        return redirect('alogin')

def AdminPCData(request):
    if "Role" in request.session and "password" in request.session:
        pc_data = PlasticData.objects.all()
        pc_name = request.GET.get('coll')
        start_date = request.GET.get('sdate')
        end_date = request.GET.get('edate')
        if pc_name !='' and pc_name is not None and pc_name !="All":
            pc_data = pc_data.filter(plastic_id__pc_name__icontains=pc_name)
        if start_date !='' and start_date is not None:
            pc_data = pc_data.filter(collection_date__gte=start_date)
        if end_date !='' and end_date is not None:
            pc_data = pc_data.filter(collection_date__lte=end_date)
        data =  {'plastic':pc_data,'comp':Company.objects.all(),'plast':PlasticC.objects.all()}
        return render(request,'ep/admin/collector_data.html',data)
    else:
        return redirect('alogin')
class AdminPCDataPdf(View):
    def get(self, request, *args, **kwargs):
        try:
            pc_data = PlasticData.objects.all()
            pc_name = request.GET.get('pc')
            start_date = request.GET.get('sdate')
            end_date = request.GET.get('edate')
            if pc_name =='' and pc_name =='' and pc_name =='':
                msg = "Field Empty"
                return render(request,"ep/admin/collector_data_dl.html",{'error':msg})
            else:
                if pc_name !='' and pc_name is not None and pc_name !="All Collectors":
                    pc_data = pc_data.filter(plastic_id__pc_name__icontains=pc_name)
                if start_date !='' and start_date is not None:
                    pc_data = pc_data.filter(collection_date__gte=start_date)
                if end_date !='' and end_date is not None:
                    pc_data = pc_data.filter(collection_date__lte=end_date)
                if pc_data.exists():
                    data =  {'plastic':pc_data,'sdate':start_date,'edate':end_date}
                    pdf = render_to_pdf('ep/admin/collector_data_report.html', data)
                    if pdf:
                        response = HttpResponse(pdf, content_type='application/pdf')
                        filename = "Reports_%s_%s_%s.pdf" %(pc_name,start_date,end_date)
                        content = "filename='%s'" %(filename)
                        response['Content-Disposition'] = content
                        return response
                else:
                    msg = "No data"
                    return render(request,"ep/admin/collector_data_dl.html",{'error':msg})
        except Exception as pcpdf:
            msg = "No Internet Connection"
            print("pcPDDDDDDDDDDDDDDDDD",pcpdf)
            return render(request,"ep/admin/collector_data_dl.html",{'error':msg})
def AdminCustData(request):
    if "Role" in request.session and "password" in request.session:
        cust_data = CustomerData.objects.all()
        cust_name = request.GET.get('cust')
        start_date = request.GET.get('sdate')
        end_date = request.GET.get('edate')
        if cust_name !='' and cust_name is not None and cust_name !="All":
            cust_data = cust_data.filter(cust_id__fname__icontains=cust_name) 
        if start_date !='' and start_date is not None:
            cust_data = cust_data.filter(collection_date__gte=start_date)
        if end_date !='' and end_date is not None:
            cust_data = cust_data.filter(collection_date__lte=end_date)
        data =  {'customer':cust_data,'cust':Customer.objects.all()}
        return render(request,'ep/admin/customer_data.html',data)
    else:
        return redirect('alogin')
class AdminCustDataPdf(View):
   
    def get(self, request, *args, **kwargs):
        try:
            cust_data = CustomerData.objects.all()
            cust_name = request.GET.get('cust')
            start_date = request.GET.get('sdate')
            end_date = request.GET.get('edate')
            if cust_name =='' and start_date =='' and end_date =='':
                msg = "Field Empty"
                return render(request,"ep/admin/customer_data_dl.html",{'error':msg})
            else:
                if cust_name !='' and cust_name is not None and cust_name !="All Customers":
                    cust_data = cust_data.filter(cust_id__fname__icontains=cust_name) 
                if start_date !='' and start_date is not None:
                    cust_data = cust_data.filter(collection_date__gte=start_date)
                if end_date !='' and end_date is not None:
                    cust_data = cust_data.filter(collection_date__lte=end_date)
                if cust_data.exists():
                    data =  {'customer':cust_data,'sdate':start_date,'edate':end_date}
                    pdf = render_to_pdf('ep/admin/customer_data_report.html', data)
                    if pdf:
                        response = HttpResponse(pdf, content_type='application/pdf')
                        filename = "Reports_%s_%s_%s.pdf" %(cust_name,start_date,end_date)
                        content = "filename='%s'" %(filename)
                        response['Content-Disposition'] = content
                        return response
                else:
                    msg = "No data"
                    return render(request,"ep/admin/customer_data_dl.html",{'error':msg})
        except Exception as pdf:
            msg = "No Internet Connection"
            print("PDDDDDDDDDDDDDDDDD",pdf)
            return render(request,"ep/admin/customer_data_dl.html",{'error':msg})
def AdminRCData(request):
    if "Role" in request.session and "password" in request.session:
        rc_data = AddToCart.objects.all().filter(payment_status='TXN_SUCCESS')
        rc_name = request.GET.get('rc')
        start_date = request.GET.get('sdate')
        end_date = request.GET.get('edate')
        if rc_name !='' and rc_name is not None and rc_name !="All":
            rc_data = rc_data.filter(company_id__comp_name__icontains=rc_name) 
        if start_date !='' and start_date is not None:
            rc_data = rc_data.filter(order_date__gte=start_date)
        if end_date !='' and end_date is not None:
            rc_data = rc_data.filter(order_date__lte=end_date)
        data =  {'company':rc_data,'rc':Company.objects.all()}
        return render(request,'ep/admin/company_data.html',data)
    else:
        return redirect('alogin')
class AdminRCDataPdf(View):
    def get(self, request, *args, **kwargs):
        try:
            rc_data = AddToCart.objects.all().filter(payment_status='TXN_SUCCESS')
            rc_name = request.GET.get('rc')
            start_date = request.GET.get('sdate')
            end_date = request.GET.get('edate')
            if rc_name =='' and rc_name =='' and rc_name =='':
                msg = "Field Empty"
                return render(request,"ep/admin/company_data_dl.html",{'error':msg})
            else:
                if rc_name !='' and rc_name is not None and rc_name !="All Companies":
                    rc_data = rc_data.filter(company_id__comp_name__icontains=rc_name) 
                if start_date !='' and start_date is not None:
                    rc_data = rc_data.filter(order_date__gte=start_date)
                if end_date !='' and end_date is not None:
                    rc_data = rc_data.filter(order_date__lte=end_date)
                if rc_data.exists():
                    data =  {'company':rc_data,'sdate':start_date,'edate':end_date}
                    pdf = render_to_pdf('ep/admin/company_data_report.html', data)
                    if pdf:
                        response = HttpResponse(pdf, content_type='application/pdf')
                        filename = "Reports_%s_%s_%s.pdf" %(rc_name,start_date,end_date)
                        content = "filename='%s'" %(filename)
                        response['Content-Disposition'] = content
                        return response
                else:
                    msg = "No data"
                    return render(request,"ep/admin/company_data_dl.html",{'error':msg})
        except Exception as rcpdf:
            msg = "No Internet Connection"
            print("RCPDDDDDDDDDDDDDDDDD",rcpdf)
            return render(request,"ep/admin/company_data_dl.html",{'error':msg})
def AddCart(request):
    if "email" in request.session and "password" in request.session:
        try:
            atcdata = Master.objects.get(id=request.session['id'])
            if atcdata.role=="customer":
                atc = Customer.objects.get(master_id=atcdata)
                print("Cust--------------->",atc)
                pro_id = request.POST['pid']
                rp = RecycleProduct.objects.get(id =pro_id)
                print("Recycle--------------->",rp)
                atc_price = int(request.POST['atcprice'])
                
                atc_qty = int(request.POST['product_quantity'])
                atc_subtotal = int(atc_price * atc_qty)
                comp = rp.company_id.id
                comp_id = Company.objects.get(id=comp)
                newAddCart=AddToCart.objects.create(rp_id=rp,cust_id=atc,cart_price=atc_price,cart_quantity=atc_qty,cart_subtotal=atc_subtotal,company_id=comp_id)
                rp.rproduct_quantity-=atc_qty
                rp.save()
                ppp = request.session['id']
                url = f"/showthecart/{ppp}"
                return redirect(url)
                
        except Exception as aaaa:
            print("Add to cart nai thatu--------------->",aaaa)
    else:
        return redirect('signin')

def ShowCart(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            cdata = Master.objects.get(id=pk)
            total = 0
            if cdata.role=="customer":
                cust = Customer.objects.get(master_id=cdata)
                show = AddToCart.objects.all().filter(cust_id=cust,payment_status="pending")
                for t in show:
                    total += t.cart_subtotal
                print("Totallll",total)
                return render(request,"ep/customercart.html",{"key20":show, "total": total})
        except Exception as skc:
            print("nai avtu---------------",skc)
    else:
        return redirect('signin')

def loadCart(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            cdata = Master.objects.get(id=pk)
            total = 0
            cust = Customer.objects.get(master_id=cdata)
            show = AddToCart.objects.all().filter(cust_id=cust)
            for t in show:
                total += t.cart_subtotal
            print(total)
            return {"key20": show, "total": total}
        except Exception as err:
            print(err)
    else:
        return redirect('signin')

def DelCart(request,pk):
    if "email" in request.session and "password" in request.session:
        r =  RecycleProduct.objects.get(id=request.POST['rcp'])
        qty = int(request.POST['product_quantity'])
        print("dellll",qty)
        ddata = AddToCart.objects.get(pk=pk)
        r.rproduct_quantity+=qty
        r.save()
        ddata.delete()
        p = request.session['id']
        url = f"/showthecart/{p}"
        return redirect(url)
    else:
        return redirect('signin')

def UpdateCart(request,pk):
    if "email" in request.session and "password" in request.session:
        rcp =  RecycleProduct.objects.get(id=request.POST['rcp'])
        print("RCPPPPPPP",rcp)
        adata = AddToCart.objects.get(pk=pk)
        quant = int(request.POST['product_quantity'])
        if quant > adata.cart_quantity:
            update = quant-adata.cart_quantity
            rcp.rproduct_quantity-=update 
            rcp.save()
            adata.cart_quantity = quant
            adata.cart_subtotal = quant*adata.cart_price
            adata.save()
            ppp = request.session['id']
            url = f"/showthecart/{ppp}"
            return redirect(url)
        elif quant < adata.cart_quantity:
            update =  adata.cart_quantity-quant
            rcp.rproduct_quantity+=update
            rcp.save()
            adata.cart_quantity = quant
            adata.cart_subtotal = quant*adata.cart_price
            adata.save()
            inc = request.session['id']
            url = f"/showthecart/{inc}"
            return redirect(url)
        else:
            adata.cart_quantity = quant
            adata.cart_subtotal = quant*adata.cart_price
            adata.save()
            sam = request.session['id']
            url = f"/showthecart/{sam}"
            return redirect(url)
    else:
        return redirect('signin')

def CartCheckout(request,pk):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=request.session['id'])
        total = 0
        if udata.role == "customer":
            cdata = Customer.objects.get(master_id=udata)
            cartdata = AddToCart.objects.all().filter(cust_id=cdata,payment_status="pending")
            for t in cartdata:
                    total += t.cart_subtotal
            return render(request,"ep/customer_cartcheckout.html",{"key22":cartdata,"total":total,"key23":cdata})
    else:
        return redirect('signin')

def Schedule(request):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=request.session['id'])
        if udata.role == "customer":
            cdata = Customer.objects.get(master_id=udata)
            cname = request.POST['pickup_name']
            email = cdata.master_id.email
            cnumber = request.POST['pickup_number']
            stime = request.POST['pickup_date_time']
            scomment = request.POST['pickup_comment']
            pickupschedule = ScheduleOrder.objects.create(cust_id=cdata,cust_name=cname,cust_number=cnumber,sc_date_time=stime,sc_comment=scomment)

            email_subject = "Plastic Pickup Request Sent"
            PickupSent(email_subject,'mail_template',email,{'fullname':cname,'contact':cnumber,'pickup_datetime':pickupschedule.sc_date_time,'pickup_details':scomment})
            message = "Pickup Request Sent!"
            return render(request,"ep/index-2.html",{'msg':message})
            
    else:
        return redirect('signin')
def ShowPickUp(request):     
    if "email" in request.session and "password" in request.session:
        pick = ScheduleOrder.objects.all()
        status = request.GET.get('status')
        search = request.GET.get('search')
        if status !='' and status is not None and status!="All":
            pick = pick.filter(pickup_status=status)
        if search !='' and search is not None:
            pick = pick.filter(sc_comment__icontains=search)| pick.filter(sc_date_time__icontains=search) | pick.filter(cust_name__icontains=search) | pick.filter(cust_number__icontains=search)
        p = Paginator(pick,5)
        page_num = request.GET.get('page')
        try:
            cust_pick = p.page(page_num)
        except PageNotAnInteger:
            cust_pick = p.page(1)
        except EmptyPage:
            cust_pick = p.page(p.num_pages)
        return render(request,"ep/showpickupreq.html",{'pickup':cust_pick,'page':p})
    else:   
        return redirect('adminin')
def PickUpStatus(request,pk):
    if "email" in request.session and "password" in request.session:
        master = Master.objects.get(id=request.session['id'])
        pick = ScheduleOrder.objects.get(id=pk)
        plastic_id = PlasticC.objects.get(master_id=master)
        if request.POST['status'] == "Accepted":
            pick.pickup_status = request.POST['status']
            pick.save()
            email_subject = "Plastic Pickup Request Accepted"
            PickupAccept(email_subject,'mail_template',pick.cust_id.master_id.email,{'pcname':plastic_id.pc_name,'pccontact':plastic_id.pc_contact,'pickup_datetime':pick.sc_date_time,'pickup_details':pick.sc_comment})
            return HttpResponseRedirect(reverse('pickuprequests'))
        if request.POST['status'] == "Rejected":
            pick.pickup_status = "pending"
            pick.save()
            # PickupReject(email_subject,'mail_template',pick.cust_id.master_id.email,{'pcname':plastic_id.pc_name,'pccontact':plastic_id.pc_contact,'pickup_datetime':pick.sc_date_time,'pickup_details':pick.sc_comment})
            return HttpResponseRedirect(reverse('pickuprequests')) 
    else:   
        return redirect('adminin')

def OrderDetails(request):
    if "email" in request.session and "password" in request.session:
        user = Master.objects.get(id=request.session['id'])
        if user.role == "RecyclingCompany":
            rc = Company.objects.get(master_id=user)
            cust = Customer.objects.all()
            for rp in RecycleProduct.objects.all().filter(company_id=rc):
                rc = rp.company_id
            order = AddToCart.objects.all().filter(company_id=rc,payment_status='TXN_SUCCESS')
            cust_name = request.GET.get('name')
            print("SSSSSSSSSSSSSSSSSsCC",cust_name)
            if cust_name !='' and cust_name is not None:
                order = order.filter(cust_id__fname__icontains=cust_name)
            search = request.GET.get('search')
            if search !='' and search is not None:
               order= order.filter(rp_id__rproduct_name__icontains= search) | order.filter(cust_id__fname__icontains= search) | order.filter(cust_id__lname__icontains= search)
            p = Paginator(order,5)
            page_num = request.GET.get('page',1)
            try:
                page = p.page(page_num)
            except PageNotAnInteger:
                page = p.page(1)
            except EmptyPage:
                page = p.page(p.num_pages)
            num =p.num_pages
            print(p.count)
            return render(request,"ep/company_order-received.html",{"order":page,'count':p,'cust':cust})
        if user.role == "customer":
            cust = Customer.objects.get(master_id=user)
            order = AddToCart.objects.all().filter(cust_id=cust).exclude(payment_status="pending")
            search = request.GET.get('search')
            status = request.GET.get('status')
            if status !="" and status is not None:
                order = order.filter(order_status__icontains=status)
            if search !='' and search is not None:
                order= order.filter(rp_id__rproduct_name__icontains= search) | order.filter(order_status__icontains=search) | order.filter(order_date__icontains=search)
            p = Paginator(order,5)
            page_num = request.GET.get('page')
            try:
                cust_orders = p.page(page_num)
            except PageNotAnInteger:
                cust_orders = p.page(1)
            except EmptyPage:
                cust_orders = p.page(p.num_pages)
            print("PPHAAAAAAAAAAAAA0",p.num_pages)
            return render(request,"ep/customer_orders.html",{"order":cust_orders,"page":p})
        if user.role == "PlasticCollector":
            pc = PlasticC.objects.get(master_id=user)
            comp = Company.objects.all()
            
            for pp in PlasticProduct.objects.all().filter(plasticc_id=pc):
                pc = pp.plasticc_id
            order = PlasticRequest.objects.all().filter(plasticc_id=pc,payment_status='TXN_SUCCESS')
            cust_name = request.GET.get('name')
            if cust_name !='' and cust_name is not None and cust_name!="All":
                order = order.filter(comp_id__comp_name__icontains=cust_name)
            search = request.GET.get('search')
            if search !='' and search is not None:
                order= order.filter(comp_id__comp_name__icontains= search) 
                
            p = Paginator(order,5)
            page_num = request.GET.get('page',1)
            try:
                page = p.page(page_num)
            except PageNotAnInteger:
                page = p.page(1)
            except EmptyPage:
                page = p.page(p.num_pages)
            num =p.num_pages
            print(p.count)
            return render(request,"ep/collector_order-received.html",{"order":page,'comp':comp,'count':p})
    else:   
            return redirect('adminin')
def OrderInfo(request,pk):
    if "email" in request.session and "password" in request.session:
        odetails = AddToCart.objects.get(id=pk)
        cust = int(odetails.cust_id.id)
        data = AddToCart.objects.all().filter(cust_id=cust)
        count=0
        for c in (data): 
            if c.payment_status=='TXN_SUCCESS':
                count=count+1
        return render(request,"ep/company_order-details.html",{"odetails":odetails,'count':count})
    else:   
            return redirect('adminin')
def SaveOrder(request,pk):
    if "email" in request.session and "password" in request.session:
        data = AddToCart.objects.get(id=pk)
        data.order_status = request.POST['ostatus']
        data.save()
        return HttpResponseRedirect(reverse('custorder')) 
    else:   
            return redirect('adminin')
def AddData(request):
    if "email" in request.session and "password" in request.session:
        user = Master.objects.get(id=request.session['id'])
        if user.role == "PlasticCollector":
            customer_id = Customer.objects.get(id=request.POST['c_id'])
            plastic_id = PlasticC.objects.get(master_id=user)
            total_collect = request.POST['totalcollect']
            use = request.POST['usage']
            waste = request.POST['wastage']
            date = request.POST['date_coll']
            newData = CustomerData.objects.create(cust_id=customer_id,plastic_id=plastic_id,total_collection=total_collect,usage=use,wastage=waste,collection_date=date)
            message = "Data Added!"
            return render(request,"ep/customer_data.html",{"cust":Customer.objects.all(),"msg":message})
            
        if user.role == "RecyclingCompany":
            recycling_id = Company.objects.get(master_id=user)
            plastic_id = PlasticC.objects.get(pc_name=request.POST['rc_id'])
            total_collect = request.POST['totalcollect']
            use = request.POST['usage']
            waste = request.POST['wastage']
            date = request.POST['date_coll']
            types = request.POST['types']
         
            if int(use) + int(waste) == int(total_collect) :
                newData = PlasticData.objects.create(rc_id=recycling_id,plastic_id=plastic_id,total_collection=total_collect,usage=use,wastage=waste,collection_date=date,types=types)
                message = "Data Added!"
                return render(request,"ep/rc_data.html",{"rc":PlasticC.objects.all(),"msg":message,'image':recycling_id.comp_image})
            else:
                message = "Invalid Data"
                return render(request,"ep/rc_data.html",{'error':message})
    else:   
        return redirect('adminin')
def CompanyOrderInfo(request,pk):
    if "email" in request.session and "password" in request.session:
        odetails = PlasticRequest.objects.get(id=pk)
        comp = int(odetails.comp_id.id)
        data = PlasticRequest.objects.all().filter(comp_id=comp)
        count=0
        for c in (data): 
            if c.payment_status=='TXN_SUCCESS':
                count=count+1
        total = odetails.request_quantity * odetails.pproduct_id.pproduct_price
        return render(request,"ep/collector_order-details.html",{"odetails":odetails,'count':count,'total':total})
    else:   
            return redirect('adminin')

def Report(request,pk):
    if "email" in request.session and "password" in request.session:
        user= Master.objects.get(id=pk)
        if user.role == "customer":
            # rFilter = ReportFilter(request.GET,queryset=report)
            # report = rFilter.qs {"reportFilter":rFilter,}
            cust = Customer.objects.get(master_id=user)
            report=CustomerData.objects.all().filter(cust_id=cust)
            pc_name = request.GET.get('pc_name')
            plast = PlasticC.objects.all()
            if pc_name != '' and pc_name is not None:
                report = report.filter(plastic_id__pc_name__icontains=pc_name)

            p = Paginator(report,5)
            page_num = request.GET.get('page')
            try:
                page = p.page(page_num)
            except PageNotAnInteger:
                page = p.page(1)
            except EmptyPage:
                page = p.page(p.num_pages)
            num =p.num_pages
            totalcollection = 0
            totalusage = 0
            totalwastage = 0
            for i in report:
                totalcollection += i.total_collection
            for u in report:
                totalusage+=u.usage
            for w in report:
                totalwastage+=w.wastage 
            
            return render(request,"ep/customer_report.html",{"plast":plast,"report":page,"totalcollection":totalcollection,"t_usage":totalusage,"t_waste":totalwastage,'total':p})

        if user.role == "PlasticCollector":
            report_r=PlasticData.objects.all().filter(plastic_id__master_id__id=request.session['id'])
            pc_name = request.GET.get('pc_name')
            comp = Company.objects.all()
            if pc_name != '' and pc_name is not None and pc_name !="All":
                report_r = report_r.filter(rc_id__comp_name=pc_name)

            p = Paginator(report_r,5)
            page_num = request.GET.get('page')
            try:
                page = p.page(page_num)
            except PageNotAnInteger:
                page = p.page(1)
            except EmptyPage:
                page = p.page(p.num_pages)
            num =p.num_pages

            totalcollection_r = 0
            totalusage_r = 0
            totalwastage_r = 0
            count_r =0
            for c in enumerate(report_r): 
                count_r=count_r+1
                print(count_r)
            for i in report_r:
                totalcollection_r += i.total_collection
            for u in report_r:
                totalusage_r+=u.usage
            for w in report_r:
                totalwastage_r+=w.wastage
            return render(request,"ep/plastic_data.html",{"comp":comp,"report_r":page,"totalcollection_r":totalcollection_r,"count_r":count_r,"t_usage_r":totalusage_r,"t_waste_r":totalwastage_r,'total':p})

    else:   
        return redirect('signin')
class ReportPdf(View):
    def get(self, request, *args, **kwargs):
        if request.session['Role'] =="customer":
            try:
                report= CustomerData.objects.filter(cust_id__master_id__id=request.session['id'])
                name = request.GET['pc_name']
                start_date = request.GET['sdate']
                end_date = request.GET['edate']
                if name =='' and start_date =='' and end_date =='':
                    msg = "Field empty"
                    return render(request,"ep/download.html",{'error':msg})
                else:
                    if name !='' and name is not None and name !='All Collectors':
                        report = report.filter(plastic_id__pc_name=name)
                    if start_date !='' and start_date is not None:
                        report = report.filter(collection_date__gte=start_date)
                    if end_date !='' and end_date is not None:
                        report =report.filter(collection_date__lte=end_date)
                    if report.exists():
                        data = {'report':report,'sdate':start_date,'edate':end_date}
                        pdf = render_to_pdf('ep/report.html', data)
                        if pdf:
                            response = HttpResponse(pdf, content_type='application/pdf')
                            filename = "Reports_%s_%s_%s.pdf" %(name,start_date,end_date)
                            content = "filename='%s'" %(filename)
                            response['Content-Disposition'] = content
                            return response
                    else:
                        msg = "No data"
                        return render(request,"ep/download.html",{'error':msg})
            except Exception as pdf:
                msg = "No Internet Connection"
                print("PDDDDDDDDDDDDDDDDD",pdf)
                return render(request,"ep/download.html",{'error':msg})
        if request.session['Role'] == "RecyclingCompany":
            try:
                orders= AddToCart.objects.all().filter(company_id__master_id=request.session['id'],payment_status="TXN_SUCCESS")
                name = request.GET['cust']
                start_date = request.GET['sdate']
                end_date = request.GET['edate']
                if name =='' and start_date =='' and end_date =='':
                    msg = "Field empty"
                    return render(request,"ep/company_orders_dl.html",{'error':msg})
                else:
                    if name !='' and name is not None and name !='All Customers':
                        orders = orders.filter(cust_id__fname=name)
                    if start_date !='' and start_date is not None:
                        orders = orders.filter(order_date__gte=start_date)
                    if end_date !='' and end_date is not None:
                        orders =orders.filter(order_date__lte=end_date)
                    if orders.exists():
                        data = {'orders':orders,'sdate':start_date,'edate':end_date}
                        pdf = render_to_pdf('ep/report.html', data)
                        if pdf:
                            response = HttpResponse(pdf, content_type='application/pdf')
                            filename = "Reports_%s_%s_%s.pdf" %(name,start_date,end_date)
                            content = "filename='%s'" %(filename)
                            response['Content-Disposition'] = content
                            return response
                    else:
                        msg = "No data"
                        return render(request,"ep/company_orders_dl.html",{'error':msg})
            except Exception as pdf:
                msg = "No Internet Connection"
                print("PDDDDDDDDDDDDDDDDD",pdf)
                return render(request,"ep/company_orders_dl.html",{'error':msg})
        if request.session['Role'] == "PlasticCollector":
            try:
                orders=PlasticData.objects.all().filter(plastic_id__master_id__id=request.session['id'])
                name = request.GET.get('comp')
                start_date = request.GET['sdate']
                end_date = request.GET['edate']
                if name =='' and start_date =='' and end_date =='':
                    msg = "Field empty"
                    return render(request,"ep/plastic_data_dl.html",{'error':msg})
                else:
                    if name !='' and name is not None and name !='All Companies':
                        orders = orders.filter(rc_id__comp_name=name)
                    if start_date !='' and start_date is not None:
                        orders = orders.filter(collection_date__gte=start_date)
                    if end_date !='' and end_date is not None:
                        orders =orders.filter(collection_date__lte=end_date)
                    if orders.exists():
                        data = {'plastic':orders,'sdate':start_date,'edate':end_date}
                        pdf = render_to_pdf('ep/report.html', data)
                        if pdf:
                            response = HttpResponse(pdf, content_type='application/pdf')
                            filename = "Reports_%s_%s_%s.pdf" %(name,start_date,end_date)
                            content = "filename='%s'" %(filename)
                            response['Content-Disposition'] = content
                            return response
                    else:
                        msg = "No data"
                        return render(request,"ep/plastic_data_dl.html",{'error':msg})
            except Exception as pdf:
                msg = "No Internet Connection"
                print("PDDDDDDDDDDDDDDDDD",pdf)
                return render(request,"ep/company_orders_dl.html",{'error':msg})
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
                received_data['message'] = "Checksum Matched"
                
                print(paytm_params['ORDERID'])
                # user = Master.objects.get(id=paytm_params['ORDERID'])
                # cust = Customer.objects.get(master_id=user)
                for i in AddToCart.objects.all().filter(transaction_id=paytm_params['ORDERID']):
                    i.payment_status = paytm_params['STATUS'] 
                    if paytm_params['STATUS'] == "TXN_SUCCESS":
                        i.order_status = "Order Placed"
                    else:
                        i.order_status = "Failed"
                    i.save()    
        else:
            received_data['message'] = "Checksum Mismatched"
            
            print("Payment3",paytm_params['STATUS'])

            return render(request, 'ep/callback.html', context=received_data)
        return render(request, 'ep/callback.html', context=received_data)

def initiate_payment(request):
    udata = Master.objects.get(id=request.session['id'])
    if udata.role == "customer":
        try:
            cdata = Master.objects.get(email=request.session['email'])
            amount = int(request.POST['total'])
            print("-------------------------------------------",amount)
            # user = authenticate(request, username=username, password=password)
        except:
            return render(request, 'ep/customer_cartcheckout.html')
        
        transaction = Transaction.objects.create(made_by=cdata, amount=amount)
    
        transaction.save()  
        cid = request.POST['cid']
        print(cid)
        print("TEREEEEEEEEE",transaction.id)

        cust_id  =Customer.objects.get(id=cid)
        pro_id = RecycleProduct.objects.get(id=request.POST['proid'])
        qty =request.POST['cqty'] 
        cmt =request.POST.get('instructions')
        print("ddddddd",cmt)
        print("ffffffffffffffff",qty) 
        for i in AddToCart.objects.all().filter(cust_id=cust_id,payment_status="pending"):
            i.transaction_id = transaction
            i.order_comment = cmt
            i.save()    
        merchant_key = settings.PAYTM_SECRET_KEY

        params = (
            ('MID', settings.PAYTM_MERCHANT_ID),
            ('ORDER_ID', str(transaction.id)),
            ('CUST_ID', request.POST['cid']),
            ('TXN_AMOUNT', str(transaction.amount)),
            ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
            ('WEBSITE', settings.PAYTM_WEBSITE),
            # ('EMAIL', request.user.email),
            # ('MOBILE_N0', '9911223388'),
            ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
            ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
            # ('PAYMENT_MODE_ONLY', 'NO'),
        )

        paytm_params = dict(params)
        checksum = generate_checksum(paytm_params, merchant_key)

        transaction.checksum = checksum
        transaction.save()
        
        paytm_params['CHECKSUMHASH'] = checksum
        #print('SENT: ', paytm_params['RESPCODE'])
        return render(request, 'ep/redirect.html', context=paytm_params)
    
    elif udata.role == "RecyclingCompany":
        try:
            cdata = Master.objects.get(email=request.session['email'])
            amount = int(request.POST['total'])
            print("-------------------------------------------",amount)
            # user = authenticate(request, username=username, password=password)
        except:
            return render(request, 'ep/company_cartcheckout.html')
        
        transaction = Transaction.objects.create(made_by=cdata, amount=amount)
        
        transaction.save()
        comp = request.POST['comp']
        req = PlasticRequest.objects.get(id=comp,payment_status="pending")
        req.transaction_id = transaction
        req.save()
        # pstatus = request.POST['paystatus']
        
        merchant_key = settings.PAYTM_SECRET_KEY

        params = (
            ('MID', settings.PAYTM_MERCHANT_ID),
            ('ORDER_ID', str(transaction.id)),
            ('CUST_ID', request.POST['comp']),
            ('TXN_AMOUNT', str(transaction.amount)),
            ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
            ('WEBSITE', settings.PAYTM_WEBSITE),
            # ('MOBILE_N0', '9911223388'),
            ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
            ('CALLBACK_URL', 'http://127.0.0.1:8000/second/'),
            # ('PAYMENT_MODE_ONLY', 'NO'),
        )
        paytm_params = dict(params)
        checksum = generate_checksum(paytm_params, merchant_key)

        transaction.checksum = checksum
        transaction.save()
    
        paytm_params['CHECKSUMHASH'] = checksum
        
        return render(request, 'ep/redirect.html', context=paytm_params)

@csrf_exempt
def second(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        
        
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
                
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
            plastic = PlasticRequest.objects.get(transaction_id=paytm_params['ORDERID'])
            plastic.payment_status=paytm_params['STATUS']
            plastic.save()   
        else:
            received_data['message'] = "Checksum Mismatched"
            
            print("Payment3",paytm_params['STATUS'])

            return render(request, 'ep/callback.html', context=received_data)
        return render(request, 'ep/callback.html', context=received_data)

def Logout(request):
    if request.session['Role'] == 'admin':
        del request.session['Role']
        del request.session['password']
        return HttpResponseRedirect(reverse('alogin')) 
    if request.session['Role'] == "customer":
        del request.session['email'] 
        del request.session['password']   
        del request.session['id']  
        del request.session['Role']   
        del request.session['Firstname']  
        del request.session['Lastname']  
        del request.session['Gender']  
        del request.session['State']   
        return HttpResponseRedirect(reverse('signin')) 
    
    if request.session['Role'] == "RecyclingCompany":
        del request.session['email']  
        del request.session['password']  
        del request.session['id']  
        del request.session['Role']   
        del request.session['Cname']  
        del request.session['Cadd']  
        del request.session['Ccon']  
        del request.session['Cfb']   
        del request.session['Cins']   
        del request.session['Clin']   
        del request.session['Ctwit']  
        del request.session['Cweb']  
        del request.session['Ofname'] 
        del request.session['Olname']    
        del request.session['Ogen'] 
        del request.session['Ocon']  
        del request.session['Oemail']
        return HttpResponseRedirect(reverse('adminin')) 

    if request.session['Role'] == "PlasticCollector":
        del request.session['email'] 
        del request.session['password']   
        del request.session['id']  
        del request.session['Role']   
        del request.session['Pcname']  
        del request.session['Pcadd']  
        del request.session['Pccon']  
        del request.session['Pcfb']   
        del request.session['Pcins']   
        del request.session['Pclin']   
        del request.session['Pctwit']  
        del request.session['Pcweb']  
        del request.session['Ofname'] 
        del request.session['Olname']    
        del request.session['Ogen'] 
        del request.session['Ocon']  
        del request.session['Oemail'] 
        return HttpResponseRedirect(reverse('adminin')) 
    
    