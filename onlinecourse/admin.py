from django.contrib import admin
from .models import Course, Instructor, Lesson, Question, Choice

# Register your models here.

class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5

class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text']

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    fields = ['lesson', 'question_text']
    inlines = [ChoiceInline]



admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)