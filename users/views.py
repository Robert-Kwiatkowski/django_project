from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserReqisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserReqisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserReqisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #sendmail(subject, message, from_email, to_list, fail_silently=True) testing
            subject = 'sss'
            message = 'xxxxx'
            from_email = settings.EMAIL_HOST_USER
            to_list = [u_form.email, p_form , settings.EMAIL_HOST_USER]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            #testing
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)




