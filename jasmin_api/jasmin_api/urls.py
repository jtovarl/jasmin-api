from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from rest_api.views import GroupViewSet, UserViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet, base_name='groups')
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
