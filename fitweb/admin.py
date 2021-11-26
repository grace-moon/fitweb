from django.contrib import admin
from .models import Post
from embed_video.admin import AdminVideoMixin

class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['Header_first', 'objects_num', 'Header_second','Header_third', 'title', ]

admin.site.register(Post, PostAdmin)

