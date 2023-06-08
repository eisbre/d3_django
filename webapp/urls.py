from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('app.urls')),
    path('chart1/', include('app.urls')),
    path('chart2/', include('app.urls')),
    path('admin/', admin.site.urls),
]
