from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from SEL4C.app1 import views
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView
from drf_spectacular.views import SpectacularAPIView

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet) 
router.register(r'admins', views.AdminViewSet)
router.register(r'emprendedor', views.EmprendedorViewSet)


#Wire up our API using automatic URL routing.
# Additionally, we include login URLS for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework')),
    path("admin/", admin.site.urls),
    
    #OpenApi
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI:
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]