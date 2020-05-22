from django.contrib import admin
from django.urls import path, include
from App_ABC import urls as App_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(App_urls)),
]
