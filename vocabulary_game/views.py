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

from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import Word, Phrase, Category, Translation

class WordCreate(generic.edit.CreateView):
    model = Word
    fields = '__all__'
    template_name_suffix = '_create_form'
    #success_url = reverse_lazy('lotteryuser-list')


#class WordUpdate(generic.edit.UpdateView):
#    model = Word
#    fields = ['name', 'number', 'prize']
#    template_name_suffix = '_update_form'
#    #success_url = reverse_lazy('lotteryuser-list')


#class WordDelete(generic.edit.DeleteView):
#    model = Word
#    #success_url = reverse_lazy('lotteryuser-list')
