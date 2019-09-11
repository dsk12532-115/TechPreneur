from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from expert.give_form import GiveForm

def form_view(request):
    form = GiveForm()
    return render(request, 'expert/my_time_form.html', {'form':form})