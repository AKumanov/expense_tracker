from django import forms

from expense_tracker.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfile(ProfileForm):
    pass


class EditProfile(ProfileForm):
    pass


class DeleteProfile(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
