from modeltranslation.translator import register, TranslationOptions
from .models import Category, Company, AdvertCategory, Advert


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
		fields = ("title",)


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
		fields = ("name", "author",  "breve", "description", "website", "phone", "date_posted", "category", "location",)

@register(AdvertCategory)
class AdvertCategoryTranslationOptions(TranslationOptions):
		fields = ("title",)


@register(Advert)
class AdvertTranslationOptions(TranslationOptions):
		fields = ("name", "author",  "breve", "description", "website", "phone", "date_posted", "category", "location",)
