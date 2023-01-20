from django import forms
from .models import *

# 방어 선택 (임의로 구현)
class DefenseForm(forms.Form):
    defense_num = forms.ModelChoiceField(
        queryset = Card.objects.order_by('?')[:10]
    )