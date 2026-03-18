import asyncio
import random
import json
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.filters import Command

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN", "")

bot = Bot(token=TOKEN)
dp = Dispatcher()

USED_FILE = "used_users.json"
used_users = set()
if os.path.exists(USED_FILE):
    try:
        with open(USED_FILE, "r", encoding="utf-8") as f:
            data = f.read().strip()
            if data:
                used_users = set(json.loads(data))
    except:
        used_users = set()


def save_used_users():
    with open(USED_FILE, "w", encoding="utf-8") as f:
        json.dump(list(used_users), f)


promo_codes = ["2", "6", "8", "10", "12", "14"]
user_data = {}
# Вопросы для промокодов. Правильный ответ всегда пишем первым. Формат: {"question": "Текст вопроса", "options": ["правильный вариант", "вариант 2", "вариант 3", "вариант 4"]}
questions = [
    {"question": "Сколько часов дарим студентам?", "options": ["3 часа", "1 час", "5 часов", "2 часа"]},
    {"question": "Сколько часов дарим за покупку от 1700₽?", "options": ["3 часа", "5 часов", "1 час", "7 часов"]},
    {"question": "Сколько часов дарим на день рождения?", "options": ["7 часов", "3 часа", "5 часов", "10 часов"]},
    {"question": "Сколько процентов возвращаем баллами?", "options": ["2-3%", "5%", "10%", "1%"]},
    {"question": "Работаем ли мы круглосуточно?", "options": ["Да", "Нет", "Иногда", "Нет выходных"]},
    {"question": "Какой статус получает новый пользователь?", "options": ["New Member", "Member", "Old Member", "VIP"]},
    {"question": "Сколько нужно правильных ответов для промокода?", "options": ["4", "5", "3", "2"]}
]

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📈 Акции")],
        [KeyboardButton(text="💰 Цены")],
        [KeyboardButton(text="🎁 Реферальная программа")],
        [KeyboardButton(text="🎁 Промокоды")],
        [KeyboardButton(text="ℹ️ Информация")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Добро пожаловать! Выберите раздел:", reply_markup=keyboard)

@dp.message(lambda m: m.text == "📈 Акции")
async def stocks(message: types.Message):
    await message.answer(
        "🔥 Текущие акции:\n\n"
        "🎓 Студентам — 3 часа бесплатно\n*при предъявлении студенческого билета*\n\n"
        "🎁 3 часа за покупку от 1700₽\n\n"
        "🎂 7 часов на день рождения\n\n"
        "💰 Возвращаем 2–3% баллами"
    )

@dp.message(lambda m: m.text == "💰 Цены")
async def prices(message: types.Message):
    table = """
Группа клиентов | 08-14 | 14-00 | 00-08
----------------------------------------
New Member      | Comfort 140 | Comfort 140 | Comfort 140
                | Cash 160    | Cash 160    | Cash 160
----------------------------------------
Member          | Comfort 140 | Comfort 140 | Comfort 140
                | Cash 160    | Cash 160    | Cash 160
----------------------------------------
Old Member      | Comfort 140 | Comfort 140 | Comfort 140
                | Cash 160    | Cash 160    | Cash 160
"""
    await message.answer(f"<pre>{table}</pre>", parse_mode="HTML")

@dp.message(lambda m: m.text == "🎁 Реферальная программа")
async def referal(message: types.Message):
    await message.answer("Приглашай друзей и получай 10% от их покупок!")

@dp.message(lambda m: m.text == "ℹ️ Информация")
async def info(message: types.Message):
    await message.answer("🕒 Работаем круглосуточно\n📍 Адрес: Северная 3/1\n📞 +7(928)842-78-94")

# ==================================================
# Начало викторины
# ==================================================
@dp.message(lambda m: m.text == "🎁 Промокоды")
async def start_quiz(message: types.Message):
    user_id = message.from_user.id
    if user_id in used_users:
        await message.answer("❌ Вы уже получали промокод.")
        return
# Меняем тут цифру для количества вопросов, не ставить больше чем элементов в списке questions
    selected = random.sample(questions, 5)
    user_data[user_id] = {"questions": selected, "current": 0, "correct": 0}
    await send_question(user_id)

# ==================================================
# Отправка вопроса
# ==================================================
async def send_question(user_id: int):
    if user_id not in user_data:
        return
    data = user_data[user_id]
    q = data["questions"][data["current"]]

    options = q["options"].copy()
    random.shuffle(options)
    correct_text = q["options"][0]
    correct_index = options.index(correct_text)
    data["correct_index"] = correct_index

    keyboard_inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=options[0], callback_data="ans_0")],
            [InlineKeyboardButton(text=options[1], callback_data="ans_1")],
            [InlineKeyboardButton(text=options[2], callback_data="ans_2")],
            [InlineKeyboardButton(text=options[3], callback_data="ans_3")]
        ]
    )

    await bot.send_message(
        user_id,
        f"❓ Вопрос {data['current'] + 1} из {len(data['questions'])}\n\n{q['question']}",
        reply_markup=keyboard_inline
    )

# ==================================================
# Обработка ответа
# ==================================================
@dp.callback_query(lambda c: c.data.startswith("ans_"))
async def handle_answer(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_data:
        await callback.answer()
        return

    data = user_data[user_id]
    answer = int(callback.data.split("_")[1])

    if answer == data["correct_index"]:
        data["correct"] += 1

    data["current"] += 1
    await callback.answer()

    # убрать старые кнопки
    try:
        await callback.message.edit_reply_markup(reply_markup=None)
    except:
        pass

    # проверка конца викторины
    if data["current"] >= len(data["questions"]):
        if data["correct"] >= 4:
            if not promo_codes:
                await bot.send_message(user_id, "❌ Промокоды закончились.")
            else:
                promo = promo_codes.pop(0)
                used_users.add(user_id)
                save_used_users()
                await bot.send_message(user_id, f"🎉 Поздравляем!\n\nВаш промокод: {promo}")
        else:
            await bot.send_message(
                user_id,
                f"❌ Правильных ответов: {data['correct']} из {len(data['questions'])}\nПопробуйте позже!"
            )
        del user_data[user_id]
    else:
        await send_question(user_id)

# ==================================================
# Запуск
# ==================================================
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())