from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from employee.models import Employee,Attendance,Notice,workAssignments, SalaryDetail
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404

@login_required(login_url='/')
def dashboard(request):
    try:
        # Assuming there is a related_name in the OneToOneField (e.g., employee)
        employee_instance = get_object_or_404(Employee, user=request.user)
        return render(request, "employee/index.html", {'info': employee_instance})
    except Employee.DoesNotExist:
        return HttpResponseServerError("Employee data not found for the current user.")

    
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee, Attendance

@login_required(login_url='/')
def attendance(request):
    # Assuming eId is the Employee instance
    employee_instance = get_object_or_404(Employee, user=request.user)
    # Retrieve all attendance records for the employee
    attendance = Attendance.objects.filter(eId=employee_instance)
    return render(request, "employee/attendance.html", {"info": attendance})


# views.py
from django.shortcuts import render
from .models import SalaryDetail

def salary(request):
    # Assuming eId is the Employee instance
    employee_instance = get_object_or_404(Employee, user=request.user)
    # Retrieve all attendance records for the employee
    salary = SalaryDetail.objects.filter(user=employee_instance)
    context = {
        'info': salary,
    }

    return render(request, 'employee/salary_details.html', context)



@login_required(login_url='/')
def notice(request):
    notices  = Notice.objects.all()
    return render(request,"employee/notice.html",{"notices":notices})

@login_required(login_url='/')
def noticedetail(request,id):
    noticedetail = Notice.objects.get(Id=id)
    return render(request,"employee/noticedetail.html",{"noticedetail":noticedetail})

