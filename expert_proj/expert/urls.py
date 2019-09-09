from django.urls import path
from expert.views import vacant

app_name = 'expert'

urlpatterns = [
    path('vacant', vacant.vacant, name='vacant'),
    ]