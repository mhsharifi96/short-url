from django.shortcuts import render
from rest_framework import viewsets
from .models import Links
from .serializers import LinksSerializers
from django.template.defaultfilters import slugify
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import redirect
from .helper import check_link
from django.core.cache import cache
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
        print(x_forwarded_for)
        # cache_main_url = cache.get(short_link)
        # if cache_main_url:
            
        #     return Response({'main_link':cache_main_url})
        # else :
        link = self.get_object()
        clean_link = check_link(link.main_link)
        # cache.set(short_link,clean_link,timeout=60)
        # return redirect(clean_link)
        return Response({'main_link':clean_link})
        

        # serializer = PasswordSerializer(data=request.data)
        # if serializer.is_valid():
        #     user.set_password(serializer.validated_data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)