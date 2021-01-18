from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from classroom.models import (Collaboration_connaissances,Collaboration_actuelle,Comment_display,Chaine, Equipe, Quiz, Capteur,  Student, TypeCapteur , Domaine, Subject, User, Profile, Comment)








class Free(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email


# Email Adress

class Subscribe(forms.Form):
    Email = forms.EmailField()
    
    def __str__(self):
        return self.Email









# Subject
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'



#Type_Capteur
class TypeCapteurForm(forms.ModelForm):
    class Meta:
        model = TypeCapteur
        fields = '__all__'


#Domaine

class DomaineForm(forms.ModelForm):
    class Meta:
        model = Domaine
        fields = '__all__'



#StudentSignUpForm

class StudentSignUpForm(UserCreationForm):
    email= forms.EmailField()


    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Vos disciplines scientifiques ',
    )

   

    chaine = forms.ModelMultipleChoiceField(
        queryset=Chaine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='chaînes d’expertises',
 
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        student.chaine.add(*self.cleaned_data.get('chaine'))
        return user









class EventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('user',None)
        #self.user = kwargs.pop('user',None)
        super(EventForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        #self.helper.form_action = reverse_lazy('simpleuser')
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))     

    class Meta:
        model = Quiz
        fields = ['subject', 'domaine', 'titre_projet', 'description_projet', 'type_evt']
        widgets ={
        'subject': forms.CheckboxSelectMultiple,
        }

















class ProjetForm(forms.ModelForm):

    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = 'Disciplines scientifiques necessaires au projet ',
    )

    chaine = forms.ModelMultipleChoiceField(
        queryset=Chaine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = 'Chaine de connaissances ',
    )


    domaine = forms.ModelMultipleChoiceField(
        queryset=Domaine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = 'Domaines d&#146applications du projet ',
    )

    type_evt = forms.ModelMultipleChoiceField(
        queryset=TypeCapteur.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = 'Type des événements à détecter ',
    )

    class Meta:
          model = Quiz
          fields = ['titre_projet', 'description_projet','type_evt', 'domaine', 'chaine',  'subject',  'sensibilite', 'stabilite',  'selectivite', 'resolution',  'precision', 'rapidite', 'justesse','reproductibilite', 'condition_ambiante','temps_de_reponse', 'bande_passante', 'hysteresis',  'cout','poids', 'taille', 'file_1', 'file_2', 'confidentalite', 'finance']
         






class UpdateProjetForm(forms.ModelForm):

    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = 'Disciplines scientifiques necessaires au projet ',
    )

    chaine = forms.ModelMultipleChoiceField(
        queryset=Chaine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = 'Chaine de connaissances ',
    )


    domaine = forms.ModelMultipleChoiceField(
        queryset=Domaine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = 'Domaine d&#146;application du projet ',
    )

    type_evt = forms.ModelMultipleChoiceField(
        queryset=TypeCapteur.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label = 'Type des événements à détecter ',
    )

    class Meta:
          model = Quiz
          fields = ['titre_projet', 'description_projet','type_evt', 'domaine', 'chaine',  'subject',  'sensibilite', 'stabilite',  'selectivite', 'resolution',  'precision', 'rapidite', 'justesse','reproductibilite', 'condition_ambiante','temps_de_reponse', 'bande_passante', 'hysteresis',  'cout','poids', 'taille', 'file_1', 'file_2', 'confidentalite', 'finance']
         






















class CapteurForm(forms.ModelForm):

    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
          model = Capteur
          fields = ['nom_capteur', 'description_projet','subject', 'type_evt', 'domaine', 'technologie_utilisee', 'etendue','sensibilite','resolution','precision', 'rapidite','justesse','reproductibilite', 'temps_de_reponse','bande_passante','hysteresis', 'gamme_temperature','file_1', 'file_2', 'file_3','confidentalite',]
         
      
       












class EquipeForm(forms.ModelForm):

    class Meta:
        model = Equipe
        fields = ['nom_1', 'prenom_1', 'adresse_email_1', 'nom_2','prenom_2']






class actuelle(forms.ModelForm):

    class Meta:
        model = Collaboration_actuelle
        fields = ['description_collaboration',]


class collab(forms.ModelForm):

    class Meta:
        model = Collaboration_connaissances
        fields = []

































class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user



 






class DateInput(forms.DateInput):
    input_type = 'date'







        





class StudentInterestsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('interests', )
        widgets = {
            'interests': forms.CheckboxSelectMultiple
        }

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']



class ProfileUpdateForm(forms.ModelForm):
    
    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
     
    domaine = forms.ModelMultipleChoiceField(
        queryset=Domaine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    chaine = forms.ModelMultipleChoiceField(
        queryset=Chaine.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
     

    class Meta:
          model = Student
          fields =[ 'image', 'nom', 'prenom', 'presentation', 'mots_cles', 'domaine', 'numero_telephone',  'fonction', 'autre_fonction', 'laboratoire', 'autre_labo', 'universite', 'autre_univ', 'link', 'adresse_email','interests', 'chaine']
         
  
class ProfileCUpdateForm(forms.ModelForm):
   


    domaine = forms.ModelMultipleChoiceField(
        queryset=Domaine.objects.all(),
        widget=forms.CheckboxSelectMultiple,

        label = 'Domaines d&#146applications  ',
    )

     

    class Meta:
          model = Student
          fields = fields =[ 'image', 'nom', 'prenom', 'presentation', 'mots_cles', 'domaine', 'numero_telephone',  'fonction', 'autre_fonction', 'laboratoire', 'autre_labo', 'universite', 'autre_univ', 'link', 'adresse_email' ]

class CommentForm(forms.ModelForm):
    class Meta:
        content = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Text goes here!!', 'rows':'4', 'cols':'50'}))
        model = Comment
        fields = ('content',)

class CommentForm_capteurs(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Text goes here!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment_display
        fields = ('content',)