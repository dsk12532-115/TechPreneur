from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages


from django.core.paginator import Paginator
from expert.models import Profile, Vacant_Seats

count = 0

def vacant(request):
    vacant_list = Vacant_Seats.objects.all().order_by('will_vacant__time')
    paginator = Paginator(vacant_list, 5)
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    vacant_seats = paginator.get_page(page)
    return render(request, 'expert/vacant_list.html', {'vacant_seats': vacant_seats, 'page': page, 'last_page': paginator.num_pages})