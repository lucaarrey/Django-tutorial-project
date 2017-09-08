from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    question_list = Question.objects.all().order_by('pubblication_date')
    #show = ', '.join([q.question_text for q in question_list])
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("the result of your question: {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("votes of the question{}".format(question_id))

