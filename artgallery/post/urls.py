from .api import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/post', PostViewSet, 'post')

urlpatterns = router.urls
