from django.test import TestCase

from main.models import Category


class CategoryTest(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='Best Picture')
        Category.objects.create(name='Best Sound Score')

    def test_category_name(self):
        best_picture = Category.objects.get(name='Best Picture')
        best_sound_score = Category.objects.get(name='Best Sound Score')

        self.assertEqual(str(best_picture), 'Best Picture')
        self.assertEqual(str(best_sound_score), 'Best Sound Score')
