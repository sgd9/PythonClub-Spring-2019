from django.test import TestCase

# Create your tests here.
def index (request):
    return render(request, 'techapp/index.html')