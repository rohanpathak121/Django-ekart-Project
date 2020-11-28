from django import forms
from django.forms import ValidationError
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import ReadOnlyPasswordHashField


attrs_dict={'class':'form-control'}

class LoginForm(forms.Form):
    email=forms.EmailField(label="Email:-",
    widget=forms.EmailInput(attrs=attrs_dict))


    pwd=forms.CharField(label="Password:-",
    widget=forms.PasswordInput(attrs=attrs_dict))

class RegistrationForm(forms.Form):

    email=forms.EmailField(label="Email:-",
    widget=forms.EmailInput(attrs=attrs_dict))

    fullname=forms.CharField(label="Full Name:-",
    widget=forms.TextInput(attrs=attrs_dict))


    mobile=forms.IntegerField(label="Mobile No:-",
    widget=forms.NumberInput(attrs=attrs_dict))


    pwd=forms.CharField(label="Password:-",
    widget=forms.PasswordInput(attrs=attrs_dict))


    cpwd=forms.CharField(label="Confirm Password:-",
    widget=forms.PasswordInput(attrs=attrs_dict))


    
    def clean(self):
        form_data=self.cleaned_data  
        #clean_data will not copadible for special symbol  data will use in user bank details like sensitive data
        if form_data.get('pwd') == form_data.get('cpwd'):
            return form_data

        else:
            raise ValidationError("Password doesn't match with Confirm Password")


    def clean_username(self):
        un=self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=un).exists():
            raise ValidationError("Username already in use......")

        return un        


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label = "Password", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput)


    class Meta:
        model = User
        fields = ('email', 'full_name', 'mobile')

    def clean(self):
        form_data=self.cleaned_data  
        #clean_data will not copadible for special symbol  data will use in user bank details like sensitive data
        if form_data.get('password1') == form_data.get('password2'):
            return form_data

        else:
            raise ValidationError("Password doesn't match with Confirm Password")

    def save(self, commit = True):
        user = super(UserAdminCreationForm, self).save(commit = False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin', 'full_name', 'mobile', 'staff')

    def clean_password(self):
        return self.initial["password"]

        