from client.api.api import ClientAPIViewsets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'client', ClientAPIViewsets, basename='user')
urlpatterns = router.urls