import requests
import re
from dotenv import load_dotenv
import os


load_dotenv("token.env")
HF_TOKEN = os.getenv("HF_TOKEN")


API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}


def query_huggingface(prompt: str) -> str:
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        print(f"[!] Ошибка запроса: {response.status_code}")
        print(response.text)
        return "Не удалось получить ответ от модели."

    result = response.json()

    raw_text = result[0]["generated_text"] if isinstance(result, list) else result.get("generated_text", "")

    return clean_response(raw_text)


def clean_response(text: str) -> str:
    matches = list(re.finditer(r"Recommendation:", text, re.IGNORECASE))

    if len(matches) >= 2:
        second_match_start = matches[1].start()
        recommendation = text[second_match_start:].strip()
    else:
        recommendation = text[matches[0].start():].strip() if matches else text.strip()

    return recommendation


def get_recommendation(file_path: str):
    """Читает метаданные из файла, отправляет в ИИ и выводит чистую рекомендацию."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            metadata_text = f.read()

        prompt = (
            "Information for analyze:"
            f"{metadata_text}"
            "Now listen prompt:"
            "You are an expert in digital metadata analysis and OSINT investigations.\n"
            "You will receive a metadata report from a digital file (image, document, media, etc).\n"
            "Your task is to:\n"
            "- Extract the following key elements: author's name, editing software, capture date, GPS coordinates, device model, user comments, and company (if present).\n"
            "- If these elements are present, highlight them in your recommendation.\n"
            "- If some of them are missing, examine the remaining metadata and try to infer or guess what might be important.\n"
            "- Based on your analysis, give a clear and useful recommendation for further OSINT investigation.\n"
            "- Format your answer like this:\n\n"
            "Recommendation: <your detailed advice here>\n\n"
        )

        answer = query_huggingface(prompt)

        print("="*50)
        print(answer)
        print("="*50)

    except Exception as e:
        print(f"Error | Ошибка: {e}")
