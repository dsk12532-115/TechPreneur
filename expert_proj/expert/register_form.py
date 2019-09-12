from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from expert.models import GENDER_LIST, Profile

class RegisterForm(UserCreationForm):
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER_LIST, required=True)
    email = forms.CharField(required=True)
    board_station = forms.CharField(required=False)
    exit_station = forms.CharField(required=False)
    time = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','age','email','gender','board_station','exit_station','time']
        labels = {
            'username': 'ユーザー名',
            'password1': 'パスワード',
            'password2': 'パスワード確認',
            'age': '年齢',
            'email':'Eメールアドレス',
            'gender': '性別',
            'board_station': 'よく乗る駅',
            'exit_station': 'よく降りる駅',
            'time':'よくある乗車時間',
        }

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError('Cannot create User and Profile without database save')
        
        user = super().save()

        try:
            max_id = Profile.objects.latest('id').id
        except ObjectDoesNotExist:
            max_id = 'U00000'

        prof_id = 'U'+(str(int(max_id[1:])+1).zfill(5))

        age = self.cleaned_data['age']
        email = self.cleaned_data['email']
        gender = self.cleaned_data['gender']
        board_station = self.cleaned_data['board_station']
        exit_station = self.cleaned_data['exit_station']
        time = self.cleaned_data['time']

        profile = Profile(id=prof_id,age=age,gender=gender,email=email,board_station=board_station,exit_station=exit_station,time=time,user_id=user.id)
        profile.save()

        return user