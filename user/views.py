from rest_framework.viewsets import ModelViewSet
from user.models import AddressGlobal
from .serializers import AddressGlobalSerializer, CustomUser, UserProfile, CustomUserSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

 
class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.prefetch_related('user_profile', 'user_profile__address_info')
    


class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.select_related('user','address_info')
 


class AddressView(APIView):
    serializer_class = AddressGlobalSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        AddressGlobal.objects.create(**serializer.validated_data)
        return Response({
            'success': 'address created'
        })