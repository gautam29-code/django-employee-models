from django.shortcuts import render
from app.models import *
def display_emp_details(request):
    QSLDO=Dept.objects.all()
    QSLEO=Emp.objects.all()
    
    content={
        "QSLDO":QSLDO,
        "QSLEO":QSLEO
    }
    return render(request,'display_emp_details.html',content)