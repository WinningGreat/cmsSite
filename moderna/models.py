from django.db import models
from mezzanine.pages.models import Page,RichText
# Create your models here.

class SalePage(Page,RichText):
    #
    pass


class Item(models.Model):
    abstract = True
    item_name = models.CharField(max_length=255)
    item_rating = models.IntegerField()
    item_price = models.FloatField()
    item_image = models.ImageField(upload_to="item/images")
    item_status = models.CharField(max_length=255,choices=(('AVAILABLE','A/V'),('NOT AVAILABLE','N/A')))
    SalePage = models.ForeignKey(SalePage)
    class Meta:
        abstract = True

class digital_item(Item):

    number_of_downloads = models.IntegerField()

class physical_item(Item):


    item_weight = models.FloatField()
    shipping_cost = models.FloatField()
    item_state = models.CharField(max_length=255,choices=(('Item is new','new'),('Item has been refurbished','refurbished'),('Item is fairly used','used')))
