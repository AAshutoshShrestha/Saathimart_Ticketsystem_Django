from django.contrib import admin
from import_export.admin import ImportExportMixin

# Register your models here.
from .models import employee

admin.site.index_title = 'Welcome to Admin Dashboard'

class EmployeList(ImportExportMixin,admin.ModelAdmin):
    list_display = ('Fullname','Emp_id','Designation', 'Role','Branch','Department','Phonenum','Email','Profile','Joined','Fb_id','Insta_id','Linkedin_id',)
    list_filter = ('Branch',)
    search_fields = ('Fullname','Designation','Emp_id','Branch',)
    list_per_page = 15
admin.site.register(employee,EmployeList)
