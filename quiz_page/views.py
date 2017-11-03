from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
import json
from quiz_page.models import quiz


# Create your views here.

class QuizPage(View):
    def get(self,request,q_id):
        try:
            question = json.loads(quiz.objects.get(quiz_id=q_id).questions);
            context = {
                'quiz_id': 'current-1',
                'questions': question
            }
            return render(request, 'quiz_page.html', context);
        except:
            raise Http404("Error Happened! Contact Administrator");


    def post(self,request,q_id):
        quiz_id = request.POST.get('quiz_id');
        question = json.loads(quiz.objects.get(quiz_id=quiz_id).questions);
        total_questions = len(question);
        student_response = [];

        # Create a list with students response
        for i in range(total_questions):
            q_id = 'q_'+str(i+1)
            student_response.append(request.POST.get(q_id))

        # Create a list of student score
        student_score = [];
        for index, items in enumerate(question):
            correct = items['correct']
            if student_response[index]==None:
                student_score.append(0)
            elif correct != student_response[index]:
                student_score.append(-1*items['negative'])
            else:
                student_score.append(items['marks'])
        total_score = sum(student_score);
        unattempted = student_response.count(None)
        context = {
            'marks':total_score,
            'student_response':student_response,
            'question':question,
            'unattempted':unattempted
        }
        return render(request,'result.html',context)