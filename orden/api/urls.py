from orden.api.api import OrdenAPIViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orden', OrdenAPIViewsets, basename='user')
urlpatterns = router.urls