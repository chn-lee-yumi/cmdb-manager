from rest_framework.routers import DefaultRouter

from .views import MachineViewSet, ProjectViewSet, RoleViewSet, GroupViewSet

router = DefaultRouter()
router.register('Machine', MachineViewSet, basename='Machine')
router.register('Project', ProjectViewSet, basename='Project')
router.register('Role', RoleViewSet, basename='Role')
router.register('Group', GroupViewSet, basename='Group')
urlpatterns = []
urlpatterns += router.urls
