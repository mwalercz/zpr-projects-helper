from django.conf.urls import url, include

from projects_helper.apps.common.views import CustomRegistrationView, user_login

urlpatterns = [
    url(r'^login/$',
        user_login,
        name="login"),
    url(r'^register/$',
        CustomRegistrationView.as_view
        (template_name='registration/registration_form.html'),
        name="register"),

]
