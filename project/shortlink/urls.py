from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LinksViewSet

router = DefaultRouter()
redirect_link = LinksViewSet.as_view({'get': 'redirect_link'})

router.register(r'link', LinksViewSet, basename='link')
urlpatterns = [
    path('redirect/<str:short_link>/', redirect_link, name='redirect-link'),
]
urlpatterns += router.urls


