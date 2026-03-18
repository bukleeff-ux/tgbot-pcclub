# 🎮 PC Club Bot

A Telegram bot for a computer club. Informs clients about promotions, pricing, and the referral program. Rewards engaged users with promo codes through an interactive quiz.

## ✨ Features

- **📈 Promotions** — current club deals (student discounts, birthday bonuses, etc.)
- **💰 Pricing** — rate table by client group and time of day
- **🎁 Referral Program** — info on bonuses for inviting friends
- **🎁 Promo Codes** — a quiz about the club; correct answers unlock a discount code
- **ℹ️ Info** — address, phone number, and opening hours

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram_3-2CA5E0?style=flat-square&logo=telegram&logoColor=white)

- **Python 3.11+**
- **aiogram 3** — async Telegram Bot API framework
- **python-dotenv** — environment variable management

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/buklee/tgbot-pcclub.git
cd tgbot-pcclub
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```bash
cp .env.example .env
```

Fill in your bot token (get it from [@BotFather](https://t.me/BotFather)):

```env
BOT_TOKEN=your_bot_token_here
```

### 4. Run

```bash
python bot.py
```

## ⚙️ Configuration

All quiz and promo code settings are configured directly in `bot.py`:

| Parameter | Description |
|---|---|
| `promo_codes` | List of available promo codes |
| `questions` | Quiz questions (first option = correct answer) |
| Number of questions | `random.sample(questions, 5)` — change the number |
| Correct answers threshold | `if data["correct"] >= 4` — change the number |

## 📁 Structure

```
tgbot-pcclub/
├── bot.py            # Main bot file
├── .env.example      # Environment variable template
├── requirements.txt
└── README.md
```

## 📫 Contact

- **Telegram:** [@buklee](https://t.me/buklee)
- **Email:** bukleeff@gmail.com
