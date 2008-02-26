from django.shortcuts import render_to_response
from wedding.models import Newspost, HotelInfo, RegistrationInfo, Info, Comments

def news(request):
    articles = Newspost.objects.all()
    return render_to_response('news.html', {'article_list': articles, 'news': True})

def hotels(request):
    hotels = HotelInfo.objects.all()
    return render_to_response('hotels.html', {'hotel_list': hotels, 'hotels': True})

def registration(request):
    registrations = RegistrationInfo.objects.all()
    return render_to_response('registration.html', {'registration_list': registrations, 'registration': True})

def info(request):
    info = Info.objects.all()
    return render_to_response('info.html', {'info_list': info, 'info': True})

def comments(request):
    comments = Comments.objects.all()
    return render_to_response('comments.html', {'comment_list': comments, 'comments': True})
