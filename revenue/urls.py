from django.urls import path, include
from rest_framework.routers import DefaultRouter

from revenue import views

router = DefaultRouter()
router.register('invoices', views.InvoiceViewSet)
router.register('payments', views.InvoicePaymentViewSet)
router.register('deposits', views.DepositViewSet)
router.register('service-requests', views.ServiceRequestViewSet)
router.register('payment-queue', views.PaymentQueueViewSet)
router.register('service-requests-queue', views.ServiceRequestQueue)
router.register('upload-download', views.UploadDownloadInvoice, basename="upload n download invoice")

urlpatterns = [
    path('', include(router.urls)),
]
