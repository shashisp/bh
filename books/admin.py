from django.contrib import admin
import books.models as models


admin.site.register(models.Book)
admin.site.register(models.Vote)
admin.site.register(models.UserProfile)
admin.site.register(models.Collection)
