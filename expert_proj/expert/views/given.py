from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from expert.given_form import GivenForm

def form_view(request):
    form = GivenForm()
    return render(request, 'expert/given_form.html', {'form':form})