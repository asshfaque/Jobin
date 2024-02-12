from django.urls import path
from JobFrontend import views

urlpatterns = [
    path('Home', views.Home, name="Home"),
    path('Jobs', views.Jobs, name="Jobs"),
    path('Company', views.Company, name="Company"),
    path('jobFilter/<cmp_name>/', views.jobFilter, name="jobFilter"),
    path('Country', views.Country, name="Country"),
    path('CompanyFilter/<cmpny_name>/', views.CompanyFilter, name="CompanyFilter"),
    path('SingleJob/<int:singleId>/', views.SingleJob, name="SingleJob"),
    path('', views.LoginSignin, name="LoginSignin"),
    path('CreateAccount', views.CreateAccount, name="CreateAccount"),
    path('UserLogin', views.UserLogin, name="UserLogin"),
    path('logout', views.logout, name="logout"),
    path('Hire', views.Hire, name="Hire"),
    path('FrontCountry', views.FrontCountry, name="FrontCountry"),
    path('FrontCompany', views.FrontCompany, name="FrontCompany"),
    path('FrontCompanySave', views.FrontCompanySave, name="FrontCompanySave"),
    path('FrontAddJob', views.FrontAddJob, name="FrontAddJob"),
    path('FrontJobSave', views.FrontJobSave, name="FrontJobSave"),
    path('ConatctUS', views.ConatctUS, name="ConatctUS"),
    path('ContactSave', views.ContactSave, name="ContactSave"),
    path('About', views.About, name="About"),
]
