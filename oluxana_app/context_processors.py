from django.http.response import JsonResponse
from django.http.request import HttpRequest
from oluxana_app.models import MainData, LeftBanner, Socials, RightBanner, MobileBanner


def banner(request: HttpRequest) -> JsonResponse:
    left_banner = LeftBanner.objects.all()
    right_banner = RightBanner.objects.all()
    mobile_banner = MobileBanner.objects.all()
    context = {
        "left_banner": left_banner,
        "right_banner": right_banner,
        "mobile_banner": mobile_banner,
    }

    return context

def main_data(request: HttpRequest) -> JsonResponse:
    maindata = MainData.objects.last()
    context = {
        "main_data": maindata
    }

    return context

def socials(request: HttpRequest) -> JsonResponse:
    social = Socials.objects.all()
    context = {
        "socials": social
    }

    return context
