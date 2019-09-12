from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from expert.models import Profile, Vacant_Seats

@login_required
def congestion(request):
    vacant = Vacant_Seats.objects.all()
    if vacant.is_vacant:
        flag[int(vacant.id)] = '空'
    else:
        flag[int(vacant.id)] = 'x'
    seat_id = int(vacant.id)
    return render(request, 'expert/congestion.html', {'flag': flag[vacant.id], 'seat_id':seat_id})