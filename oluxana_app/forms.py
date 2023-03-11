from django import forms
from django.forms import inlineformset_factory

from oluxana_app.models import PersonalAnnouncement, AnnouncementImage


class AnnouncementImageForm(forms.ModelForm):
    class Meta:
        model = AnnouncementImage
        fields = ['image']

        widgets = {
            'image': forms.FileInput(attrs={'required': 'required', 'class': 'form-control', 'multiple': 'multiple', 'hidden': 'hidden'})
        }

AnnouncementImageFormSet = inlineformset_factory(PersonalAnnouncement, AnnouncementImage, form=AnnouncementImageForm, extra=1, can_delete=False, )

class CreateAnnouncementForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('Yeni', 'Yeni'),
        ('İkinci əl', 'İkinci əl'),
    ]
    product_status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = PersonalAnnouncement
        fields = (
            "name", 
            "price",
            "email",
            "seller_name",
            "description",
            "phone",
            "brand",    
            "motor",
            "car_year",
            "product_kind",
            "model",
            "product_status"
        )

        widgets = {
                'price': forms.TextInput(attrs={'required': 'required', 'name': 'full_name', 'placeholder': 'Qiyməti'}),
                'brand': forms.Select(),
                'model': forms.Select(),
                'product_kind': forms.Select(),
                'car_year': forms.TextInput(attrs={'required': 'required', 'name': 'full_name', 'placeholder': 'Buraxılış ili'}),
                'name': forms.TextInput(attrs={'required': 'required', 'name': 'full_name', 'placeholder': 'Satacağınız məhsul'}),
                'phone': forms.TextInput(attrs={'required': 'required', 'name': 'full_name', 'placeholder': 'Telefon'}),
                'seller_name': forms.TextInput(attrs={'required': 'required', 'name': 'full_name', 'placeholder': 'Əlaqədar şəxs'}),
                'email': forms.TextInput(attrs={'required': 'required', 'name': 'full_name', 'placeholder': 'Elektron poçt ünvanı'}),
                'motor': forms.TextInput(attrs={'required': 'required', 'name': 'full_name', 'placeholder': 'Motorun həcmi'}),
                'description': forms.Textarea(attrs={'required': 'required', 'name': 'message', 'placeholder': 'Əlavə qeydlər'}),
            }
    image_formset = AnnouncementImageFormSet()
    