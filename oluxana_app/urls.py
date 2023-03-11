from django.urls import path
from oluxana_app.views import index, about, contact, oluxana, personal_announcement, \
    personal_announcement_detail, create_announcement, oluxana_detail, my_view


urlpatterns = [
    path("", index, name="index"),
    path("brand/", my_view, name="my_view"),
    path("haqqimizda", about, name="about"),
    path("elaqe", contact, name="contact"),
    path("oluxanalar", oluxana, name="oluxana"),
    path("oluxanalar/<str:slug>", oluxana_detail, name="oluxana_detail"),
    path("ferdi-elanlar", personal_announcement, name="personal_announcement"),
    path("ferdi-elanlar/<str:slug>", personal_announcement_detail, name="personal_announcement_detail"),
    path("elan-yerlesdir", create_announcement, name="create_announcement"),
]
