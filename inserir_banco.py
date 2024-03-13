from galeria.models import Fotografia

foto = Fotografia(nome="Pilares da criação", legenda="nasa.org / NASA / James Webb", foto="pilares-da-criacao.webp") 
foto.save()

Fotografia.objects.all()