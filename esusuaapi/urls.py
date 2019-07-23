from rest_framework.routers import DefaultRouter
from .views import userViewset, groupViewset
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Esusu API Documentation")

router = DefaultRouter()
# the user and group paths
router.register('users', userViewset, base_name='users')
router.register('groups', groupViewset, base_name='groups')



urlpatterns =[
     path('rest-auth/',include('rest_auth.urls')),
     path('rest-auth/registration/', include('rest_auth.registration.urls')),
     path('invitations/', include('invitations.urls', namespace='invitations')),
     path('invitations/send-invite', include('invitations.urls', namespace='sendinvite')),
     path('api_documentation/',schema_view),

]

urlpatterns = urlpatterns + router.urls
