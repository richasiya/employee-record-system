from django.http import HttpResponse
import datetime
from django.shortcuts import render


def home(request):

    if request.method =='POST':
        check = request.POST['check']
        print(check)

    date = datetime.datetime.now()
    isActive = True
    name = "Richa Yadhuvanshi"
    #list_of_programs=[
       # 'WAP to check even or odd',
       # 'WAP to print pascals triangle',
        #'WAP to print all prime nu.',
    #]
    student ={
        'student_name':"Siya Yadhuvanshi",
        'student_college':"MIT",
        'student_city':"Meerut",

    }

    #print("test fun is called from view")
    #return HttpResponse("<h1>Hello this is index page</h1>"+str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        #'list_of_programs':list_of_programs,
        'student':student,
    }
    return render(request,"home.html",data)

def about(request):
    date = datetime.datetime.now()
    #return HttpResponse("<h1>This is my about page</h1>")
    return render(request,"aboutpage.html",{})

def services(request):
    date = datetime.datetime.now()
    
    #return HttpResponse("<h1>This is my services page</h1>")
    return render(request,"services.html",{})

