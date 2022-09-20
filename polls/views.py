from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question, Vote
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    """Class based view for viewing a poll."""

    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, pk):
        self.question = get_object_or_404(Question, pk=pk)
        voting = self.question.can_vote()
        if not voting:
            messages.error(request, "Cannot Vote in this time")
            HttpResponseRedirect(reverse('polls:index'))
        return super().get(request, pk=pk)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required()
def vote(request, question_id):
    """Vote page for the selected question."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice.",
        })
    else:
        if question.vote_set.filter(user=request.user).exists():
            the_vote = question.vote_set.get(user=request.user)
            the_vote.choice = selected_choice
            the_vote.save()
        else:
            selected_choice.vote_set.create(user=request.user, question=question)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

