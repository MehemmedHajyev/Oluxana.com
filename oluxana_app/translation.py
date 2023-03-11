from oluxana_app.models import MainData, About, HomeSlider, ProductKind, Address, Morgue
from modeltranslation.translator import TranslationOptions, register


@register(MainData)
class MainDataTranslationOptions(TranslationOptions):
    fields = (
        "footer_text",
    )

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = (
        "text",
    )

@register(HomeSlider)
class HomeSliderTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
        "button_text",
    )

@register(ProductKind)
class ProductKindTranslationOptions(TranslationOptions):
    fields = (
        "name",
    )

@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = (
        "name",
    )

@register(Morgue)
class MorgueTranslationOptions(TranslationOptions):
    fields = (
        "address_detail",
        "description",
    )
