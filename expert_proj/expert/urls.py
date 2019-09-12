from django.urls import path
from expert.views import vacant, mypage, vacant_overwrite, give, congestion, given, vacant_given

app_name = 'expert'

urlpatterns = [
    path('vacant', vacant.vacant, name='vacant'),
    path('vacant_given', vacant_given.vacant, name='vacant_given'),
    path('mypage', mypage.mypage_top, name='mypage_top'),
    path('give_form', give.form_view, name='give_form' ),
    path('given_form', given.form_view, name='given_form' ),
    path('congestion', congestion.congestion, name='congestion' ),
    # path('info', info.info, name='info'),
    # path('vacant/overwrite', vacant_overwrite.vacant_overwrite, name='vacant_overwrite'),
    # path('vacant_info/<string:vacant_id>', vacant_info.),
    # path('expert/give_form', give_given_form.give, name='give_form')
    ]