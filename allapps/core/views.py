import json

from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


# Create your views here.
def index(request):
    return render(request, "core/index.html", {})


# Check this with Postman - POST Data
@method_decorator(csrf_exempt, name="dispatch")
class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        The JSON data should contain a 'text' attribute.
        """

        input_data = json.loads(request.body.decode("utf-8"))
        if "text" not in input_data:
            return JsonResponse(
                {
                    "text": ['The attribute "text" is required.'],
                },
                status=400,
            )

        response = self.chatterbot.get_response(input_data)
        response_data = response.serialize()

        return JsonResponse(
            {
                "response_text": response_data["text"],
            },
            status=200,
            safe=False,
        )

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        # print(self.chatterbot.__dict__)
        return JsonResponse({"name": self.chatterbot.name})
