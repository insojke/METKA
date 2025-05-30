import requests
import re
from dotenv import load_dotenv
import os


load_dotenv("token.env")
HF_TOKEN = os.getenv("HF_TOKEN")


API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
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
            "Information for analysis:\n"
            f"{metadata_text}\n"
            "Now listen carefully:\n"
            "You are an expert in digital metadata analysis and OSINT investigations.\n"
            "Your task is to analyze the provided metadata and give a recommendation for further investigation.\n"
            "- If key details like author's name, software, date, GPS coordinates, device model, or comments are present, highlight them in your recommendation.\n"
            "- If some information is missing, suggest potential next steps based on available clues in the metadata.\n"
            "- If important information is missing or masked, give advice on how to try and extract or infer it.\n"
            "- Provide a clear and actionable recommendation for continuing the OSINT investigation.\n"
            "- Format your answer as follows:\n\n"
            "Recommendation: <your detailed advice here>\n\n"
        )

        answer = query_huggingface(prompt)

        print("="*50)
        print(answer)
        print("="*50)

    except Exception as e:
        print(f"Error | Ошибка: {e}")
