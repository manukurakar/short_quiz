from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from quiz_page.models import quiz
from homepage.models import students

# Create your views here.

class LandingPage(View):
    def get(self,request):
        active_questions = quiz.objects.all();
        context = {
            'questions':active_questions
        }
        return render(request,'index.html',context);

    def post(self,request):
        return HttpResponse("Error Page not found");


# Create a  categories page here

class QuizCategories(View):
    def get(self, request,q_id):
        context = {
            'q_id':q_id
        }
        return render(request,'categoryPage.html',context);

    def post(self,request):
        passcode = request.POST.get('passcode');
        mobile = request.POST.get('mobile');
        q_id = request.POST.get('q_id');

        try:
            quiz.objects.get(quiz_id=q_id);
            if passcode.upper() == 'WWCS':
                student_details = students(mobile_no=mobile);
                student_details.save();
                return HttpResponseRedirect('/online/'+q_id);
            else:
                return HttpResponse("Incorrect Username or password");
        except:
            raise Http404("Page not available");


#Create question editor here

class QuizEditor(View):
    def get(self,request):
        return render(request,'quiz_editor.html')

    def post(self,request):
        quiz_id = request.POST.get('quiz_id');
        quiz_cat = request.POST.get('cat');
        quiz_auth = request.POST.get('author');
        questions = request.POST.get('question_json');
        quiz_save = quiz(quiz_id=quiz_id,cat=quiz_cat,auth=quiz_auth,questions=questions);
        quiz_save.save();
        return HttpResponse("Question Saved");

