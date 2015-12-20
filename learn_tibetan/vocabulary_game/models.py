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

class Word(models.Model):
    word = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/",blank=True)
    pronunciation = models.FileField(upload_to="pronunciations/", blank=True)
    is_formal = models.BooleanField (default=False)


class Category(models.Model):
    category = models.ManyToManyField(Word, related_name="word_category",
            blank=True)


class Translation(model.Model):
    LANGUAGE_CODE_CHOICES = (
             ('es', 'Español'),
             ('en', 'English'),
    )

    translation = models.ManyToManyField(Word, related_name="word_translation",
            blank=True)
    #The Language Code ISO 639-1
    language_code = models.CharField(max_length=2,choices=LANGUAGE_CODE_CHOICES,
                                                  default='es')
    definition = models.TextField()

