from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Users


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    queryset = Users.objects.all()
    lookup_field = 'id'

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.save()
        return Response({"token": Token.objects.create(user=user).key}, status=201)

    def get(self, request):
        return Response(Users.objects.values('first_name', 'last_name', 'email', 'username', 'company_id'))


class UserDetailView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    queryset = Users.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        return Response(Users.objects.filter(id=id).values('first_name', 'last_name', 'email', 'username', 'company'))

    def patch(self, request, id):
        user = Users.objects.get(id=id)
        serializer = UserSerializer(
            user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(Users.objects.filter(id=id).values('first_name', 'last_name', 'email', 'username', 'company'))
