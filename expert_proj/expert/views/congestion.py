from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from expert.models import Vacant_Seats, WaitUser

@login_required
def congestion(request):
    wait_user = WaitUser.objects.all().order_by('-timestamp')
    paginator = Paginator(wait_user, 10)
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    return render(request, 'expert/congestion.html', {'wait_user':wait_user})