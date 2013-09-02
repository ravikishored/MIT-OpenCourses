from django.db import models
from django.contrib import admin

class Course(models.Model):
    title = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.title

class Comments(models.Model):
    title = models.ForeignKey('Course')
    comment = models.CharField(max_length=160)
    
    def __unicode__(self):
        return "Title: {} --- Comment: {}".format(self.title,self.comment)


admin.site.register(Course)
admin.site.register(Comments)
