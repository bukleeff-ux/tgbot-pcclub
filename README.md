# 🎮 PC Club Bot

Telegram-бот для компьютерного клуба. Информирует клиентов об акциях, ценах и реферальной программе. Выдаёт промокоды через интерактивную викторину.

## ✨ Функции

- **📈 Акции** — актуальные акции клуба (скидки студентам, бонусы на день рождения и т.д.)
- **💰 Цены** — таблица тарифов по группам клиентов и времени суток
- **🎁 Реферальная программа** — информация о бонусах за приглашение друзей
- **🎁 Промокоды** — викторина с вопросами о клубе, правильные ответы дают промокод на скидку
- **ℹ️ Информация** — адрес, телефон, режим работы

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram_3-2CA5E0?style=flat-square&logo=telegram&logoColor=white)

- **Python 3.11+**
- **aiogram 3** — асинхронный фреймворк для Telegram Bot API
- **python-dotenv** — управление переменными окружения

## 🚀 Быстрый старт

### 1. Клонируй репозиторий

```bash
git clone https://github.com/buklee/tgbot-pcclub.git
cd tgbot-pcclub
```

### 2. Установи зависимости

```bash
pip install -r requirements.txt
```

### 3. Создай `.env` файл

```bash
cp .env.example .env
```

Впиши токен бота (получить у [@BotFather](https://t.me/BotFather)):

```env
BOT_TOKEN=your_bot_token_here
```

### 4. Запусти

```bash
python bot.py
```

## ⚙️ Конфигурация

Все настройки викторины и промокодов задаются прямо в `bot.py`:

| Параметр | Описание |
|---|---|
| `promo_codes` | Список доступных промокодов |
| `questions` | Вопросы для викторины (первый вариант = правильный) |
| Количество вопросов | `random.sample(questions, 5)` — меняй число |
| Порог правильных ответов | `if data["correct"] >= 4` — меняй число |

## 📁 Структура

```
tgbot-pcclub/
├── bot.py            # Основной файл бота
├── used_users.json   # Создаётся автоматически (список использовавших промокод)
├── .env.example      # Шаблон переменных окружения
├── requirements.txt
└── README.md
```

## 📫 Контакты

- **Telegram:** [@buklee](https://t.me/buklee)
- **Email:** bukleeff@gmail.com
