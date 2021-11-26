from django.contrib import admin
from .models import Post
from embed_video.admin import AdminVideoMixin

class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['Header_first', 'Header_second','Header_third', 'title', 'published_date']

admin.site.register(Post, PostAdmin)

