"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from items.views import delete_item, view_home, create_item, view_items, update_item, search_items


urlpatterns = [
    path('', view_home, name='home'),
    path("admin/", admin.site.urls),
    path('users/', include('users.urls')),

    path('items', view_items, name='list-items'),
    path('create_items', create_item, name='create-item'),
    path('delete_item/<item_id>', delete_item, name='delete-item'),
    path('update_item/<item_id>', update_item, name='update-item'),
    path('search_items', search_items, name='search-item'),

]

# To ensure the server serves static files
if bool(settings.DEBUG): 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Used in development to serve user uploaded files
