from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'), 
    path('update/<int:id>',views.Edit_Student,name='edit_student'),
    path('add/',views.Add_Student,name="add_student"),
    path("delete/<int:id>",views.deletedata,name="delete"),
    path("profile/",views.profile,name="profile"),
    path("register/",views.Register,name="register"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),
    path("passchange/",views.passwchange,name="passchange"),
    path("passwordchangeee/",views.passwordchange,name="passwordchangeee"),
]