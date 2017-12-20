from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
import json
from quiz_page.models import quiz
from homepage.models import studentResponse


# Create your views here.

class QuizPage(View):
    def get(self,request,q_id):
        if request.user.is_authenticated:
            if studentResponse.objects.filter(Q(mobile_no=request.user.username)&Q(quiz_id=q_id)).count():
                return render(request, 'attempted.html');
            else:
                try:
                    question = json.loads(quiz.objects.get(quiz_id=q_id).questions);
                    context = {
                        'quiz_id': 'current-1',
                        'questions': question
                    }
                    return render(request, 'quiz_page.html', context);
                except:
                    raise Http404("Error Happened! Contact Administrator");
        else:
            return HttpResponseRedirect('/login/')


    def post(self,request,q_id):
        if request.user.is_authenticated:
            quiz_id = request.POST.get('quiz_id');
            quiz_obj = quiz.objects.get(quiz_id=quiz_id)
            question = json.loads(quiz_obj.questions);
            hold = quiz_obj.result_hold
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
            save_marks = studentResponse(mobile_no=request.user.username,quiz_id=quiz_id,marks=total_score,student_response=student_response)
            save_marks.save()
            context = {
                'marks':total_score,
                'student_response':student_response,
                'question':question,
                'unattempted':unattempted
            }
            if hold:
                return render(request, 'hold.html', context)
            else:
                return render(request,'result.html',context)
        else:
            return HttpResponseRedirect('/login/')