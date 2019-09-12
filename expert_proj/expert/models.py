from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

GENDER_LIST = ( (0, '男性'), (1, '女性') )
dict_gender_list = {0:'男性',1:'女性'}



class Profile(models.Model):
    class Meta:
        verbose_name = 'ユーザー情報データ'
        verbose_name_plural = 'ユーザー情報データ'
    user = models.OneToOneField(User, verbose_name='ユーザー',null=True, blank=True, on_delete=models.CASCADE)
    
    id = models.CharField(max_length=6,primary_key=True)
    email = models.CharField('Email',max_length=50)
    age = models.IntegerField('年齢')
    gender = models.IntegerField('性別',choices=GENDER_LIST)
    time = models.IntegerField('持ち時間')
    board_station = models.CharField('いつも乗る駅',max_length=70,default='')
    exit_station = models.CharField('いつも降りる駅',max_length=70,default='')
    given_point = models.IntegerField('ゆずられポイント',default=0)
    give_point = models.IntegerField('ゆずりポイント',default=10)

    def __str__(self):
        user_str = ''
        if self.user is not None:
            user_str = '(' + self.user.username + ')'

        return self.id+' '+str(self.age)+'歳 ' \
            +self.email+' ' \
            +dict_gender_list.get(self.gender)+' ' \
            +str(self.time)+'分 '\
            +'いつも乗る駅 '+self.board_station+'駅'\
            +'いつも降りる駅'+self.exit_station+'駅'\
            +'予定通り席に座れた回数 '+str(self.given_point)+'回 '\
            +'予定通り席を空けた回数 '+str(self.give_point)+'回'


class Station(models.Model):
    class Meta:
        verbose_name = '駅データ'
        verbose_name_plural = '駅データ'
    
    id = models.CharField('駅ID',max_length=4,primary_key=True) # 'JY06'
    name = models.CharField('駅名',max_length=50)       # '鎌倉'

    def __str__(self):
        return self.id+' '+self.name+'駅 '

LR_LIST = ( (0, '右'), (1, '左') )
dict_lr_list = {0:'右',1:'左',2:''}

class Vacant_Seats(models.Model):
    class Meta:
        verbose_name = '空席予報データ'
        verbose_name_plural = '空席予報データ'
    seat_id = models.CharField(max_length=2,default='')
    car_number = models.CharField('号車',max_length=2,default='')
    door_number = models.CharField('進行方向からのドア数',max_length=1,help_text='進行方向に最も近い座席の場合は0です',default='')
    seat_place = models.IntegerField('進行方向に対する場所',choices=LR_LIST,default=2)
    seat_number = models.CharField('進行方向からの席数',max_length=1,default='')
    # will_vacant = models.ForeignKey(Profile,
    #             verbose_name='ユーザー情報',
    #             on_delete=models.CASCADE) #例: 2(min)
    vacant_time = models.IntegerField('待ち時間', default=0)
    timestamp = models.DateTimeField('タイムスタンプ', default=timezone.now)
    board_station = models.CharField('乗車駅',max_length=70, default='')
    exit_station = models.CharField('降車駅',max_length=70, default='')
    is_vacant = models.BooleanField(default=True)
    
    def __str__(self):
        return '席id '+self.seat_id+' '+self.car_number+'号車 '+'降車駅は'+self.exit_station+'駅'\
        +' 日時 '+str(self.timestamp)

class WaitUser(models.Model):
    class Meta:
        verbose_name = '起立ユーザーデータ'
        verbose_name_plural = '起立ユーザーデータ'
    # profile = models.ForeignKey(Profile, verbose_name='ユーザー情報', on_delete=models.CASCADE)
    car_number = models.CharField('号車',max_length=2,default='')
    board_station = models.CharField('乗車駅',max_length=70, default='')
    exit_station = models.CharField('降車駅',max_length=70, default='')
    timestamp = models.DateTimeField('タイムスタンプ', default=timezone.now)

    def __str__(self):
        return self.car_number+'号車 '+'乗車駅は'+self.board_station+'駅 '+'降車駅は'+self.exit_station+'駅'\
        +' 日時 '+str(self.timestamp)



# class Give(models.Model):
#     class Meta:
#         verbose_name = 'ゆずりデータ'
#         verbose_name_plural = 'ゆずりデータ'
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='give_user')
#     seat = models.ForeignKey(Vacant_Seats, on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add=True)