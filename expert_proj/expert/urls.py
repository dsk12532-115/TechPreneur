from django.urls import path
from expert.views import vacant, mypage, vacant_overwrite, give

app_name = 'expert'

urlpatterns = [
    path('vacant', vacant.vacant, name='vacant'),
    path('mypage', mypage.mypage_top, name='mypage_top'),
    path('give_form', give.form_view, name='give_form' ),
    # path('vacant/overwrite', vacant_overwrite.vacant_overwrite, name='vacant_overwrite'),
    # path('vacant_info/<string:vacant_id>', vacant_info.),
    # path('expert/give_form', give_given_form.give, name='give_form')
    ]