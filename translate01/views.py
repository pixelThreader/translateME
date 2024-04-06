from django.shortcuts import render, HttpResponse
from googletrans import Translator, LANGUAGES
from django.http import JsonResponse


# Initilizing the translator
translator = Translator()


# Create your views here.


def home(requests):
    # Get a dictionary of all possible languages and their codes
    all_languages = LANGUAGES

    # Print the list of languages and their codes
    langs = []
    for code, language in all_languages.items():
        langs.append({'code': code, 'language': language})

    context = {'langs': langs}  # Pass the 'langs' list in the context
    return render(requests, 'index.html', context)


def translate(request):
    if request.method == "POST":
        lang = request.POST.get("languageTarget")
        targetLang = request.POST.get("targetText")
        result = translator.translate(targetLang, src="en", dest=lang)
    else:
        HttpResponse("Forbidden")

    return JsonResponse({"translatedText": result.text})
