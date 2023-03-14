
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from bls import views


admin.site.site_header = "de factum Education"
admin.site.site_title = "de factum Education"
admin.site.index_title = "de factum Education"







urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('coursepage/<int:pk>', views.coursedetail),
    path('register/', views.register),
)
