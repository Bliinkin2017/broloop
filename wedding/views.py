from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import ObjectPaginator, InvalidPage
from mysite.wedding.models import Newspost, HotelInfo, RegistrationInfo, Info, Comments, RSVP
from mysite.wedding.forms import CommentForm, RSVPForm

def news(request):
    articles = Newspost.objects.all()
    return render_to_response('news.html', {'article_list': articles, 'news': True})

def rsvp(request):
    template_parms = {'rsvp': True}
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        template_parms['form'] = form
        if form.is_valid():
            r = RSVP()
            r.name = form.clean_data['name']
            r.will_attend = form.clean_data['will_attend']
            r.num_guests = form.clean_data['num_guests']
            r.additional_guests = form.clean_data['additional_guests']
            r.save()
            if r.will_attend:
                return HttpResponseRedirect('/rsvped/')
            else:
                return HttpResponseRedirect('/thanks/')
    else:
        form = RSVPForm()
        template_parms['form'] = form
    return render_to_response('rsvp.html', template_parms)

def hotels(request):
    hotels = HotelInfo.objects.all()
    return render_to_response('hotels.html', {'hotel_list': hotels, 'hotels': True})

def registration(request):
    registrations = RegistrationInfo.objects.all()
    return render_to_response('registration.html', {'registration_list': registrations, 'registration': True})

def info(request):
    info = Info.objects.all()
    return render_to_response('info.html', {'info_list': info, 'info': True})

def comments(request, page):
    paginator = ObjectPaginator(Comments.objects.all(), 10)
    comments = paginator.get_page(page)
    template_parms = {'comment_list': comments, 'comments': True}
    if paginator.has_next_page(page):
        template_parms['next'] = True
    if paginator.has_previous_page(page):
        template_parms['prev'] = True

    return render_to_response('comments.html', template_parms)
