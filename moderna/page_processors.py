from django import forms
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import SalePage, Item, digital_item

@processor_for(SalePage)
def item_view(request, page):
    if request.method == "GET":
        items = digital_item.objects.all()

    return {"items":items}

