from django.shortcuts import render
from App.models import Employee
# Create your views here.

def home(request):
    employee_list = Employee.objects.all()
    context = {"employee" : employee_list}
    return render(request,"home.html", context)