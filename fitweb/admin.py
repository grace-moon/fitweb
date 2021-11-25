from django.contrib import admin
from .models import Post, Image
from embed_video.admin import AdminVideoMixin

class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['Header_first', 'Header_second','Header_third', 'title']

admin.site.register(Post, PostAdmin)
admin.site.register(Image)
