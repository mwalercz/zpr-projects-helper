from django.core.urlresolvers import reverse
# Create your tests here.
from django_webtest import WebTest

from projects_helper.apps.common.models import CustomUser


class RegistrationTest(WebTest):
    def test_custom_registration_view(self):
        response = self.app.get(reverse('common:register'))
        username = 'matika'
        self.assertFalse(CustomUser.objects.filter(username=username).exists())

        form = response.forms['registration_form']
        form['username'] = username
        password = "macienko123"
        form['password1'] = password
        form['password2'] = password
        form['email'] = "matika@gma.com"
        form.submit().follow()

        user_instance = CustomUser.objects.get(username=username)
        self.assertEqual(user_instance.username, username)
        self.assertEqual(user_instance.user_type, "S")
