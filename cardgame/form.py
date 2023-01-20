from django import forms
from .models import *

# 공격 선택 (임의로 구현)
class AttackForm(forms.Form):
    attack_num = forms.ModelChoiceField(
        queryset=Card.objects.order_by('?')[:10])
    defense_user = forms.ModelChoiceField(queryset=User.objects.all())