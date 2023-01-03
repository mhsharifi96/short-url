from rest_framework import serializers
from django.template.defaultfilters import slugify

from .models import Links,Links_log,packets_log


class LinksSerializers(serializers.ModelSerializer):
    def create(self,validated_data):
        
        validated_data['short_link'] = slugify(validated_data['short_link'])
        if not Links.objects.filter(short_link=validated_data['short_link']).exists():
            return Links.objects.create(**validated_data)
        raise serializers.ValidationError({'error':'short link should be unique !'})



    class Meta : 
        model = Links
        fields = ('short_link','main_link')
        lookup_field = 'short_link'
    

    

class Links_logSerializers(serializers.ModelSerializer):

    class Meta : 
        model = Links_log
        fields = '__all__'
        

class Packets_logSerializers(serializers.ModelSerializer):

    class Meta : 
        model = packets_log
        fields = '__all__'
