from rest_framework import routers

from directory.views import MarkViewSet, BrandViewSet


router = routers.SimpleRouter()
router.register('marks', MarkViewSet)
router.register('brands', BrandViewSet)

urlpatterns = []

urlpatterns += router.urls
