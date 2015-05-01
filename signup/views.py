from django.shortcuts import render
from django.views import generic

from signup.models import User, Cadet


class IndexView(generic.ListView):
    template_name = 'signup/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Cadet.objects
