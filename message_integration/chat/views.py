from django.conf import settings
from django.http import JsonResponse
from twilio.rest import Client
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def broadcast_sms(request):

    if request.method == 'POST':
        data = request.data

        custom_message = data.get('storeGrade')
        size = request.query_params.get('size', 20)  # Default size if not provided

        # Ensure size is an integer
        try:
            size = int(size)
        except ValueError:
            return Response({"error": "Invalid size parameter. It must be an integer."}, status=400)

        # Create the verification message
        message_to_broadcast = f"{custom_message}"

        # Create the Twilio client
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Send the message to each recipient
        for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
            if recipient:
                client.messages.create(
                    to=recipient,
                    from_=settings.TWILIO_NUMBER,
                    body=message_to_broadcast
                )

        return JsonResponse({"message": f"Messages sent successfully!"}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
