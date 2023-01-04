from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MachineViewSet, ProjectViewSet, RoleViewSet, GroupViewSet, CurrentUserView, get_csrf_token

router = DefaultRouter()
router.register('Machine', MachineViewSet, basename='Machine')
router.register('Project', ProjectViewSet, basename='Project')
router.register('Role', RoleViewSet, basename='Role')
router.register('Group', GroupViewSet, basename='Group')
urlpatterns = [
    path('user/CurrentUser', CurrentUserView.as_view(), name='CurrentUser'),
    path('token', get_csrf_token, name='Token'),
]
urlpatterns += router.urls
