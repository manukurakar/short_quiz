"""wwcs_quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from homepage.views import *
from quiz_page.views import QuizPage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginUser.as_view()),
    url(r'^login/$', LoginUser.as_view()),
    url(r'^manage_users/$', ManagePage.as_view()),
    url(r'^logout/$', LogoutUser.as_view()),
    url(r'^dashboard/$', LandingPage.as_view()),
    url(r'^profile/$', UserProfile.as_view()),
    url(r'^readuser/$', CreateUserFromFile.as_view()),
    url(r'^register/$', RegisterUser.as_view()),
    url(r'^online/(\S+)/$', QuizPage.as_view()),
    url(r'^exams/$', QuizCategories.as_view()),
    url(r'^editor/', QuizEditor.as_view()),

]
