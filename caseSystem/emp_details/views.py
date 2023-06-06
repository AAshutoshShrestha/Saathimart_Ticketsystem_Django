from django.db.models import query
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import employee
from .forms import empForm
from datetime import datetime

def page_not_found_view(request, exception):
    return render(request, 'admin/404.html', status=404)

def index(request):
    return render(request, 'empdetails/home.html')

def add_emp(request):
    sumbitted = False
    if request.method == "POST":
        form = empForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_emp?sumbitted=True')
    else:
        form = empForm
        if 'sumbitted' in request.GET:
            sumbitted = True
    return render(request, 'empdetails/form.html', { 'form' : form , 'sumbitted': sumbitted})


def search(request):
    query_list = employee.objects.order_by('Emp_id')
    if 'search' in request.GET:
        now = datetime.now()
        search = request.GET['search']
        if search:
            # join = query_list.filter(join_date, Emp_id__iexact=search),
            query_list = query_list.filter(Emp_id__iexact=search)
    context = {
        'now' : now ,
        'search' : search,
        'listings' : query_list,
    }

    return render(request, 'empdetails/profile.html',context)

