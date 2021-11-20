""" Los generics son esas clases genericas, que cada una incorpora funcionalidades directas para las operaciones del crud"""
from rest_framework                     import generics
from appRestaurante.models.user                import UserProfile
from appRestaurante.serializers.userSerializer import UserProfileSerializer

""" RetriveAPIView Obtiene un Objeto y su ID
    Vista concreta para recuperar una instancia de modelo
 """
class UserDetailView(generics.RetrieveAPIView):
    queryset           = UserProfile.objects.all() # Se traen todos los elementos de la tabla
    serializer_class   = UserProfileSerializer     # Se Define la clase que se va a usar para la serializacion en un Atributo heredado
    
