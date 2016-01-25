from django.contrib import admin

from .models import Word, Phrase, Category, Translation

admin.site.register(Word)
admin.site.register(Phrase)
admin.site.register(Category)
admin.site.register(Translation)
