from django.conf.urls import patterns, include, url



urlpatterns = patterns('taskLeranCircle.views',


	url(r'^$', 'home', name='home'),
        url(r'^database','databaseInsertion',name='databaseInsertion'),

        #url(r'^$', 'mit', name='mit'),
        
    #url(r'^get-code$', 'get_code', name='get_code'),

    #url(r'^upload-resume/$', 'upload', name='upload'),


)
