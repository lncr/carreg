from rest_framework.routers import SimpleRouter

from cars.views import CarViewSet

router = SimpleRouter()

router.register('cars', CarViewSet)

urlpatterns = []

urlpatterns += router.urls
