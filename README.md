# METKA

**METKA** is a console utility for analyzing digital metadata and OSINT (Open Source Intelligence) data. It is designed to extract useful information from various types of files, including images, audio, video, documents, and more. The utility processes metadata in various formats, saves an analysis report, and provides recommendations from artificial intelligence for further forensic investigation.

## Features

- Analyze EXIF data from images (JPEG, TIFF, PNG, etc.)
- Extract metadata from audio and video files
- Process document files (PDF, DOCX, RTF, etc.)
- Extract metadata from presentations (PPTX)
- Analyze XML, HTML, and JSON files
- Automatic report generation and recommendations for further OSINT investigation

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/insojke/METKA.git
    ```

2. Navigate to the project directory:

    ```bash
    cd METKA
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a token.env file and paste the Hugging Face token there (you can get it here: https://huggingface.co/settings/tokens )

## Usage

### Basic Command

To analyze the file, run the following command in your terminal:

```bash
python metka.py
```
==============================================
# METKA

**METKA** - консольная утилита для анализа цифровых метаданных и данных OSINT (Open Source Intelligence). Она предназначена для извлечения полезной информации из различных типов файлов, включая изображения, аудио, видео, документы и многое другое. Утилита обрабатывает метаданные в различных форматах, сохраняет отчёт анализа и предоставляет рекомендации от искусственного интеллекта для дальнейшего криминалистического расследования.

## Возможности

- Анализ данных EXIF из изображений (JPEG, TIFF, PNG и т.д.)
- Извлечение метаданных из аудио- и видеофайлов
- Обработка файлов документов (PDF, DOCX, RTF и т.д.)
- Извлечение метаданных из презентаций (PPTX)
- Анализ XML, HTML и JSON файлов
- Автоматическое формирование отчетов и рекомендаций для дальнейшего OSINT-расследования

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/insojke/METKA.git
    ```

2. Откройте директорию:

    ```bash
    cd METKA
    ```

3. Установите необходимые библиотеки:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл token.env и вставьте туда токен Hugging Face (можно получить здесь: https://huggingface.co/settings/tokens)

## Использование

### Базовая команда

Чтобы проанализировать файл, выполните в своем терминале следующую команду:

```bash
python metka.py
```
