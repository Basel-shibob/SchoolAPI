from django.urls import path, include
from people import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('teachers',views.TeacherViewSet)
router.register('students',views.StudentViewSet)

urlpatterns = [
    path('',include(router.urls))
]

