from googletrans import Translator, LANGUAGES

translator = Translator()

text_to_translate = "Hello how are you?"
target_language = "hi"

translated_text = translator.translate(text_to_translate, dest=target_language)

print("Original text:", translated_text.origin)
print("Translated text:", translated_text.text)
print("Source language:", translated_text.src)
print("Target language:", translated_text.dest)
print("Pronunciation:", translated_text.pronunciation)
# print("Extra data:", translated_text.extra_data)

# # Get a dictionary of all possible languages and their codes
# all_languages = LANGUAGES

# # Print the list of languages and their codes
# for code, language in all_languages.items():
#     print(f"{code}: {language}")

# Get a dictionary of all possible languages and their codes
all_languages = LANGUAGES

# # Create a list of dictionaries with code and language
# langs = []
# for code, language in all_languages.items():
#     langs.append({'code': code, 'language': language})

# # Print the list of languages and their codes
# for lang in langs:
#     print(f"Code: {lang['code']}, Language: {lang['language']}")



# text_to_detect = text_to_translate  # Replace this with your text

# # Detect the language of the text
# detected_language = translator.detect(text_to_detect)

# # Print the detected language code and confidence
# print("Detected language:", detected_language.lang)
# print("Confidence:", detected_language.confidence)