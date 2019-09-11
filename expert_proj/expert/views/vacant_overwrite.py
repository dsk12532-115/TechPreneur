from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.core.paginator import Paginator
from expert.models import Profile, Vacant_Seats

@login_required
def vacant_overwrite(request):
    vacant_seat = Vacant_Seats.objects.all()
    wait_time = Profile.objects.get(user=request.user)
    user_time = wait_time.time
    vacant_seat.vacant_time = user_time
    vacant_seat.update()
    vacant_list = Vacant_Seats.objects.all().order_by('will_vacant')
    paginator = Paginator(vacant_list, 5)
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    vacant_seats = paginator.get_page(page)
    return render(request, 'expert/vacant_list.html', {'vacant_seats': vacant_seats, 'page': page, 'last_page': paginator.num_pages})