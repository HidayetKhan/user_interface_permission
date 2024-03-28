from django.shortcuts import render,redirect
from . models import USerMaster
from django.http import HttpResponseBadRequest,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
# Create your views here.

#home page
def home_page(request):
    return render(request, 'home.html')

#updateform page
def update(request):
    return render(request,'update.html')

#to create a user
def submit_form(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        city = request.POST.get('city')
        my_field = request.POST.get('my_field')

        # Create an instance of your model and save it to the database
        USerMaster.objects.create(
            name=name,
            email=email,
            phone=phone,
            date_of_birth=date_of_birth,
            city=city,
            my_field=my_field
        )

        
        # return redirect('success_url')  # Redirect to success page after successful form submission

    return render(request, 'basic.html')




#for login to diffrent user
# def custom_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if user.groups.filter(name='superuser').exists():
#                 return redirect('submit_form')
#             elif user.groups.filter(name='user').exists():
#                 return redirect('home_page')
#             elif user.groups.filter(name='admin').exists():
#                 return redirect('viewer_dashboard')
#             else:
#                 # Handle case when user doesn't belong to any group
#                 return redirect('dashboard')  # Redirect to a generic dashboard page
#         else:
#             # Handle invalid login credentials
#             return render(request, 'login.html', {'error_message': 'Invalid username or password'})
#     else:
#         return render(request, 'login.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='superuser').exists():
                return redirect('submit_form')
            elif user.groups.filter(name='user').exists():
                return redirect('home_page')
            elif user.groups.filter(name='admin').exists():
                return redirect('submit_form')
            else:
                # Handle case when user doesn't belong to any group
                return redirect('home_page')  # Redirect to a generic dashboard page
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Clear session data when user visits login page
        request.session.flush()
        return render(request, 'login.html')


#for updating user
def update_user(request):
    if request.method == 'POST':
        # Retrieve data from the form
        update_name = request.POST.get('update_name')
        update_email = request.POST.get('update_email')
        update_phone = request.POST.get('update_phone')
        update_city = request.POST.get('update_city')
        user_id = request.POST.get('user_id')  # Assuming there's an input field named 'user_id' in your form

        # Get the user instance based on the provided user_id
        user_instance = USerMaster.objects.get(id=user_id)  

        # Update user fields with new values
        user_instance.name = update_name
        user_instance.email = update_email
        user_instance.phone = update_phone
        user_instance.city = update_city
        user_instance.save()

        return redirect('home_page')  # Redirect to the home page after successful update

    # If the request method is not POST, render the form page
    return render(request, 'update.html')



#for logout
def logout_user(request):
    logout(request)
    return redirect('home_page')



#for handling diffrent interface
def sidebar(request):
    user_group = None
    if request.user.is_authenticated:
        if request.user.groups.filter(name='superuser').exists():
            user_group = 'superuser'
        elif request.user.groups.filter(name='admin').exists():
            user_group = 'admin'
    return render(request, 'basic.html', {'user_group': user_group})

