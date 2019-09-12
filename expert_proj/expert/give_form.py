from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from django import forms

from expert.models import Vacant_Seats, Profile, LR_LIST


class GiveForm(forms.ModelForm):
    seat_id = forms.CharField(required=True)
    car_number = forms.CharField(required=True)
    # door_number = forms.CharField(required=True)
    # seat_place = forms.ChoiceField(choices=LR_LIST, required=True)
    # seat_number = forms.CharField(required=True)
    # vacant_time = forms.IntegerField(required=True)
    # board_station = forms.CharField(required=True)
    exit_station = forms.CharField(required=True)
    class Meta:
        model = Vacant_Seats
        fields = ['seat_id','car_number','exit_station']
        labels = {
            'seat_id':'座席のid(画像参照)',
            'car_number':'号車',
            # 'door_number':'ドア数',
            # 'seat_place':'進行方向に対して右か左か',
            # 'seat_number':'進行方向からの席数',
            # 'vacant_time': '降りるまでの時間',
            # 'board_station': '乗車駅',
            'exit_station':'降車駅',
        }
    
    def save(self, commit=True):
        seat_id = self.cleaned_data['seat_id']
        car_number = self.cleaned_data['car_number']
        # door_number = self.cleaned_data['door_number']
        # seat_place = self.cleaned_data['seat_place']
        # seat_number = self.cleaned_data['seat_number']
        # vacant_time = self.cleaned_data['vacant_time']
        # board_station = self.cleaned_data['board_station']
        exit_station = self.cleaned_data['exit_station']
        vacant_seats = Vacant_Seats(seat_id=seat_id,car_number=car_number,exit_station=exit_station)
        vacant_seats.save()

#,'door_number','seat_place','seat_number','vacant_time','board_station',

#door_number=door_number,seat_place=seat_place,seat_number=seat_number,vacant_time=vacant_time,board_station=board_station,