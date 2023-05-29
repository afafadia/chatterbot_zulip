from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return True

    def process(self, input_statement, additional_response_selection_parameters):
        import requests
        from chatterbot.conversation import Statement

        # Make a request to the Air Quality API
        response = requests.get(
            # "https://docs.patentaware.com/api/documents/?collection=Documents&q=intel&page=1&format=json",
            "http://50.211.199.147:8000/api/documents/?collection=Documents&q=intel&page=1&format=json"
        )
        data = response.json()
        # print(data)

        # Let's base the confidence value on if the request was successful
        # if response.status_code == 200:
        #     confidence = 1
        # else:
        #     confidence = 0

        # latitude = data.get("latitude", "unavailable")

        response_statement = Statement(text=f"The current latitude is {data}")
        return response_statement
