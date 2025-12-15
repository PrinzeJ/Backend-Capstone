from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu, Booking
from .serializer import MenuSerializer, BookingSerializer, UserSerializer

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu':menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_items(request, pk = None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    
    return render(request, 'menu_item.html', {'menu_item': menu_item})

#API views

class MenuListView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = ([permissions.IsAuthenticated])

class BookingListView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes =[permissions.IsAuthenticated]

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({'message':'This view is protected'})

class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Authenticated'})