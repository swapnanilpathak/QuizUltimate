from django.shortcuts import render
from . models import Question
from django.contrib.auth.models import User
from accounts.models import QuizTaker
import os
# Create your views here.

def homepage(request):
	
	return render(request,'questions/homepage.html')

def startquiz1(request):
	# try the list shuffle solution also
	questions = Question.objects.all().order_by('?')[:4]
	return render(request,'questions/startquiz1.html',{'questions':questions})


def evaluate(request):
	questions = Question.objects
	
	total_questions = 4
	your_score=0
	l=[]

	
	key_list =[]
	for k in request.POST.keys():
		key_list.append(k)
	key_list.remove('csrfmiddlewaretoken')
	key_list.remove('submitquiz1')
	for i in key_list:
		
		your_answer = request.POST[i]
		l.append(your_answer)
		
		correct_answer = questions.get(pk=i)
		if(correct_answer.correctOption==your_answer):
			your_score+=1

	percentage = (your_score/total_questions)*100
	#add percentage to user model
	current_user = request.user
	print(current_user.username)
	print('old: ',current_user.quiztaker.score)
	if percentage > current_user.quiztaker.score:

		current_user.quiztaker.score=percentage
		current_user.quiztaker.save()
	print('new: ',current_user.quiztaker.score)
	return render(request,'questions/result.html',{'score':your_score,'percentage':percentage,'total_questions':total_questions})