#    This Python file uses the following encoding: utf-8 .
#    See http://www.python.org/peps/pep-0263.html for details

#    Its a views of vocabulary games and translator which allows anyone to 
#    learn tibetan.
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

from django.shortcuts import render
from random import shuffle

from core.models import Word

NUM_OPTIONS = 4


def generate_options(list_options, num_options):
    """
    Return a right option and a list of shuffle options
    """
    shuffle(list_options)
    right_option = list_options[0]
    options = list_options[0:num_options]
    return right_option, options

def vocabulary_game(request):
    """
    View to the vocabulary game
    """
    list_words = list(Word.objects.all())
    right_answer, answers = generate_options(list_words, NUM_OPTIONS)
    shuffle(answers)
    score = 0
    if request.method == 'POST':
        score = int(request.POST.get('score'))
        #TODO print score
        context = {
            'right_answer': right_answer,
            'answers': answers,
            'score':score
        }
        return render(request, 'vocabulary_game/index.html', context)
    context = {
        'right_answer': right_answer,
        'answers': answers,
        'score':score
    }
    return render(request, 'vocabulary_game/index.html', context)

def translator(request):
    """
    Get word translation
    """
    translate = []
    if request.method == 'POST':
        if (request.POST.get('tibetan') == 'true'):
            word = request.POST.get('origin')
            if Word.objects.filter(translation__translation=word).exists():
                translate = Word.objects.filter(translation__translation=word)
        elif(request.POST.get('spanish') == 'true'):
            word = request.POST.get('origin')
            if Word.objects.filter(word=word).exists():
                translate = Word.objects.get(word=word).translation.all()
        context = {
            'origin': word,
            'result': translate
        }
        return render(request, 'translator/index.html', context)
    return render(request, 'translator/index.html')
