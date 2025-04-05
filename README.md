# METKA

**METKA** is a console utility for analyzing digital metadata and OSINT (Open Source Intelligence) data. It is designed to extract useful information from various types of files, including images, audio, video, documents, and more. The utility processes metadata in various formats, saves an analysis report, and provides recommendations from artificial intelligence for further forensic investigation.

## Features

- Analyze EXIF data from images (JPEG, TIFF, PNG, etc.)
- Extract metadata from audio and video files
- Process document files (PDF, DOCX, RTF, etc.)
- Extract metadata from presentations (PPTX)
- Analyze XML, HTML, and JSON files
- Automatic report generation and recommendations for further OSINT investigation

## Installation for Linux Terminal

1. Install or update Python and pip3:

    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/insojke/METKA.git
    ```

3. Navigate to the project directory:

    ```bash
    cd METKA
    ```

4. Get an API token for Hugging Face (you can get it here: https://huggingface.co/settings/tokens)

5. Create a token.env file:

    ```bash
    nano token.env
    ```

6. In the editor that opens, enter your token as follows:

     ```bash
    HF_TOKEN=YOUR_TOKEN_IS_HERE
    ```

7. Press "Ctrl+O", then "Enter", then "Ctrl+X" to save the changes in the file.

8. Create a virtual environment and activate it:
    ```bash
    sudo apt install python3-venv -y
    python3 -m venv venv
    source venv/bin/activate
    ```
    
9. Install the required dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

10. Run the utility:

    ```bash
    python3 metka.py
    ```

## Installation for Windows PowerShell

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

4. Get an API token for Hugging Face (you can get it here: https://huggingface.co/settings/tokens)

5. Create a token.env file:

    ```bash
    New-Item -Path . -Name "token.env" -ItemType "file"
    ```

6. Open the token.env file in a text editor:

   ```bash
    notepad token.env
    ```

7. In the editor that opens, enter your token as follows and save:

   ```bash
   HF_TOKEN=YOUR_TOKEN_IS_HERE
   ```

8. Run the utility:

    ```bash
    python metka.py
    ```

## Usage

### Basic Command

To analyze the file, run the following command in your terminal:

```bash
python metka.py
```
========================================================================
# METKA

**METKA** - консольная утилита для анализа цифровых метаданных и данных OSINT (Open Source Intelligence). Она предназначена для извлечения полезной информации из различных типов файлов, включая изображения, аудио, видео, документы и многое другое. Утилита обрабатывает метаданные в различных форматах, сохраняет отчёт анализа и предоставляет рекомендации от искусственного интеллекта для дальнейшего криминалистического расследования.

## Возможности

- Анализ данных EXIF из изображений (JPEG, TIFF, PNG и т.д.)
- Извлечение метаданных из аудио- и видеофайлов
- Обработка файлов документов (PDF, DOCX, RTF и т.д.)
- Извлечение метаданных из презентаций (PPTX)
- Анализ XML, HTML и JSON файлов
- Автоматическое формирование отчетов и рекомендаций для дальнейшего OSINT-расследования

## Установка для терминала Linux

1. Установите или обновите Python и pip3:

    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/insojke/METKA.git
    ```

3. Перейдите в каталог проекта:

    ```bash
    cd METKA
    ```

4. Получите API-токен для Hugging Face (Вы можете получить его здесь: https://huggingface.co/settings/tokens)

5. Создайте файл token.env:

    ```bash
    nano token.env
    ```

6. В открывшемся редакторе введите Ваш токен следующим образом:

    ```bash
    HF_TOKEN=YOUR_TOKEN_IS_HERE
    ```

7. Нажмите "Ctrl+O", затем "Enter", затем "Ctrl+X", чтобы сохранить изменения в файле.

8. Создайте виртуальную среду и активируйте её:

    ```bash
    sudo apt install python3-venv -y
    python3 -m venv venv
    source venv/bin/activate
    ```

9. Установите необходимые зависимости:

    ```bash
    pip3 install -r requirements.txt
    ```

10. Запустите утилиту:

    ```bash
    python3 metka.py
    ```

## Установка для Windows PowerShell

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/insojke/METKA.git
    ```

2. Перейдите в каталог проекта:

    ```bash
    cd METKA
    ```
    
3. Установите необходимые зависимости:
   
    ```bash
    pip install -r requirements.txt
    ```

4. Получите API-токен для Hugging Face (Вы можете получить его здесь: https://huggingface.co/settings/tokens)

5. Создайте файл token.env:

    ```bash
    New-Item -Path . -Name "token.env" -ItemType "file"
    ```

6. Откройте файл token.env в текстовом редакторе:

   ```bash
    notepad token.env
    ```

7. В открывшемся редакторе введите Ваш токен следующим образом и сохраните::

   ```bash
   HF_TOKEN=YOUR_TOKEN_IS_HERE
   ```

8. Запустите утилиту:

    ```bash
    python metka.py
    ```

## Использование

### Базовая команда

Чтобы проанализировать файл, выполните в своем терминале следующую команду:

```bash
python metka.py
```
