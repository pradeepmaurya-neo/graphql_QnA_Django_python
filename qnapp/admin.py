from django.contrib import admin
from . import models


@admin.register(models.Category)

class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        
    ]

@admin.register(models.Question)
class 