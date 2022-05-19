
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse






@login_required
def profile_detail(request, username):
    user = get_object_or_404(User, username=username)

    if request.user == user:
        return render(request, 'accounts/manage-profile.html')
    else:
        return HttpResponse("you are not allowed to view this profile")


@login_required
def profile_setting(request, username):
    user = get_object_or_404(User, username=username)

    if request.user == user:
        return render(request, 'accounts/setting.html')
    else:
        return HttpResponse("you are not allowed to view this profile")


