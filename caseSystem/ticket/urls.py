from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('dashboard', views.home, name="home"),
    path('components', views.components, name="components"),

    path('profile/<str:pk_test>/', views.profile, name="profile"),
    path('userupdate/', views.User_Update_form, name="UserUpdate"),

    # path('account/', views.accountSettings, name="account"),

    path('cases/<str:pk>/', views.caseslist, name='cases'),

    path('createcase', views.createcase, name="createCase"),
    path('updatecase/<str:pk>/', views.updateCase, name="updateCase"),
    path('deletecase/<str:pk>/', views.deletecase, name="deleteCase"),


]