import translators


def translate(input_, to_lang):
    try:
        output = translators.google(input_, to_language=to_lang)

    except:
        output = "The inserted or selected language is not yet added."

    finally:
        return output