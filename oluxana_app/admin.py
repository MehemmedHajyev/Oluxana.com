from django.contrib import admin
from django.contrib.auth import get_user_model
from oluxana_app.models import ContactUs, PhoneNumber, Email, About, MainData, Morgue, Brand, Address, \
    PersonalAnnouncement, AnnouncementImage, CarModel, ProductKind, Socials, HomeSlider, LeftBanner, RightBanner, \
    MobileBanner


User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username", 
        "email", 
        "is_staff", 
        "is_active", 
    )

    readonly_fields = (
        "password",
        "date_joined",
        "last_login",
    )

    fieldsets_map = {
        None: {"__all__": {"fields": (
            "username", 
            "password",
            )}},
        "Personal Info": {"__all__": {"fields": (
            "first_name", 
            "last_name", 
            "email",

            "address",
            "country",
            "city",

            "phone",


            )}},
        "Permissions": {"__all__": {"fields": (
                "is_staff",
                "is_active",
                "is_superuser",
                "groups",
                "user_permissions",
            )}},
        "Important Dates": {"__all__": {"fields": (
                "date_joined",
                "last_login",
            )}}
    }
    

    def get_fieldsets(self, request, obj=None):
        fieldsets = []
        for title, fields in self.fieldsets_map.items():
            options = fields["__all__"]
            fieldsets.append((title, options))
        return fieldsets


admin.site.register(About)
admin.site.register(MainData)
admin.site.register(CarModel)
admin.site.register(ProductKind)
admin.site.register(Socials)
admin.site.register(HomeSlider)
admin.site.register(LeftBanner)
admin.site.register(RightBanner)
admin.site.register(MobileBanner)

class PhoneNumberAdmin(admin.StackedInline):
    model = PhoneNumber

class EmailAdmin(admin.StackedInline):
    model = Email

class AnnouncementImageAdmin(admin.StackedInline):
    model = AnnouncementImage

@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberAdmin, EmailAdmin]

@admin.register(PersonalAnnouncement)
class PersonalAnnouncementAdmin(admin.ModelAdmin):
    inlines = [AnnouncementImageAdmin,]

admin.site.register(Brand)
admin.site.register(Address)
admin.site.register(Morgue)
