from django.test import TestCase
from model_mommy import mommy

from ..models import Project, Lecturer


class ProjectTest(TestCase):

    def test_lecturer_creates_project(self):
        lecturer = mommy.make(Lecturer)
        project = Project.objects.create(lecturer=lecturer)
        self.assertEqual(project.lecturer, lecturer)

    def test_status(self):
        instance = mommy.make(Project)
        self.assertEqual(instance.status(), "free")
