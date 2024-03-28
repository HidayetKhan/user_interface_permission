from django.urls import path
from .views import  home_page,submit_form ,custom_login, update_user,logout_user,sidebar

urlpatterns = [
    path('', home_page, name='home_page'),#home.html for homepage
    path('submit/', submit_form, name='submit_form'),#basic.html for  adduser
    # path('login/', login, name='login'),
    path('login/', custom_login, name='custom_login'), #login.html for login
    path('update',  update_user, name='update1'),# upadte.html
    path('logout/', logout_user, name='logout'),#logout
    path('sidebar/',sidebar, name='sidebar'),
    
]
