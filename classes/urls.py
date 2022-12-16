from django.urls import path, include

from rest_framework.routers import DefaultRouter

from classes import views


router = DefaultRouter()
router.register('school-class', views.SchoolClassViewSet)
router.register('student-enrollment', views.StudentEnrollmentViewSet,)

urlpatterns = [
    path('', include(router.urls))
]
