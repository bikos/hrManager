from django.contrib import admin

from hrTransaction.models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date', 'question_text']
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)




admin.site.register(Choice)
