from django.contrib import admin
from .models import Post,Category
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header='CodeWithKisan'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('id','name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','author','read_time')
