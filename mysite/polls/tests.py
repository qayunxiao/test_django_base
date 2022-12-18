from django.test import TestCase
from django.test import Client
#用来写测试
# Create your tests here.
from django.utils import timezone
from polls.models import Question
from polls.models import Choice
# class QuesionTestCase(TestCase):
#     def setUp(self):
#         Question.objects.create(id=1,question_text="what is new?",pub_date=timezone.now())
#
#     def test_question_create(self):
#         Question.objects.create(id=5,question_text="what is new?",pub_date=timezone.now())
#         q= Question.objects.get(id=5)
#         self.assertEqual(q.question_text,"what is new?")
#
#     def test_question_query(self):
#         q=Question.objects.get(id=1)
#         print("q:",q)
#         self.assertEqual(q.question_text,"what is new?")
#
#     def test_question_update(self):
#         q= Question.objects.get(id=1)
#         q.question_text="吃东西?"
#         q.save()
#         q2=Question.objects.get(id=1)
#         self.assertEqual(q2.question_text,"吃东西?")
#
#     def test_question_delete(self):
#         q=Question.objects.get(id=1)
#         q.delete()
#         #删除之后没数据
#         all=Question.objects.all()
#         print("all:",all)
#         self.assertEqual(len(all),0)

class IndexTestCase(TestCase):
    def setUp(self):
        Question.objects.create(id=1,question_text="what is new?",pub_date=timezone.now())
        Choice.objects.create(id=1,choice_text="Not much",votes=0,question_id=1)
        Choice.objects.create(id=2,choice_text="The SKY",votes=888,question_id=1)

    def test_index_page(self):
        c=Client()
        response = c.get("/polls/")
        print(response.status_code)
        # self.assertEqual(response.status_code,200)
        # self.assertIn(b"what is new?" ,response.content)
        self.assertTemplateUsed(response,'polls/index.html')

    def test_detail_page(self):
        c=Client()
        response = c.get("/polls/1/")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"what is new?" ,response.content)
        self.assertIn(b"Not much" ,response.content)
        self.assertIn(b"The SKY" ,response.content)
        self.assertTemplateUsed(response,'polls/detail.html')

    def test_result_page(self):
        c=Client()
        response = c.get("/polls/1/results/")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"what is new?" ,response.content)
        self.assertIn(b"Not much" ,response.content)
        self.assertIn(b"The SKY" ,response.content)
        self.assertIn(b"888" ,response.content)
        self.assertTemplateUsed(response,'polls/results.html')
    def test_vote_page(self):
        c=Client()
        response = c.post("/polls/1/vote/",data={"choice":2})
        self.assertEqual(response.status_code,302)
        response = c.get("/polls/1/results/")
        self.assertEqual(response.status_code,200)
        self.assertIn(b"889" ,response.content)
