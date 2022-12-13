from django.shortcuts import render, get_object_or_404
# 页面 --》处理层view --》数据库数据
# 当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象
# 作为第一个参数，被“捕获”的参数以关键字参数的形式传入
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from polls.models import Question,Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_qlist'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def vote(request, question_id):
#     model = Question
#     template_name = 'polls/results.html'

# def index(request):
#     latest_qlist = Question.objects.order_by('-pub_date')[:5]
#     # output=','.join([q.question_text for q in latest_qlist])
#     context={'latest_qlist':latest_qlist}
#     return  render(request,"polls/index.html",context)
#  #question_id 要与path里的值一致，path('<int:question_id>/', views.detail, name='detail'),
# def detail(request, question_id):
#     print("问题id",question_id)
#     try:
#         q = Question.objects.get(id=question_id)
#     except Question.DoesNotExist:
#         raise Http404("ID 不存在！")
#     print(q,q.question_text)
#     c1=Choice.objects.filter(question_id=q.id)
#     print(c1)
#     for c in c1:
#         print(c)
#     return render(request,"polls/detail.html",{'question':q})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))