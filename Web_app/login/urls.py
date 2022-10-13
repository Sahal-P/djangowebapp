from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginpage, name='loginpage'),
    path('', views.signup, name='signup'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('User/', views.userpage, name='userpage'),
    path('logout', views.logout1, name='logout'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('user_list', views.user_list, name='user_list'),
    path('userform', views.userform, name='userform'),
    path('<int:id>', views.userform, name='updateuser'),
    path('delete/<int:id>', views.user_delete, name='user_delete'),
     path('search', views.search, name='search'),
]
