from django.contrib import admin
from app.models import *
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Book)
admin.site.register(Music)
admin.site.register(Movie)
admin.site.register(CollectionBook)
admin.site.register(CollectionMovie)
admin.site.register(CollectionMusic)
admin.site.register(Token)
