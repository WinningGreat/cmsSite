from django.contrib import admin
from mezzanine.pages.admin import PageAdmin, deepcopy
from .models import SalePage, digital_item, physical_item
# Register your models here.

class digital_item_inline(admin.TabularInline):
    model = digital_item

class physical_item_inline(admin.TabularInline):
    model = physical_item

class SalePageAdmin(PageAdmin):
    inlines = (digital_item_inline,physical_item_inline,)
    fieldsets = deepcopy(PageAdmin.fieldsets)


admin.site.register(SalePage,SalePageAdmin)