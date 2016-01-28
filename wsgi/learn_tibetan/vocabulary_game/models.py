#    This Python file uses the following encoding: utf-8 .
#    See http://www.python.org/peps/pep-0263.html for details

#    Its a vocabulary game which allows anyone to learn tibetan.
#
#    Copyright (C) 2015 Tsering Döndrub
#
#    This file is part of Learn Tibetan web apps.
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models

class Category(models.Model):
    LANGUAGE_CODE_CHOICES = (
             ('es', 'Español'),
             ('en', 'English'),
    )

    #The Language Code ISO 639-1
    language_code = models.CharField(max_length=2,choices=LANGUAGE_CODE_CHOICES,
                                                  default='es')
    category = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.category


class Translation(models.Model):
    LANGUAGE_CODE_CHOICES = (
             ('es', 'Español'),
             ('en', 'English'),
    )

    translation = models.CharField(max_length=200, unique=True)
    #The Language Code ISO 639-1
    language_code = models.CharField(max_length=2,choices=LANGUAGE_CODE_CHOICES,
                                                  default='es')
    definition = models.TextField(blank=True)

    def __unicode__(self):
        return self.translation


class Phrase(models.Model):
    phrase = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="images/", blank=True)
    pronunciation = models.FileField(upload_to="pronunciations/", blank=True)
    is_honorific = models.BooleanField (default=False)
    thl_phonetic_transcription = models.CharField(max_length=200,
            help_text="THL Simplified Phonetic Transcription of Standard Tibetan", blank=True)
    thl_wylie_transliteration = models.CharField(max_length=200,
            help_text="THL Extended Wylie Transliteration", blank=True)
    categories = models.ManyToManyField(Category, related_name="phrase_category",
            blank=True)
    translation = models.ManyToManyField(Translation, related_name="pharse_translation",
            blank=True)

    def __unicode__(self):
        return self.phrase


class Word(models.Model):
    word = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="images/",blank=True)
    pronunciation = models.FileField(upload_to="pronunciations/", blank=True)
    is_honorific = models.BooleanField (default=False)
    thl_phonetic_transcription = models.CharField(max_length=200,
            help_text="THL Simplified Phonetic Transcription of Standard Tibetan", blank=True)
    thl_wylie_transliteration = models.CharField(max_length=200,
            help_text="THL Extended Wylie Transliteration", blank=True)
    grammar = models.CharField(max_length=200, blank=True)
    phrase = models.ManyToManyField(Phrase, related_name="word_phrase",
            blank=True)
    categories = models.ManyToManyField(Category, related_name="word_category",
            blank=True)
    translation = models.ManyToManyField(Translation, related_name="word_translation",
            blank=True)

    def __unicode__(self):
        return self.word

