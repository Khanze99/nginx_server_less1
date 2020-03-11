from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Question
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_list(request):
    page_number = request.GET.get('page', 1)
    limit = 10
    objects = Question.objects.new()
    paginator = Paginator(objects, limit)
    page_object = paginator.get_page(page_number)

    
