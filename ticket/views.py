from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import signals
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Tag,Employe,OrgDepartment,supervisor,Workers,CouponType,Case
from .forms import CreateUserForm, WorkersForm, CaseForm,EmployeForm
from .decorators import unauthenticated_user, allowed_users, admin_only


def components(request):
	context = {
    }
	return render(request, 'views/components.html',context)

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'User was created for ' + username)
			return redirect('login')
		

	context = {'form':form}
	return render(request, 'views/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'views/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	notification = signals.notification.send(sender=request.user,updatedby=request.user)

	prof = Workers.objects.get(user=request.user)
	Cases = Case.objects.filter(user=prof.user.id)

	total_Cases = Cases.count()
	delivered = Cases.filter(Status='Delivered').count()
	pending = Cases.filter(Status='Pending').count()
	on_process = Cases.filter(Status='On Process').count()
	ON_Hold = Cases.filter(Status='ON Hold').count()
	Completed = Cases.filter(Status='Completed').count()
	context = {
		'notify':notification,
		'profile':prof,
		'usercases':Cases,
		'total_count':total_Cases,
		'delivered':delivered,
		'on_process':on_process,
		'ON_Hold':ON_Hold,
		'pending':pending, 
		'Completed':Completed
		}

	return render(request, 'views/home.html', context)


@login_required(login_url='login')
def profile(request, pk_test):
	profile = Workers.objects.get(id=pk_test)
	context = {
        'profile':profile, 
    }
	return render(request, 'views/profile.html',context)

@login_required(login_url='login')
def caseslist(request, pk):
	prof = Workers.objects.get(id=pk)
	Cases = Case.objects.filter(Department=prof.department)
	context = {
        'cases':Cases, 
        'profile':prof 
    }
	return render(request, 'views/case.html',context)


@login_required(login_url='login')
def createcase(request):
	form = CaseForm()
	if request.method == 'POST':
		form = CaseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'views/case_form.html', context)


@login_required(login_url='login')
def updateCase(request, pk):
	Cases = Case.objects.get(id=pk)
	form = CaseForm(instance=Cases)
	if request.method == 'POST':
		form = CaseForm(request.POST, instance=Cases)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {
        'Cases':Cases,
        'form':form
        }
	return render(request, 'views/Case_form.html', context)



@login_required(login_url='login')
def deletecase(request, pk):
	Cases = Case.objects.get(id=pk)
	if request.method == "POST":
		Cases.delete()
		return redirect('home')

	context = {'item':Cases}
	return render(request, 'views/delete.html', context)


@login_required(login_url='login')
def User_Update_form(request):
	WorkForm = WorkersForm()
	EmpForm = EmployeForm()
	if request.method == 'POST':
		WorkForm = WorkersForm(request.POST)
		EmpForm = EmployeForm(request.POST)
		if WorkForm.is_valid() and EmpForm.is_valid():
			WorkForm.save()
			EmpForm.save()
			return redirect('home')
	context = {
		'Worker':WorkForm,
		'Emp':EmpForm
		}
	return render(request, 'views/userDetailsUpdateForm.html', context)
