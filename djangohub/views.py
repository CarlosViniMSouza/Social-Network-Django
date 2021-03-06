from django.shortcuts import render
from .models import Profile


def dashboard(request):
    return render(request, "base.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "djangohub/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "djangohub/profile.html", {"profile": profile})
