from django.conf.urls import url, include
from django.contrib import admin
from hoteldeals import views
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', views.users)
# # router.register(r'hotel_deals', views.)
# router.register(r'^hotels_list/(?P<user_id>\d+)/$', views.hotels_list)
# router.register(r'stats', views.stats)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(router.urls)),
    # # Wire up our API using automatic URL routing.
    # # Additionally, we include login URLs for the browsable API.
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^$', views.index, name='index')
    url(r'^hotels_list/(?P<no_of_pages>\d+)/$', views.hotels_list),
    url(r'stats', views.stats)
]
