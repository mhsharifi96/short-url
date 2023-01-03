from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LinksViewSet,packetsLogViewSet,LinksLogViewSet

router = DefaultRouter()

router.register(r'link', LinksViewSet, basename='link')
router.register(r'packet', packetsLogViewSet, basename='packet')
router.register(r'link-log', LinksLogViewSet, basename='link-log')

# cusom link
redirect_link = LinksViewSet.as_view({'get': 'redirect_link'})


urlpatterns = [
    # path('<str:short_link>/', redirect_link, name='redirect-link-root'),
    path('redirect/<str:short_link>/', redirect_link, name='redirect-link'),
]
urlpatterns += router.urls


