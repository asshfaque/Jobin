from django.shortcuts import render, redirect
from JobBackend.models import CompanyDb, jobDb, CountryDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from JobFrontend.models import FrontJobDb, FrontCompanyDb, FrontCountryDb, Contactusdb


# Create your views here.

def Index(request):
    return render(request, "Index.html")


def AddCompany(request):
    cry = CountryDb.objects.all()
    return render(request, "AddCompany.html", {'cry': cry})


def CompanySave(req):
    if req.method == "POST":
        cn = req.POST.get('companyName')
        ci = req.POST.get('companyInfo')
        c = req.POST.get('country')
        cp = req.FILES['companyProfile']
        obj = CompanyDb(companyName=cn, information=ci, country=c, companyProfile=cp)
        obj.save()
        messages.success(req, "Company Saved Successfully")
        return redirect(AddCompany)


def CompanyView(req):
    data = CompanyDb.objects.all()
    return render(req, "ViewCompanies.html", {'data': data})


def EditCompany(req):
    data = CompanyDb.objects.all()
    return render(req, "EditCompany.html", {'data': data})


def UpdateCompany(req, dataid):
    cr = CountryDb.objects.all()
    company = CompanyDb.objects.get(id=dataid)
    return render(req, "UpdateCompany.html", {'company': company, 'cr': cr})


def UpdateCompanyButton(req, dataid):
    if req.method == "POST":
        cn = req.POST.get('companyName')
        ci = req.POST.get('companyInfo')
        c = req.POST.get('country')
        try:
            img = req.FILES['companyProfile']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CompanyDb.objects.get(id=dataid).companyProfile
        CompanyDb.objects.filter(id=dataid).update(companyName=cn, information=ci, country=c, companyProfile=file)
        messages.success(req, "Company Updated Successfully")
        return redirect(EditCompany)


def DeleteCompany(req, dataid):
    compny = CompanyDb.objects.filter(id=dataid)
    compny.delete()
    messages.warning(req, "Company Deleted Successfully")
    return redirect(EditCompany)


def AddJob(request):
    data = CompanyDb.objects.all()
    return render(request, "AddJob.html", {'data': data})


def JobSave(req):
    if req.method == "POST":
        cn = req.POST.get('companyName')
        j = req.POST.get('job')
        jd = req.POST.get('jobDetails')
        q = req.POST.get('qualification')
        e = req.POST.get('experience')
        d = req.POST.get('date')
        t = req.POST.get('time')
        l = req.POST.get('location')
        ctn = req.POST.get('contactNumber')
        obj = jobDb(companyName=cn, job=j, jobDetails=jd, qualification=q, experience=e, date=d, time=t, location=l,
                    contactNumber=ctn)
        obj.save()
        messages.success(req, "Job saved Successfully")
        return redirect(AddJob)


def JobView(req):
    Data = jobDb.objects.all()
    return render(req, "ViewJob.html", {'Data': Data})


def EditJob(req):
    Data = jobDb.objects.all()
    return render(req, "EditJob.html", {'Data': Data})


def UpdateJob(req, dataId):
    job = jobDb.objects.get(id=dataId)
    more = CompanyDb.objects.all()
    return render(req, "UpdateJob.html", {'job': job, 'more': more})


def Settings(req):
    return render(req, "Settings.html")


def UpdateJobButton(req, dataId):
    if req.method == "POST":
        cn = req.POST.get('companyName')
        j = req.POST.get('job')
        jd = req.POST.get('jobDetails')
        q = req.POST.get('qualification')
        e = req.POST.get('experience')
        d = req.POST.get('date')
        t = req.POST.get('time')
        l = req.POST.get('location')
        cnm = req.POST.get('contactNumber')
        jobDb.objects.filter(id=dataId).update(companyName=cn, job=j, jobDetails=jd, qualification=q, experience=e,
                                               date=d, time=t, location=l, contactNumber=cnm)
        messages.success(req, "job Updated Successfully")
        return redirect(EditJob)


def DeleteJob(req, dataId):
    job = jobDb.objects.filter(id=dataId)
    job.delete()
    messages.warning(req, "Job Deleted Successfully")
    return redirect(EditJob)


def AddCountry(request):
    return render(request, 'AddCountry.html')


def CountrySave(req):
    if req.method == "POST":
        cn = req.POST.get('countryName')
        l = req.POST.get('location')
        cf = req.FILES['countryFlag']
        obj = CountryDb(countryName=cn, location=l, countryFlag=cf)
        obj.save()
        messages.success(req, "Country Saved Successfully")
        return redirect(AddCountry)


def CountryView(req):
    data = CountryDb.objects.all()
    return render(req, "ViewCountry.html", {'data': data})


def EditCountry(req):
    more = CountryDb.objects.all()
    return render(req, "EditCountry.html", {'more': more})


def UpdateCountry(req, dataid):
    country = CountryDb.objects.get(id=dataid)
    return render(req, "UpdateCountry.html", {'country': country})


def UpdateCountryButton(req, dataid):
    if req.method == "POST":
        cn = req.POST.get('countryName')
        l = req.POST.get('location')
        try:
            img = req.FILES['countryFlag']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CountryDb.objects.get(id=dataid).countryFlag
        CountryDb.objects.filter(id=dataid).update(countryName=cn, location=l, countryFlag=file)
        messages.success(req, "Country Updated Successfully")
        return redirect(EditCountry)


def DeleteCountry(req, dataid):
    cntry = CountryDb.objects.filter(id=dataid)
    cntry.delete()
    messages.warning(req, "Country Deleted Successfully")
    return redirect(EditCountry)


def Login(req):
    return render(req, "Login.html")


def AdminLogin(req):
    if req.method == "POST":
        un = req.POST.get('user_name')
        pd = req.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pd)
            if user is not None:
                login(req, user)
                req.session['username'] = un
                req.session['password'] = pd
                return redirect(Index)
            else:
                return redirect(Login)
        else:
            return redirect(Login)


def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Login)


def DailyUpdates(req):
    country = FrontCountryDb.objects.all()
    return render(req, "DailyJobUpdates.html", {'country': country})


def DailyUpdates1(req):
    company = FrontCompanyDb.objects.all()
    return render(req, "DailyJobUpdates1.html", {'company': company})


def DailyUpdates2(req):
    job = FrontJobDb.objects.all()
    return render(req, "DailyJobUpdates2.html", {'job': job})


def Deleteall(req, dataid):
    cntry = FrontCountryDb.objects.filter(id=dataid)
    cmpny = FrontCompanyDb.objects.filter(id=dataid)
    jb = FrontJobDb.objects.filter(id=dataid)
    cntry.delete()
    cmpny.delete()
    jb.delete()
    messages.warning(req, "User Request Deleted Successfully")
    return redirect(DailyUpdates)


def ContactDetails(req):
    msg = Contactusdb.objects.all()
    return render(req, "ContactDetails.html", {'msg': msg})


def contactdlt(req, data):
    dlt = Contactusdb.objects.filter(id=data)
    dlt.delete()
    return redirect(ContactDetails)
