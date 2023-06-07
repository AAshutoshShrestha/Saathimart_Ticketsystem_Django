from django.contrib import admin
from import_export.admin import ImportExportMixin

# Register your models here.
from .models import Tag,Employe,OrgDepartment,supervisor,Workers,CouponType,Case

class TagList(ImportExportMixin,admin.ModelAdmin):
    list_display =('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 15

admin.site.register(Tag,TagList)

class EmployeList(ImportExportMixin,admin.ModelAdmin):
    list_display =('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 15

admin.site.register(Employe,EmployeList)

class Department(ImportExportMixin,admin.ModelAdmin):
    list_display =('id','name','description',)
    list_filter = ('name',)
    search_fields = ('name','description','employId',)
    list_per_page = 15

admin.site.register(OrgDepartment,Department)

class supervisorList(ImportExportMixin,admin.ModelAdmin):
    list_display =('id','name','empID')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 15

admin.site.register(supervisor,supervisorList)

class employ_lists(admin.ModelAdmin):
    list_display = ('name','Profile','phone', 'email','joining_date','branch','Designation','title','department','TeamHead')
    list_filter = ('branch','department','TeamHead', )
    search_fields = ('name','branch','title','phone','department','TeamHead',)
    list_per_page = 15

admin.site.register(Workers,employ_lists)


class CouponType_list(ImportExportMixin,admin.ModelAdmin):
    list_display = ('name','validationTime')
    list_filter = ('name', )
    search_fields = ('name',)
    list_per_page = 15

admin.site.register(CouponType,CouponType_list)

class AllCoupon_list(admin.ModelAdmin):
    list_display = ('user','topic','description', 'Category','Priority','Status','note','date_created')
    list_filter = ('user','Category', 'date_created',)
    search_fields = ('user','topic')
    list_per_page = 15

admin.site.register(Case,AllCoupon_list)





