from django.test import TransactionTestCase
from polls.models import Question
from django.utils import timezone

class TransactionTests(TransactionTestCase):

    def test_object_persists_after_exception(self):
        Question.objects.create(
            question_text="Transaction test",
            pub_date=timezone.now()
        )

        try:
            raise RuntimeError("Simulated error")
        except RuntimeError:
            pass

        self.assertEqual(Question.objects.count(), 1)
