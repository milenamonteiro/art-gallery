from .api import UserViewSet
from .views import SignUpView
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')

router.urls.append(path('signup/', SignUpView.as_view(), name='signup'))
urlpatterns = router.urls
