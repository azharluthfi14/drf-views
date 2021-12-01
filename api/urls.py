from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import ListItems, DetailItem, ItemsListGeneric, ItemDetailGeneric, ItemsViewSet

from rest_framework import routers
""" URL APIViews """

urlpatterns = [
    path('api/view', ListItems.as_view()),
    path('api/view/<pk>', DetailItem.as_view()),
]

""" URL Generic Views """
urlpatterns = [
    path('api/generic-view/', ItemsListGeneric.as_view()),
    path('api/generic-view/<pk>', ItemDetailGeneric.as_view()),
]

""" URL Viewset """
# router = routers.DefaultRouter()
# router.register(r'viewset', ItemsViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
