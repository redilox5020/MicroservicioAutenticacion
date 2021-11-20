from rest_framework                               import serializers
from appRestaurante.models.address                import Address
from appRestaurante.models.user                   import UserProfile      # Traemos el modelo de Usuario
from appRestaurante.serializers.addressSerializer import AddressSerializer  # Tambien Cuentas 



class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializa objeto de perfil de usuario """
    address = AddressSerializer()
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'nickname' ,'fullname', 'password', 'address')

        ''' Se hace un excepcion con el campo de password ya que no se quiere ver el hash del password '''
        extra_kwargs = {
            'password': {
                # cuando ocurre password, se añaden permisos adicionales
                'write_only': True, # con esto impedimos que el password sea visible cuando se recupera el objeto, solo es visible cuando se esta creando
                'style': {'input_type': 'password'}# para estilizar la clave, no se muestra la info, a cambio se muestran *
            }
        }

    def create(self, validated_data):
        """ Crea y retornar nuevo usuario """
        
        addressData  = validated_data.pop('address')
        addressInstance = Address.objects.create(**addressData)
        userInstance = UserProfile.objects.create(address=addressInstance ,**validated_data)
        userInstance.set_password(validated_data["password"])
        userInstance.save()

        return userInstance


    def update(self, instance, validated_data):
        """ Actualiza cuenta de usuario """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)

