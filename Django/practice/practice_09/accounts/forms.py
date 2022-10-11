from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'last_name', 'first_name', )
        # labels = {
        #     'username': _('사용자 이름'),
        #     'email': _('이메일 주소'),
        # }
    
    # def __init__(self):
    #     super(CustomUserCreationForm, self).__init__()
    #     self.fields['password1'].label = '비밀번호'
    #     self.fields['password2'].label = '비밀번호 확인'
