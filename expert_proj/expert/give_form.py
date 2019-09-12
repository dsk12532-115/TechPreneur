from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from django import forms

from expert.models import Vacant_Seats, Profile, LR_LIST


class GiveForm(forms.ModelForm):
    id = forms.CharField(required=True)
    car_number = forms.CharField(required=True)
    door_number = forms.CharField(required=True)
    seat_place = forms.ChoiceField(choices=LR_LIST, required=True)
    seat_number = forms.CharField(required=True)
    vacant_time = forms.IntegerField(required=True)
    class Meta:
        model = Vacant_Seats
        fields = ['id','car_number','door_number','seat_place','seat_number','vacant_time']
        labels = {
            'id':'座席のid(画像参照)',
            'car_number':'号車',
            'door_number':'ドア数',
            'seat_place':'進行方向に対して右か左か',
            'seat_number':'進行方向からの席数',
            'vacant_time': '降りるまでの時間',
        }
    
    def save(self, commit=True):
        id = self.cleaned_data['id']
        car_number = self.cleaned_data['car_number']
        door_number = self.cleaned_data['door_number']
        seat_place = self.cleaned_data['seat_place']
        seat_number = self.cleaned_data['seat_number']
        vacant_time = self.cleaned_data['vacant_time']
        vacant_seats = Vacant_Seats(id=id,car_number=car_number,door_number=door_number,seat_place=seat_place,seat_number=seat_number,vacant_time=vacant_time)
        vacant_seats.save()