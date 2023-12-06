from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import home, product_list, add_product, register
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),
    path('accounts/profile/', RedirectView.as_view(url='/'), name='profile'),
]
