from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib import messages


from django.core.paginator import Paginator
from expert.models import Profile, Vacant_Seats, Give

@login_required
def give(request, *args, **kwargs):
    vacant_seats = Vacant_Seats.objects.get(id=kwargs['vacant_id'])
    give_point = Give.objects.filter(user=request.user).filter(seat=vacant_seats).count() #今使っているユーザが対象のささやきに与えているいいねの数
    # TODO 正常に席を譲られた場合にのみgive_pointをインクリメントする
    # if  is_like == 1:
    #     liking = Like.objects.get(sasayaki__id=kwargs['sasayaki_id'], joyu=request.user)
    #     liking.delete()
    #     sasayaki.good_count -= 1
    #     sasayaki.save()
    #     return redirect(request.META['HTTP_REFERER'])

    sasayaki.good_count += 1
    sasayaki.save()
    like = Like()
    like.joyu = request.user
    like.sasayaki = sasayaki
    like.save()
    messages.success(request, 'ぐー')
    #return HttpResponseRedirect(reverse_lazy('joyuchan:post_list'))
    return redirect(request.META['HTTP_REFERER'])