from django.contrib import admin
from .models import Post,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('id','name')



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','author','read_time')
