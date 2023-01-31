from django.views.generic import TemplateView


# def greetings(request: WSGIRequest, name: str = 'Bob', age: int = 42):
#     return render(
#         request=request,
#         template_name='first_example/greetings.html',
#         context={
#             "name": name,
#             "age": age,
#         },
#     )


class GreetingsView(TemplateView):
    template_name = "first_example/greetings.html"

    def get_context_data(self, name: str = "Alex", age: int = 42, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)

        context_data["name"] = name
        context_data["age"] = age

        context_data["title"] = "Greetings"

        return context_data
