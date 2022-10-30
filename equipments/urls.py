from django.urls import path
from . import views


urlpatterns =[
    path('',views.equipment, name ="equipment"),
    path('cart/', views.cart, name ="cart"),
    path('login/', views.login_auth, name = "login"),
    path('logout/', views.logout_auth, name ="logout"),
    path('signup/', views.signup_auth, name="signup"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('checkout/', views.checkout, name ="checkout"),
    path('procced-to-pay/', views.processOrder, name ="process_order"),



]

