#coding: utf8
from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf

from main_page.models import Ad
# Create your views here.

def new_ad(request):
	try:
		new_ad = Ad()
		new_ad.ad_header = request.POST['caption']
		new_ad.ad_content = request.POST['text']
		new_ad.ad_preview = request.POST['preview']
		new_ad.save()
		return redirect('/')
	except:
		return HttpResponse('Неудача! (здесь будет страница обработки ошибок)')
	

def show_current(request, ad_id):
	args = {}
	current_ad = Ad.objects.get(id = ad_id)
	args['current_ad'] = current_ad
	"""
	прверяем куку, если ид объявления в ней есть, значит это объявление уже просматривали
	Обычно такие вещи я прячу куда-нибудь в декоратор, но в данном случае не имеет смысла
	"""
	try:
		values = request.session['views']
		ad_id_list = values.split(';')
		if ad_id in ad_id_list:
			pass
		else:
			current_ad.ad_views += 1
			current_ad.save(update_fields=['ad_views',])
			request.session['views'] += '{};'.format(ad_id)
	except:
		#значит такой куки нет
		request.session['views'] = '{};'.format(ad_id)
		current_ad.ad_views += 1
		current_ad.save(update_fields=['ad_views',])
	finally:
		return render_to_response('ad.html', args)
		
	

def show_billboard(request):
	args = {}
	args.update(csrf(request))
	args['ad_list'] = Ad.objects.all()
	return render_to_response('main.html', args)
