from django.db import models

# Create your models here.
from django.contrib.auth.models import User 
from django.db import models 

GENDER_LIST = ( (0, '男性'), (1, '女性') )
dict_gender_list = {0:'男性',1:'女性'}

STATION_LIST = ((0, '逗子'),(1, '鎌倉'),(2, '北鎌倉'),
                (3, '大船'),(4, '戸塚'),(5, '東戸塚'),
                (6, '保土ヶ谷'),(7, '横浜'),(8, '新川崎'),
                (9, '武蔵小杉'),(10, '西大井'),(11, '大崎'),
                (12, '恵比寿'),(13, '渋谷'),(14, '新宿'),
                (15, '池袋'),(16, '赤羽'),(17, '浦和'),
                (18, '大宮'),(19, '宮原'),(20, '上尾'),
                (21, '北上尾'),(22, '桶川'),(23, '北本'),
                (24, '鴻巣'),(25, '北鴻巣'),(26, '吹上'),
                (27, '行田'),(28, '熊谷'),(29, '籠原'),
                (30, '深谷'),(31, '岡部'),(32, '本庄'),
                (33, '神保原'),(34, '新町'),(35, '倉賀野'),
                (36, '高崎'),(37, '高崎問屋町'),(38, '井野'),
                (39, '新前橋'),(40, '前橋'),(41, '土呂'),
                (42, '東大宮'),(43, '蓮田'),(44, '白岡'),
                (45, '新白岡'),(46, '久喜'),(47, '東鷲宮'),
                (48, '栗橋'),(49, '古河'),(50, '野木'),
                (51, '間々田'),(52, '小山'),(53, '小金井'),
                (54, '自治医大'),(55, '石橋'),(56, '雀宮'),
                (57, '宇都宮'))
dict_station_list = {
                0: '逗子',1: '鎌倉',2: '北鎌倉',
                3:'大船',4: '戸塚',5: '東戸塚',
                6: '保土ヶ谷',7: '横浜',8:'新川崎',
                9: '武蔵小杉',10: '西大井',11: '大崎',
                12: '恵比寿',13: '渋谷',14: '新宿',
                15: '池袋',16: '赤羽',17: '浦和',
                18: '大宮',19: '宮原',20: '上尾',
                21: '北上尾',22: '桶川',23: '北本',
                24: '鴻巣',25: '北鴻巣',26: '吹上',
                27: '行田',28: '熊谷',29: '籠原',
                30: '深谷',31: '岡部',32: '本庄',
                33: '神保原',34: '新町',35: '倉賀野',
                36: '高崎',37: '高崎問屋町',38: '井野',
                39: '新前橋',40: '前橋',41: '土呂',
                42: '東大宮',43: '蓮田',44: '白岡',
                45: '新白岡',46: '久喜',47: '東鷲宮',
                48: '栗橋',49: '古河',50: '野木',
                51: '間々田',52: '小山',53: '小金井',
                54: '自治医大',55: '石橋',56: '雀宮',
                57: '宇都宮'
                }

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
    # boarding_station = models.IntegerField('乗車駅',choices=STATION_LIST,default=0)
    # exit_station = models.IntegerField('降車駅',choices=STATION_LIST,default=0)

    def __str__(self):
        user_str = ''
        if self.user is not None:
            user_str = '(' + self.user.username + ')'

        return self.id+' '+str(self.age)+'歳 ' \
            +self.email+' ' \
            +dict_gender_list.get(self.gender)+' ' \
            +str(self.time)+'分 '\
            # +dict_station_list.get(self.boarding_station)+' '\
            # +dict_station_list.get(self.exit_station)

class Station(models.Model):
    class Meta:
        verbose_name = '駅データ'
        verbose_name_plural = '駅データ'
    
    id = models.CharField('駅ID',max_length=4,primary_key=True) # 'S00001'
    name = models.CharField('駅名',max_length=50)       # '喜多見'

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