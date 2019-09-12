from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from django import forms

from expert.models import WaitUser

class GivenForm(forms.ModelForm):
    car_number = forms.CharField(required=True)
    board_station = forms.CharField(required=True)
    exit_station = forms.CharField(required=True)
    class Meta:
        model = WaitUser
        fields = ['car_number','board_station','exit_station']
        labels = {
            'car_number':'号車',
            'board_station':'乗車駅',
            'exit_station':'降車駅',
        }
    def save(self, commit=True):
        car_number = self.cleaned_data['car_number']
        board_station = self.cleaned_data['board_station']
        exit_station = self.cleaned_data['exit_station']
        wait_user = WaitUser(car_number=car_number,board_station=board_station,exit_station=exit_station)
        wait_user.save()