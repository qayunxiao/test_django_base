from django.test import TestCase
#用来写测试
# Create your tests here.
from django.utils import timezone
from polls.models import Question

class QuesionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(id=1,question_text="what is new?",pub_date=timezone.now())

    def test_question_create(self):
        Question.objects.create(id=5,question_text="what is new?",pub_date=timezone.now())
        q= Question.objects.get(id=5)
        self.assertEqual(q.question_text,"what is new?")

    def test_question_query(self):
        q=Question.objects.get(id=1)
        print("q:",q)
        self.assertEqual(q.question_text,"what is new?")

    def test_question_update(self):
        q= Question.objects.get(id=1)
        q.question_text="吃东西?"
        q.save()
        q2=Question.objects.get(id=1)
        self.assertEqual(q2.question_text,"吃东西?")

    def test_question_delete(self):
        q=Question.objects.get(id=1)
        q.delete()
        #删除之后没数据
        all=Question.objects.all()
        print("all:",all)
        self.assertEqual(len(all),0)