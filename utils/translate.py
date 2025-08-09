from langdetect import detect
from langchain_openai import ChatOpenAI


# # ====== Language Detection ======
# def detect_language(text: str) -> str:
#     translator = GoogleTranslator(source="auto", target="en")
#     detected_lang = translator.detect(text)
#     return detected_lang[0]  # returns language code like 'en', 'zh', etc.


# # ====== Translation ======
# def translate_to_english(text: str) -> str:
#     translator = GoogleTranslator(source="auto", target="en")
#     return translator.translate(text)


# def translate_from_english(text: str, target_lang: str) -> str:
#     translator = GoogleTranslator(source="en", target=target_lang)
#     return translator.translate(text)


# lightweight language detection
def detect_language(text: str) -> str:
    try:
        return detect(text)
    except Exception:
        return "en"


# translate text using llm
def translate_text(text: str, target_lang: str = "en") -> str:
    """
    Translate text into target_lang (ISO code, e.g., 'en','zh','ms','ta','tl').
    Uses the ChatOpenAI model; tune prompt if you want formal/informal style.
    """
    system = f"You are a translator. Translate the user's text to {target_lang}. Keep meaning exact and preserve named entities."
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = f"{text}\n\nTranslate to {target_lang}:"

    resp = llm.invoke(prompt)
    # If response object differs, get the text accordingly:
    # e.g., resp.content or resp['content'] depending on the lib you use
    try:
        return resp.content
    except Exception:
        return str(resp)
