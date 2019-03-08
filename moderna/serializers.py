from rest_framework import serializers
from .models import digital_item, physical_item

class DigitalItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = digital_item
        fields = ('item_name','item_rating','item_price','item_image','item_status','slug','item_id','number_of_downloads')



class PhysicalItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = physical_item
        fields = '__all__'