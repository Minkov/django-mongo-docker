from django.contrib.auth.models import User
from django.views.generic import ListView


class UsersListView(ListView):
    model = User
    template_name = "users_list.html"
