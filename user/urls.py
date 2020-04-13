from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_note, delete_note, register


urlpatterns = [
    url(r'home$', home, name="user_home"),
    url(r'login$', LoginView.as_view(template_name="user/login_form.html"),
        name="user_login"),
    url(r'logout$', LogoutView.as_view(), name="user_logout"),
    url(r'register$', register, name='register'),
    url(r'note$', new_note, name="user_new_note"),
    url(r'delete/(?P<id>\d+)/$', delete_note, name="user_delete_note"),
]