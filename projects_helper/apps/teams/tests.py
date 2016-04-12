from django.core.urlresolvers import reverse
from django_webtest import WebTest
from model_mommy import mommy
from .models import Team


class TeamTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Team)
        self.assertTrue(isinstance(instance, Team))


    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('teams:create'))
        new_name = 'A freshly created thing'

        # check that we don't already have a model with this name
        self.assertFalse(Team.objects.filter(name=new_name).exists())

        form = response.forms['team_form']
        form['name'] = new_name
        form.submit().follow()

        instance = Team.objects.get(name=new_name)
        self.assertEqual(instance.name, new_name)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Team)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)


    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Team)
        pk = instance.pk
        response = self.app.get(reverse('teams:delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Team.objects.filter(pk=pk).exists())
