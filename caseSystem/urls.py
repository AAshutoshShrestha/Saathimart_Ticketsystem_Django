from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',include('emp_details.urls')),    
    path('',include('ticket.urls')),    

    re_path(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
    re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),

]
handler404 = "emp_details.views.page_not_found_view"
