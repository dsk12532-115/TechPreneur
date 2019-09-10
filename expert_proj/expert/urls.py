from django.urls import path
from expert.views import vacant, mypage

app_name = 'expert'

urlpatterns = [
    path('vacant', vacant.vacant, name='vacant'),
    # path('mypage', mypage.mypage_top, name='mypage_top'),
    ]