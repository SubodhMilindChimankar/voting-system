from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home(request):
    form = Question.objects.order_by('-pub_date')[:5]
    context = {
        'form': form
    }
    return render(request, 'home.html', context)

def index(request):
    form = Question.objects.order_by('-pub_date')[:5]
    context = {
        'form':form
    }
    return render(request,'index.html',context)

def detail(request,id):
    try:
        form = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404('Question not found')
    return render(request,'detail.html',{'form':form})

def result(request,id):
    form = get_object_or_404(Question,id =id)
    return render(request,'result.html',{'form':form})

def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls / detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('result', args =(question.id, )))