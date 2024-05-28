from django.forms import ModelForm, ModelChoiceField
from .models import Like
from django.contrib.auth.models import User

class LikeForm(ModelForm):
    user = ModelChoiceField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Like
        fields = ['user', 'form_data_id']