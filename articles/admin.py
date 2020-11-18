from django.contrib import admin
from .models import Article, Comment

class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines=[
        CommentInLine
    ]

admin.site.register(Article)
admin.site.register(Comment)
