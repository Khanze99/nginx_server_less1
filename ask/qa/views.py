from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

from .models import Question
from .forms import AskForm, AnswerForm
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    return render(request, 'qa/question_detail.html', {'question': question, 'answers': answers})
    


def question_list(request):
    page_number = request.GET.get('page', 1)
    limit = 10
    objects = Question.objects.new()
    paginator = Paginator(objects, limit)
    questions = paginator.get_page(page_number)
    return render(request, 'qa/index.html', {'questions': questions})

def popular_question_list(request):
    page_number = request.GET.get('page', 1)
    limit = 10
    objects = Question.objects.popular()
    paginator = Paginator(objects, limit)
    questions = paginator.get_page(page_number)
    return render(request, 'qa/index.html', {'questions': questions})


def post_ask(request):
    if request.POST:
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            question = question.id
            return HttpResponseRedirect(f'/question/{question}/')
    form = AskForm()
    return render(request, 'qa/new_post.html', {'form': form})
