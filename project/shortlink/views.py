from django.shortcuts import render
from rest_framework import viewsets
from .models import Links,Links_log,packets_log
from .serializers import LinksSerializers,Packets_logSerializers,Links_logSerializers
from django.template.defaultfilters import slugify
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import redirect
from django.core.cache import cache

from .helper import check_link
from .crud import create_link_log,update_count_view
# Create your views here.


class LinksViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing link instances.
    """
    serializer_class = LinksSerializers
    queryset = Links.objects.all()
    lookup_field = 'short_link'

    @action(detail=True, methods=['get'])
    def redirect_link(self, request, short_link=None):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR',None)
        x_forwarded_host = request.META.get('HTTP_X_FORWARDED_HOST',None)
       
        create_link_log(
            cookie = request.COOKIES.get('csrftoken'),
            user_agent = request.META['HTTP_USER_AGENT'],
            dst_ip = x_forwarded_for,
            src_ip = x_forwarded_host,
            link = request.get_full_path()
        )
        link = self.get_object()
        clean_link = check_link(link.main_link)
        update_count_view(link)
        
        return Response({'main_link':clean_link})

    @action(detail=True, methods=['get'])
    def redirect_link_cache(self, request, short_link=None):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR',None)
        x_forwarded_host = request.META.get('HTTP_X_FORWARDED_HOST',None)
        create_link_log(
            cookie = request.COOKIES.get('csrftoken'),
            user_agent = request.META['HTTP_USER_AGENT'],
            dst_ip = x_forwarded_for,
            src_ip = x_forwarded_host,
            link = request.get_full_path()
        )
        cache_main_url = cache.get(short_link)
        if cache_main_url:
            
            return Response({'main_link':cache_main_url})
        else :
            link = self.get_object()
            clean_link = check_link(link.main_link)
            update_count_view(link)
            cache.set(short_link,clean_link,timeout=60)
        # return redirect(clean_link)
        return Response({'main_link':clean_link})

    @action(detail=True, methods=['get'])
    def analyse(self, request, short_link=None):
        pass

        

class LinksLogViewSet(viewsets.ModelViewSet):

    serializer_class = Links_logSerializers
    queryset = Links_log.objects.all()

    


class packetsLogViewSet(viewsets.ModelViewSet):

    serializer_class = Packets_logSerializers
    queryset = packets_log.objects.all()

    