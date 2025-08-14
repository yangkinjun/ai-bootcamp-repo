from langdetect import detect
from langchain_openai import ChatOpenAI


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

    try:
        return resp.content
    except Exception:
        return str(resp)
