from django.urls import path

from .views import login_user, sign_up_user, logout_user

urlpatterns = [
    path('sign_up/', sign_up_user, name='signup'),
    path('login_user/', login_user, name='login'),
    path('logout_user/', logout_user, name='logout'),

]

