from django.contrib import admin
from blog.models import Tag, Post

admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
# Register your models here.
admin.site.register(Post, PostAdmin)