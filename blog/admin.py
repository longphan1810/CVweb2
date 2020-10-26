from django.contrib import admin

# Register your models here.
from .models import topic, article, Comment

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]

admin.site.register(topic)
admin.site.register(article, PostAdmin)

