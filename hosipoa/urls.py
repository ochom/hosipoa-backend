from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('bugs.urls')),
    path('api/organization/', include('organization.urls')),
    path('api/records/', include('records.urls')),
    path('api/outpatient/', include('outpatient.urls')),
    path('api/revenue/', include('revenue.urls')),
    path('api/laboratory/', include('laboratory.urls')),
    path('api/radiology/', include('radiology.urls')),
    path('api/pharmacy/', include('pharmacy.urls')),
    path('api/inpatient/', include('inpatient.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/mpesa/', include('mpesa.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
