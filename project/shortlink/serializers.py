from rest_framework import serializers
from django.template.defaultfilters import slugify

from .models import Links


class LinksSerializers(serializers.ModelSerializer):


    def create(self,validated_data):
        print('test')
        validated_data['short_link'] = slugify(validated_data['short_link'])
        if not Links.objects.filter(short_link=validated_data['short_link']).exists():
            return Links.objects.create(**validated_data)
        raise serializers.ValidationError({'error':'short link should be unique !'})



    class Meta : 
        model = Links
        fields = ('short_link','main_link')
        lookup_field = 'short_link'
    

    

