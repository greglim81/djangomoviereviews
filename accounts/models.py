from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class UserCreateForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None