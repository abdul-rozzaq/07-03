from django.urls import path

from .views import user_login, user_logout, register, create_assignment, submit_assignment, home_page, assignment_page

urlpatterns = [
    path("", home_page, name="home"),
    
    path("assignment/<int:pk>/", assignment_page, name="assignment"),
    
    path("create/", create_assignment, name="create-assignment"),
    path("submit/", submit_assignment, name="submit-assignment"),
    
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]

