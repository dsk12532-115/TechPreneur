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
    email = models.CharField('Email')
    age = models.IntegerField('年齢')
    gender = models.IntegerField('性別',choices=GENDER_LIST)

    def __str__(self):
        return self.id+' '+str(self.age)+'歳 ' \
            +self.email+' ' \
            +dict_gender_list.get(self.gender)+' ' \
            +str(self.household_num)+'人世帯 ' 