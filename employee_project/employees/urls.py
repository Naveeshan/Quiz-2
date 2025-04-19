from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('attendance', AttendanceViewSet)
router.register('performance', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
