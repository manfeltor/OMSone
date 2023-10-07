from django.urls import path
from .views import login1, registration, list_registered_users
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('', login1, name="login"),
    path('registration/', registration, name="registration"),
    path('listusers/', list_registered_users, name="list_users"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
]