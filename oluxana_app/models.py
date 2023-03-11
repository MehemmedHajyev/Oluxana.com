from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify

from oluxana_app.utils import unique_slug_generator


SOCIAL_CHOICES = (
    ("facebook", "Facebook"),
    ("twitter", "Twitter"),
    ("instagram", "Instagram"),
    ("youtube", "Youtube"),
    ("tiktok", "Tiktok"),
)

class User(AbstractUser):
    username = models.CharField(
        ("username"),
        null=True, blank=True,
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )
    profile_image = models.ImageField(upload_to="user", default="users/default-pp/avatar-1.jpg", null=True, blank=True)
    first_name = models.CharField(
        ("first name"), 
        max_length=255, 
        blank=True
    )
    last_name = models.CharField(
        ("last name"), 
        max_length=255, 
        blank=True
    )
    address = models.TextField(
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    email = models.EmailField(
        ("email address"), 
        max_length=255, 
        unique=True,
    )
    phone = models.CharField(
        max_length=50,
        null=True,
        blank=True
    ) 
    is_staff = models.BooleanField(
        ("staff status"),
        default=False,
        help_text=("Designates whether the user can log into this admin " "site."),
    )

    # def save(self, *args, **kwargs) -> None:
    #     self.username = self.first_name + self.last_name + 'kerim'
    #     super(User, self).save(*args, **kwargs)

    @property
    def full_name(self) -> str:
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self) -> str:
        return self.full_name



class About(models.Model):
    image = models.ImageField(upload_to="haqqimizda/")
    text = RichTextField()

    def __str__(self):
        return "Haqqımızda"
    
    class Meta:
        verbose_name = _("Haqqımızda")
        verbose_name_plural = _("Haqqımızda")

class HomeSlider(models.Model):
    image = models.ImageField(upload_to="home/slider/")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    button_text = models.CharField(max_length=400)
    button_link = models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _("Slayder")
        verbose_name_plural = _("Slayder")

class LeftBanner(models.Model):
    image = models.ImageField(upload_to="banner/")
    link = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.link}"
    
    class Meta:
        verbose_name = _("Sol banner")
        verbose_name_plural = _("Sol banner")

class RightBanner(models.Model):
    image = models.ImageField(upload_to="banner/")
    link = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.link}"
    
    class Meta:
        verbose_name = _("Sağ banner")
        verbose_name_plural = _("Sağ banner")

class MobileBanner(models.Model):
    image = models.ImageField(upload_to="banner/")
    link = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.link}"
    
    class Meta:
        verbose_name = _("Mobil banner")
        verbose_name_plural = _("Mobil banner")

class Brand(models.Model):
    slug = models.SlugField(
        max_length=255, 
        null=True, 
        blank=True, 
        unique=True, 
        editable=False, 
        db_index=True
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="brand")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Marka")
        verbose_name_plural = _("Markalar")

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = unique_slug_generator(self, slugify(f"{self.name}"))
        
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('oluxana_detail', kwargs={'slug': self.slug})
    
class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")
    slug = models.SlugField(
        max_length=255, 
        null=True, 
        blank=True, 
        unique=True, 
        editable=False, 
        db_index=True
    )
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = unique_slug_generator(self, slugify(f"{self.name}"))
        
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Model")
        verbose_name_plural = _("Modellər")

class ProductKind(models.Model):
    slug = models.SlugField(
        max_length=255, 
        null=True, 
        blank=True, 
        unique=True, 
        editable=False, 
        db_index=True
    )
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = unique_slug_generator(self, slugify(f"{self.name}"))
        
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Məhsulun növü")
        verbose_name_plural = _("Məhsulun növü")

class Address(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Axtarış üçün ünvan")
        verbose_name_plural = _("Axtarış üçün ünvanlar")

class Morgue(models.Model):
    image = models.ImageField(upload_to="oluxana")
    wp_number = models.CharField(max_length=200)
    brand = models.ManyToManyField(Brand, related_name="morguebrand")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="morgueaddress")
    address_detail = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    staff_name = models.CharField(max_length=200, null=True, blank=True)
    map = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = _("Ölüxana")
        verbose_name_plural = _("Ölüxanalar")

class PersonalAnnouncement(models.Model):
    slug = models.SlugField(
        max_length=255, 
        null=True, 
        blank=True, 
        unique=True, 
        editable=False, 
        db_index=True
    )

    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    seller_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="personalannouncment", null=True, blank=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="personalannouncment", null=True, blank=True)
    motor = models.CharField(max_length=200, null=True, blank=True)
    car_year = models.CharField(max_length=200, null=True, blank=True)
    product_status = models.CharField(max_length=200, null=True, blank=True)
    product_kind = models.ForeignKey(ProductKind, on_delete=models.CASCADE, related_name="personalannouncment", null=True, blank=True)


    verified = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = unique_slug_generator(self, slugify(f"{self.name}"))
        
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('personal_announcement_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = _("Fərdi elan")
        verbose_name_plural = _("Fərdi elanlar")
    
class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(PersonalAnnouncement, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="announcement")

    def __str__(self) -> str:
        return self.announcement.name
    
    class Meta:
        verbose_name = _("Elan şəkili")
        verbose_name_plural = _("Elan şəkilləri")

class Socials(models.Model):
    social_type = models.CharField(max_length=200, choices=SOCIAL_CHOICES)
    link = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.social_type
    
    class Meta:
        verbose_name = _("Sosial şəbəkə")
        verbose_name_plural = _("Sosial şəbəkələr")

class ContactUs(models.Model):
    address = models.CharField(max_length=200)
    map_link = models.TextField(null=True)

    def __str__(self) -> str:
        return "Əlaqə"
    
    class Meta:
        verbose_name = _("Əlaqə")
        verbose_name_plural = _("Əlaqə")

class PhoneNumber(models.Model):
    contact_us = models.ForeignKey(ContactUs, on_delete=models.CASCADE, related_name="phone_number")
    phone_number = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.phone_number
    
    class Meta:
        verbose_name = _("Telefon nömrəsi")
        verbose_name_plural = _("Telefon nömrələri")

class Email(models.Model):
    contact_us = models.ForeignKey(ContactUs, on_delete=models.CASCADE, related_name="email")
    email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = _("Email ünvanı")
        verbose_name_plural = _("Email ünvanları")

class MainData(models.Model):
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=200)
    footer_text = models.TextField()
    logo = models.ImageField(upload_to="logo")
    favicon = models.ImageField(upload_to="logo", null=True, blank=True)
    map_url = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = _("Əsas məlumat")
        verbose_name_plural = _("Əsas məlumatlar")
