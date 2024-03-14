
from django.http import JsonResponse


def handle_not_found(request, exception):
    return JsonResponse({'error': 'Not Found'}, status=404)