from django.contrib import admin
from django.urls import path
from products.views import product_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', product_view),
]
