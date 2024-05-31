from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Home",
            "subtitle": "Vista inicial - Taller 01 - TEIS",

        })
        return context


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us ",
            "subtitle": "About Taller 01 - TEIS",
            "description": "This is an about page ...",
            "author": "Developed by: Santiago Gallego",
        })

        return context
