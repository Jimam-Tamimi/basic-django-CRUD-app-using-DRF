from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'students', StudentViewSet)

urlpatterns = router.urls