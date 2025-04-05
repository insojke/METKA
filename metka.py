from scripts.metadata_analyzer import analyze_metadata, create_report_file
from scripts.AI_recommendation import get_recommendation
from dotenv import load_dotenv
import os


def draw_metka():
    metka_art = """
    ╔══════════════════════════════════════════════════════════════╗
    ║  ██      ██  ██████████  ██████████  ██      ██    ██████    ║
    ║  ████  ████  ██              ██      ██    ██    ██      ██  ║
    ║  ██  ██  ██  ████████        ██      ██████      ██      ██  ║
    ║  ██      ██  ██              ██      ██    ██    ██████████  ║
    ║  ██      ██  ██████████      ██      ██      ██  ██      ██  ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(metka_art)


def main():
    while True:
        draw_metka()
        print("Select an action | Выберите действие:")
        print("[1] Analyze the file | Анализировать файл")
        print("[2] Exit | Выйти")
        choice = input("\nEnter the action number | Введите номер действия: ").strip()

        if choice == "1":
            report_file_name = input("\nEnter a name for the report file | Введите название для файла отчёта: ").strip()
            if not report_file_name.lower().endswith(".txt"):
                report_file_name += ".txt"
            create_report_file(report_file_name)

            file_path = input(
                "\nEnter the path to the file without quotation marks | Введите путь к файлу без кавычек: ").strip()
            analyze_metadata(file_path)
            get_recommendation(f"C:/METKA_Reports/{report_file_name}")

            input("\nPress Enter to return to the menu... | Нажмите Enter, чтобы вернуться в меню...")

        elif choice == "2":
            print("Exit the program... | Выход из программы...")
            break
        else:
            print("Wrong choice. Please enter 1 or 2 | Неверный выбор. Пожалуйста, введите 1 или 2.")
            input("\nPress Enter to try again... | Нажмите Enter, чтобы попробовать снова...")

if __name__ == "__main__":
    main()
