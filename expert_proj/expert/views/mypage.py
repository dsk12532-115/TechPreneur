from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
# from expert.models import Vacant_Seats


@login_required
def mypage_top(request):
    user = request.user
    profile = user.profile
#     mylogs = Profile.objects.filter(profile_id=profile.id)
#     myrooms = RentRoom.objects.filter(owner_id=profile.id)

    return render(request, 'expert/mypage.html', {'profile':profile})