from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Question
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
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
