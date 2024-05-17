from django.contrib import admin
from .models import Question,Choice

# Register your models here.

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster Admin Area"

class Choice_Inline(admin.TabularInline):
    model = Choice
    extra = 3
class Question_Admin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [Choice_Inline]

admin.site.register(Question,Question_Admin)
