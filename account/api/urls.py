from rest_framework import routers

from account.api.views import UserView, GroupView

app_name = 'api_user'
namespace = app_name


router = routers.DefaultRouter()
router.register(r'user', UserView, basename='user')
router.register(r'group', GroupView, basename='group')

urlpatterns = router.urls
