from tastypie.resources import ModelResource
from books.models import Book


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        always_return_data = True
