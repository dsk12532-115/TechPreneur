from django.db import models

# Create your models here.
from django.contrib.auth.models import User 
from django.db import models 

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

    def __str__(self):
        user_str = ''
        if self.user is not None:
            user_str = '(' + self.user.username + ')'

        return self.id+' '+str(self.age)+'歳 ' \
            +self.email+' ' \
            +dict_gender_list.get(self.gender)+' ' \
            +str(self.time)+'分 '


class Station(models.Model):
    class Meta:
        verbose_name = '駅データ'
        verbose_name_plural = '駅データ'
    
    id = models.CharField('駅ID',max_length=4,primary_key=True) # 'JY06'
    name = models.CharField('駅名',max_length=50)       # '鎌倉'

    def __str__(self):
        return self.id+' '+self.name+'駅 '


class Vacant_Seats(models.Model):
    class Meta:
        verbose_name = '空席予報データ'
        verbose_name_plural = '空席予報データ'
    id = models.CharField(max_length=6,primary_key=True)
    will_vacant = models.ForeignKey(Profile,
                verbose_name='ユーザー情報',
                on_delete=models.CASCADE) #例: 2(min)
    
    def __str__(self):
        return self.id+' '+str(self.will_vacant.time)