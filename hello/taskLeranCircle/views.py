from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import models
from django.template import Context, loader, RequestContext
import json,requests
from hello.settings import API
from taskLeranCircle.models import Course, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

def getCourses(page):
	
	course_object = Course.objects.all()
	paginator = Paginator(course_object, 10)
	courses = paginator.page(page)
	course_data = dict()
	previous_page_number = page -1
	next_page_number = page + 1
	for course in courses:
		course_data[course.id]=course.title
	data = {'data': course_data, 'previous_page_number':previous_page_number, 'next_page_number': next_page_number}
	return data

def home(request):
	
	page = 1
	course_object = Course.objects.all()
	try:
		page  = int(request.GET['page'])
	except:
		# If page is not an integer, deliver first page.
		page = 1
	if len(course_object) == 0:
		response = requests.get(url=API)
		jsonResponse = json.loads(response.text)
		if jsonResponse:
			courseData = [course['CourseSection'] for course in jsonResponse['Results']] #list comprehension
			for course in courseData:
				course_object = Course(title=course)
				course_object.save()		
	
	data = getCourses(page)
	return render_to_response("form.html",data,context_instance=RequestContext(request))

def getComments(request):
	
	comments_object = Comments.objects.all()
	comment_data=dict()
	for comments in comments_object:
		comment_data[comments.title]=comments.comment
	data={'data':comment_data}
	return render_to_response("comments.html",data,context_instance=RequestContext(request))
	#return HttpResponse

def saveComments(request):
	
	courses=request.POST
	for course in courses:
		if courses[course]:
			#import pdb
			#pdb.set_trace()
			commentObj = Comments(title=Course.objects.get(id=course), comment=courses[course])
			commentObj.save()
	
	return render_to_response("success.html",context_instance=RequestContext(request))
	#return HttpResponseRedirect(reverse('home'))
	
	


