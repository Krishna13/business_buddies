from django.urls import path
from buddies_app import views

urlpatterns = [
    path("", views.render_login, name="render_login"),
    path("perform_login", views.perform_login, name="perform_login"),
    path("logout", views.logout_it, name="logout"),
    path("admin_home/", views.admin_home, name="admin_home"),
    path("create_orders/", views.render_create_orders, name="render_create_orders"),
    path("create_products/", views.render_create_products, name="render_create_products"),
]