# Изучение немецкого языка
Проект по веб-разработке

## Как использовать

1. Скачать этот репозиторий или клонировать его
2. Перейти в папку репозитория при помощи `cd`
3. `pip install -r requirements.txt`
4. `python manage.py runserver --insecure`

## Версии ПО

Предполагается использование версии 4.1.7 фреймворка Django. Для ее запуска вам понадобится интерпретатор Python версии 3.8, 3.9, 3.10, 3.11 или (рекомендуется) 3.12.

В своем проекте вы можете использовать и более новую версию фреймворка (5.x.x).

## Корректное хранение секретов и токенов

Для загрузки секретов как переменных окружения используется библиотека [python-dotenv](https://pypi.org/project/python-dotenv/).

Все секретные токены должны быть спрятаны в коде за импортом. Для этого создайте в корне репозитория файл `.env` 
и добавьте в него пары «переменная=значение».

Файл `.env` нужно **обязательно** поместить в `.gitignore`!

Затем в `settings.py` загрузите эти переменные при помощи команды `load_dotenv()` и обратитесь к ним через `os.getenv()`:

```python
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv() 

SECRET_KEY = str(os.getenv("SECRET_KEY"))
```


