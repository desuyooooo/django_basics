from django.shortcuts import render
from django.views.generic import View

from .models import Note
from .forms import NoteForm

# Create your views here.
class Index(View):
    template_name = 'notes/index.html'

    def get_context_data(self):
        context = {
            'notes': Note.objects.order_by('-id'),
            }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = NoteForm(request.POST)
        context = self.get_context_data()
        if form.is_valid():
            form.save()
        return render(request, self.template_name, context)
