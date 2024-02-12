from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from JobBackend.models import jobDb, CompanyDb, CountryDb
from JobFrontend.models import CreateAccountDb, FrontCountryDb, FrontCompanyDb, FrontJobDb, Contactusdb
from django.contrib import messages


# Create your views here.
def Home(request):
    return render(request, "Home.html")


def Jobs(request):
    job = jobDb.objects.all()
    return render(request, "Jobs.html", {'job': job})


def Company(req):
    company = CompanyDb.objects.all()
    return render(req, "Companies.html", {'company': company})


def jobFilter(req, cmp_name):
    data = jobDb.objects.filter(companyName=cmp_name)
    return render(req, "JobFilter.html", {'data': data})


def Country(req):
    country = CountryDb.objects.all()
    return render(req, "Countries.html", {'country': country})


def CompanyFilter(req, cmpny_name):
    data = CompanyDb.objects.filter(country=cmpny_name)
    return render(req, "CompnyFilter.html", {'data': data})


def SingleJob(req, singleId):
    data = jobDb.objects.get(id=singleId)
    return render(req, "SingleJob.html", {'data': data})


def LoginSignin(req):
    return render(req, "Login&Signin.html")


def CreateAccount(req):
    if req.method == "POST":
        n = req.POST.get('username')
        e = req.POST.get('email')
        pwd = req.POST.get('password')
        p = req.FILES['profile']
        obj = CreateAccountDb(username=n, email=e, password=pwd, profile=p, )
        obj.save()
        messages.success(req, "Account Created successfully")
        return redirect(LoginSignin)


def UserLogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        p = request.POST.get('password')
        if CreateAccountDb.objects.filter(username=un, password=p).exists():
            request.session['username'] = un
            request.session['password'] = p
            messages.success(request, "Login successfully")
            return redirect(Home)
        else:
            messages.warning(request, "Wrong password or Username")
            return redirect(LoginSignin)
    return redirect(LoginSignin)


def logout(req):
    del req.session['username']
    del req.session['password']
    messages.success(req, "Logout successfully")
    return redirect(UserLogin)


def Hire(req):
    return render(req, "Hire.html")


def FrontCountry(req):
    if req.method == "POST":
        cn = req.POST.get('countryName')
        l = req.POST.get('location')
        cf = req.FILES['countryFlag']
        obj = FrontCountryDb(countryName=cn, location=l, countryFlag=cf)
        obj.save()
        messages.success(req, "Country Saved Successfully")
        return redirect(FrontCompany)


def FrontCompany(req):
    cry = FrontCountryDb.objects.all()
    return render(req, "FrontCompany.html", {'cry': cry})


def FrontCompanySave(req):
    if req.method == "POST":
        cn = req.POST.get('companyName')
        ci = req.POST.get('companyInfo')
        c = req.POST.get('country')
        cp = req.FILES['companyProfile']
        obj = FrontCompanyDb(companyName=cn, information=ci, country=c, companyProfile=cp)
        obj.save()
        messages.success(req, "Company Saved Successfully")
        return redirect(FrontAddJob)


def FrontAddJob(request):
    data = FrontCompanyDb.objects.all()
    return render(request, "FrontJob.html", {'data': data})


def FrontJobSave(req):
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
        obj = FrontJobDb(companyName=cn, job=j, jobDetails=jd, qualification=q, experience=e, date=d, time=t,
                         location=l,
                         contactNumber=ctn)
        obj.save()
        messages.success(req, "Job saved Successfully")
        return redirect(Home)


def ConatctUS(req):
    return render(req, "ConatctUS.html")


def ContactSave(req):
    if req.method == 'POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        m = req.POST.get('mobile')
        mg = req.POST.get('message')
        obj = Contactusdb(name=n, email=e, mobile=m, message=mg)
        obj.save()
        return redirect(ConatctUS)


def About(req):
    return render(req, "About.html")
