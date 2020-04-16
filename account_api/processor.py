from datetime import date


def current_year(request):
    return {"current_year": date.today().year}
