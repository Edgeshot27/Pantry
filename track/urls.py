from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.item_list,name='item_list'),
    path('add_item_view/',views.add_item_view,name='add_item_view'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('increase_quantity/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
