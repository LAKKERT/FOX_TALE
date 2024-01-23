from django.shortcuts import render, redirect, Http404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.http import Http404
from django.contrib import messages
from django.views import View

from .forms import UserRegistrationForm, UserEmailChangeForm, ChangePasswordForm
from .models import UserProfileModel

from django.contrib.auth import logout

# Create your views here.

def logout_without_confirm(request):
    logout(request)
    return redirect('home')

class RegistrationUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            raise Http404()
        form = UserRegistrationForm()
        user = User.objects.all()
        return render(request, 'registration.html', {'form':form, 'objects':user})
    
    def post(self, request):
        if request.user.is_authenticated:
            raise Http404()
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.save()
            
            user_profile = UserProfileModel(user=user, month=form.cleaned_data['month'], day=form.cleaned_data['day'], year=form.cleaned_data['year'])
            user_profile.save()

            return redirect('login')
        else:
            form = UserRegistrationForm()
        return render(request, 'registration.html', {'form':form})

def ProfileView(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            user_profile = UserProfileModel.objects.get(user=user)
        except:
            user_profile = None
    else:
        return redirect('home')
    user = request.user
    password_error = ""
    email_error = ""

    form_change_password = ChangePasswordForm(request.POST)
    form_change_email = UserEmailChangeForm(request.POST)
    if request.method == 'POST':
        if form_change_password.is_valid():
            old_password = form_change_password.cleaned_data['old_password']
            new_password1 = form_change_password.cleaned_data['new_password1']
            new_password2 = form_change_password.cleaned_data['new_password2']
            
            if not request.user.check_password(old_password):
                password_error = 'The old password is incorrect'
                return render(request, 'profile/profile.html', {'user_profile': user_profile, 'password_error':password_error, 'form_change_email': form_change_email, 'email_error': email_error, 'form_change_password': form_change_password})            
            if new_password1 != new_password2:
                password_error = 'The new passwords do not match'
                return render(request, 'profile/profile.html', {'user_profile': user_profile, 'password_error':password_error, 'form_change_email': form_change_email, 'email_error': email_error, 'form_change_password': form_change_password})            
            request.user.set_password(new_password1)
            request.user.save()
            update_session_auth_hash(request, user)
            
            return redirect('profile')
        else:
            form_change_password = ChangePasswordForm()

        if form_change_email.is_valid():
            user = request.user
            email = request.POST.get('new_email')
            if User.objects.filter(email=email).exists():
                print('exist')
                email_error = "Email already exist"
                return render(request, 'profile/profile.html', {'user_profile': user_profile, 'password_error':password_error, 'form_change_email': form_change_email, 'email_error': email_error, 'form_change_password': form_change_password})
            user.email = email
            user.save()
            print('email changed')
        else:
            form_change_email = UserEmailChangeForm()
    
    return render(request, 'profile/profile.html', {'user_profile': user_profile, 'password_error':password_error, 'form_change_email': form_change_email, 'email_error': email_error, 'form_change_password': form_change_password})