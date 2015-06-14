from django.conf.urls import patterns, include, url
from django.contrib import admin


from tastypie.api import Api
import books.api

api = Api(api_name='v1')
api.register(books.api.BookResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'books.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),    
)
