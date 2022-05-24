from email.policy import default
from django import forms


class RollForm(forms.Form):
    skill = forms.BooleanField(
        label="Avez-vous la compétence ?",
        required=False,
    )
    domain = forms.BooleanField(
        label="Avez-vous le domaine ?",
        required=False,
    )
    mastery = forms.BooleanField(
        label="Avez-vous la maîtrise sur l'action, la compétence ou le domaine concerné ?",
        required=False,
    )

    equipment = forms.BooleanField(
        label="Avez-vous un équipement supérieur qui s'applique ?",
        required=False,
    )

    difficulty = forms.IntegerField(
        label="Quelle est la difficulté, de 0 à 2 ?",
        initial=0,
        min_value=0,
        max_value=2,
        required=True,
    )
