
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from bls import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', views.main),
    path('register/', views.register),
)
