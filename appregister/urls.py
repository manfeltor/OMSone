from django.urls import path
from .views import login1, registration, list_registered_users, list_delete_users, delete_users, delete_users_success, update_user
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('', login1, name="login"),
    path('registration/', registration, name="registration"),
    path('listusers/', list_registered_users, name="list_users"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('listdeleteusers/', list_delete_users, name="list_delete_users"),
    path('deleteusers/', delete_users, name="delete_users"),
    path('deleteuserssuccess/', delete_users_success, name="delete_users_success"),
    path('updateuser/', update_user, name="update_user"),
]