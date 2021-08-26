from django import forms
from .models import Freebie, Orig_Sharer


# See "Add blog categories - Django blog #12" by Codemy for explanation (around 7min mark)
# Note that only admins can add Category-s. For users, it'll only be a dropdown selector
# sharers = Orig_Sharer.objects.all().values_list('name', 'name')
# sharers_list = []

# for sharer in sharers:
# 	sharers_list.append(sharer)

class FreebieForm(forms.ModelForm):
    title = forms.CharField(max_length=100)		# i think this can be removed since the same field is in the model?
    
    class Meta:
    	model = Freebie
    	fields = ['title', 'content', 'orig_sharer']
    	widgets = {
    		# 'tag'
    		# 'orig_sharer' : forms.Select(choices=sharers, attrs={'class': 'form-control'},)
    	}