from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)
        labels = {
            'username': _('아이디'),
        }

class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            ""
        ),
    )

    class Meta:
        model = get_user_model()
        fields = ('last_name', 'first_name', 'email',)