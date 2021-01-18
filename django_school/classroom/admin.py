from django.contrib import admin
from .models import Profile, Subject,  Student, Fonction, Equipe,Chaine, Quiz,  ExpertListe, Comment, Question, Answer, Domaine, TypeCapteur



# Register your models here.

admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Equipe)
admin.site.register(Quiz)
admin.site.register(ExpertListe)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Domaine)
admin.site.register(TypeCapteur)
admin.site.register(Chaine)
admin.site.register(Fonction)