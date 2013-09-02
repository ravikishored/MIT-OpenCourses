from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import models
from django.template import Context, loader, RequestContext
import json,requests
from hello.settings import API
from taskLeranCircle.models import Course, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
	try:
		course_object = Course.objects.all()
		if len(course_object) == 0:
			response = requests.get(url=API)
			jsonResponse = json.loads(response.text)
			if jsonResponse:
				courseData = [course['CourseSection'] for course in jsonResponse['Results']] #list comprehension
				for course in courseData:
					course_object = Course(title=course)
					course_object.save()		
		course_data = dict()
		for course in course_object:
			course_data[course.id]=course.title
		data = {'data': course_data}
		return render_to_response("form.html",data,context_instance=RequestContext(request))
			
	except:
		return HttpResponse ("teseu")

def databaseInsertion(request):
	courses=request.POST
	for course in courses:
		if courses[course]:
			commentObj = Comments(title=Course.objects.get(id=course), comment=courses[course])
			commentObj.save()
	#c = Course(name=cour++se)
        #c = Course(course_name='cse',comment='')
        #c.save()
	return HttpResponse ("got the key")

	
	


