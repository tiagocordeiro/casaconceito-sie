"""casaconceito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# from django.contrib import admin
# from django.urls import path, re_path, include

# from pages.views import home_view
# from parceiros.views import home_parceiros
from casaconceito import settings

admin.site.site_header = 'Casa Conceito'

urlpatterns = [
    # re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    # url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('parceiros.urls')),
    # path('', home_view, name='home'),
    # path('', index, name='parceiros_home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
