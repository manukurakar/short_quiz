from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout,user_logged_in
from django.views import View
from quiz_page.models import quiz
from homepage.models import students
from homepage.models import studentResponse
from django.contrib.auth.models import User
from homepage.user_reg_form import RegistrationForm
import regex as re

# Create your views here.

class LandingPage(View):
    def get(self,request):
        if request.user.is_authenticated:
            active_questions = quiz.objects.all();
            context = {
                'questions':active_questions
            }
            if students.objects.filter(mobile_no=request.user.username).count():
                return render(request, 'index.html', context);
            else:
                return HttpResponseRedirect('/profile/')

        else:
            return HttpResponseRedirect('/login/')

    def post(self,request):
        return HttpResponse("Error Page not found");


class LoginUser(View):
    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request,'login.html')

    def post(self,request):
        login_credentials = request.POST
        username = login_credentials.get('mobile')
        password = login_credentials.get('password')
        password1 = login_credentials.get('password1')
        error_message = None
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                if students.objects.filter(mobile_no=username).count():
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return HttpResponseRedirect('/profile/')
            else:
                return HttpResponse('User not active, please contact admin')
        error_message = "Invalid username or password, Please login again"
        return HttpResponse(error_message)
        #todo implement login logic

class RegisterUser(View):
    def get(self,request):
        # If get request is available on the url redirect to login page, we expect post request on this url
        return HttpResponseRedirect('/login/')

    def post(self,request):
        if not request.user.is_authenticated():
            new_user_data = request.POST
            mobile = new_user_data.get('mobile')
            password = new_user_data.get('password')
            is_valid,errors = self.reg_form_is_valid(new_user_data)

            if is_valid:
                user = User.objects.create_user(username=mobile,password=password)
                # user.set_password(user.password)
                user.save()

                """ Now automatic login for user"""
                user = authenticate(username =mobile, password = password )
                login(request,user)
                return HttpResponseRedirect('/profile/')
            else:
                # This block generates the error message to the frontend. Unable to register
                # todo implement the page to display the error messages
                context = {
                    'error_message': errors

                }
                return  HttpResponse(errors)

        else:
            # Here we handles the case when user already logged in. Logged in users were not allowed to sign in again
            # todo implement the logic to redirect to the home page incase logged in
            return HttpResponse("Redirect to home page")

    def reg_form_is_valid(self,new_user_data):
        is_valid = True
        error_det = []
        # Check mobile number valid or not
        mobile = new_user_data.get('mobile');
        password = new_user_data.get('password');
        password1 = new_user_data.get('password1');
        # if not re.match(r'^[789]\d{9}$', mobile, flags=0):
        #     is_valid = False
        #     error_det.append("Invalid Mobile number.<br> ");
        # Check whether mobile number already registered or not
        if User.objects.filter(username=mobile).count():
            is_valid = False
            error_det.append('Mobile Number already registered.<br>  ')

        if password != password1:
            is_valid = False
            error_det.append('Passwords not matching. <br> ')
        return is_valid,error_det


class CreateUserFromFile(View):
    def get(self,request):
        with open('users.txt','r') as data:
            count = 1
            for line in data:
                user = User.objects.create_user(username=line, password='wwcs')
                user.save();
        return HttpResponse("Check log")









# Create a  categories page here

class QuizCategories(View):
    def get(self, request):
        raise Http404

    def post(self,request):
        if request.user.is_authenticated:
            q_id = request.POST.get('q_id');

            try:
                quiz.objects.get(quiz_id=q_id);
                return HttpResponseRedirect('/online/' + q_id);
            except:
                raise Http404("Page not available");
        else:
            return HttpResponseRedirect('/login/')


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



class LogoutUser(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/login/')

    def post(self,request):
        logout(request)
        return HttpResponseRedirect('/login/')


class UserProfile(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,'userprofile.html')
        else:
            return HttpResponseRedirect('/login/')

    def post(self,request):
        if request.user.is_authenticated:
            mobile_no = request.user.username
            name = request.POST.get('name')
            location = request.POST.get('location')
            school = request.POST.get('school')
            dob = request.POST.get('dob')
            parent_contact = request.POST.get('parent')
            profile = students(mobile_no=mobile_no,location=location,school=school,dob=dob,parent_contact=parent_contact,name=name)
            profile.save()
            return HttpResponseRedirect('/dashboard/')
        else:
            return HttpResponseRedirect('/login/')


class ManagePage(View):
    def get(self,request):
        if request.user.is_authenticated:
            user_details = students.objects.all()
            student_res = studentResponse.objects.all()
            context = {'user_det': user_details,
                       'std_rsp':student_res}
            if request.user.is_staff:
                return render(request,'manage.html',context)
            else:
                return HttpResponse("You are not authorised to view this")
        else:
            return HttpResponseRedirect('/login/')
    def post(self,request):
        pass
