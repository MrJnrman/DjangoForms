from django import forms

from . import models

'''
    models forms created using an existing model and specifying what fields to used to generate the formc
'''
class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions',
        ]

class QuestionForm(forms.ModelForm):
    class Media:
        # css is a dictionary
        css ={'all': ('courses/css/order.css',)}  # ',' because this is a tuple
        js = (
            'courses/js/vendor/jquery.fn.sortable.min.js',
            'courses/js/order.js'
        )

class TrueFalseQuestionForm(QuestionForm):
    class Meta:
        model = models.TrueFalseQuestion
        fields = [
            'order',
            'prompt',
        ]


class MultipleChoiceQuestionForm(QuestionForm):
    class Meta:
        model = models.MultipleChoiceQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers',
        ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'order',
            'text',
            'correct',
        ]

AnswerFormSet = forms.modelformset_factory(
    models.Answer,
    form=AnswerForm,
    extra=2,

)

AnswerInlineFormSet = forms.inlineformset_factory(
    models.Question,  # model that we will be saving with/parent model
    models.Answer,  # model being edited in form/ which model the factory is for
    formset=AnswerFormSet,
    fields=('order', 'text', 'correct'),
    extra=2,
    min_num=1,
)