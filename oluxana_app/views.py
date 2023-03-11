from django.shortcuts import render, redirect
from django.core.serializers import serialize
import json
from django.urls import translate_url
from django.conf import settings
from django.http.response import JsonResponse
from django.utils import translation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from oluxana_app.models import About, PersonalAnnouncement, ContactUs, Morgue, Address, Brand, \
    HomeSlider, CarModel, AnnouncementImage

from oluxana_app.forms import CreateAnnouncementForm


def set_language(request, lang_code):
    lang = request.META.get("HTTP_REFERER", None)
    
    response = redirect(translate_url(lang, lang_code))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)

    return response

def index(request):
    addresses = Address.objects.all()
    brands = Brand.objects.all()
    data = request.GET.get("address")
    sliders = HomeSlider.objects.all()
    morgue = None
    if data and data is not None:
        try:
            address = Address.objects.get(id=data)
            morgue = Morgue.objects.filter(address=address)
        except:
            morgue = None
    context = {
        "page": "index",
        "addresses": addresses,
        "brands": brands,
        "morgue": morgue,
        "sliders": sliders,
    }
    return render(request, 'index-3.html', context=context)

def about(request):
    about = About.objects.last()
    context = {
        "page": "index",
        "about": about
    }
    return render(request, 'about.html', context=context)

def contact(request):
    contact = ContactUs.objects.last()
    context = {
        "page": "index",
        "contact": contact
    }
    return render(request, 'contacUs.html', context=context)

def oluxana(request):
    morgues = Morgue.objects.all()
    context = {
        "page": "index",
        "morgues": morgues
    }
    return render(request, 'ferdi.html', context=context)

def oluxana_detail(request, slug):
    morgues = Morgue.objects.filter(brand__slug=slug)
    context = {
        "page": "index",
        "morgues": morgues
    }
    return render(request, 'ferdi.html', context=context)

def personal_announcement(request):
    announcements = PersonalAnnouncement.objects.filter(verified=True)
    page = request.GET.get("page", 1)
    paginator = Paginator(announcements, 15)
    page_obj = paginator.get_page(page)
    try:
        announcements = paginator.page(page)
    except PageNotAnInteger:
        announcements = paginator.page(1)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)
    context = {
        "page": "index",
        "page_obj": page_obj,
        "announcements": announcements
    }
    return render(request, 'ferdi-details.html', context=context)

def personal_announcement_detail(request, slug):
    announcement = PersonalAnnouncement.objects.filter(slug=slug, verified=True)[0]
    related_products = PersonalAnnouncement.objects.filter(brand=announcement.brand, verified=True).exclude(id=announcement.id)[:3]
    context = {
        "announcement": announcement, 
        "related_products": related_products
    }
    return render(request, 'indbdle.html', context=context)

def create_announcement(request):
    form = CreateAnnouncementForm()
    if request.method == "POST":
        form = CreateAnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            for i in request.FILES.getlist("images-0-image"):
                image = AnnouncementImage.objects.create(
                    announcement=product,
                    image=i
                )
            form = CreateAnnouncementForm()
    context = {
        "page": "index",
        "form": form
    }
    return render(request, 'elan-yerlesdir.html', context=context)

def my_view(request):
    brand = request.GET.get('brand')
    marka = None
    try:
        brand = Brand.objects.get(id=brand)
        marka = CarModel.objects.filter(brand=brand)
        serialized_data = serialize("json", marka)
        serialized_data = json.loads(serialized_data)
        serialized_data 
        return JsonResponse(serialized_data, safe=False)
    except:
        marka = None
        return JsonResponse(list(marka), safe=False)
