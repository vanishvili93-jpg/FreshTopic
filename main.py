import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://flamecoredup.top/click?key=ec4496c6669c47e5bb69785bca5bde2b", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Read", web_app=types.WebAppInfo(url=WEB_APP_URL)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Read now", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Read now", url="https://flamecoredup.top/click?key=ec4496c6669c47e5bb69785bca5bde2b")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📰 *Welcome to CA Daily Read.*\n\n"
        "Every day a curated selection of "
        "culture, travel, food, science "
        "and technology — to read at your "
        "own pace in chat.\n\n"
        "Tap *Today's picks* to begin.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Culture — fall exhibitions", callback_data="culture"),
        types.InlineKeyboardButton(text="🍁 Food — Canadian classics", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Travel — five hidden towns", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📋 *Today's picks*\n\n"
        "Three stories selected for today. "
        "Each one complete in chat.\n\n"
        "*Culture* — fall exhibitions: five "
        "must-see shows at Canadian museums.\n\n"
        "*Food* — Canadian classics: four "
        "dishes that define our cuisine.\n\n"
        "*Travel* — five hidden towns across "
        "Canada for a long weekend.\n\n"
        "Tap a title to read the full story.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🎨 *Fall exhibitions: five must-see "
        "shows at Canadian museums*\n\n"
        "Museums open the new season.\n\n"
        "*Toronto — AGO*\n"
        "The Art Gallery of Ontario presents "
        "a major retrospective of the Group "
        "of Seven. Rare sketches and field "
        "studies alongside the iconic canvases.\n\n"
        "*Montreal — MMFA*\n"
        "Montreal Museum of Fine Arts hosts "
        "an exhibition on contemporary "
        "Indigenous art from coast to coast. "
        "Painting, sculpture and installation.\n\n"
        "*Vancouver — VAG*\n"
        "Vancouver Art Gallery shows Emily "
        "Carr and the forests of BC. New "
        "restorations reveal colours unseen "
        "for a century.\n\n"
        "*Ottawa — National Gallery*\n"
        "Inuit art from Kinngait Studios. "
        "Prints, drawings and carvings that "
        "tell the story of the North.\n\n"
        "*Winnipeg — WAG-Qaumajuq*\n"
        "The world's largest public collection "
        "of Inuit art. New galleries dedicated "
        "to Arctic sculpture and textile.\n\n"
        "_Check museum websites for hours._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🍁 *Canadian classics: four dishes "
        "that define our cuisine*\n\n"
        "Canadian food is comfort, "
        "community and cold-weather cooking.\n\n"
        "*Poutine*\n"
        "Fresh-cut fries, cheese curds "
        "and hot gravy. The curds must "
        "squeak. Born in Quebec, loved "
        "everywhere. Best late at night.\n\n"
        "*Tourtiere*\n"
        "A savoury meat pie with pork, "
        "veal and spices in a flaky crust. "
        "Served at Christmas in Quebec "
        "and across the Maritimes. Every "
        "family has their own recipe.\n\n"
        "*Butter Tarts*\n"
        "Pastry shells filled with butter, "
        "sugar, syrup and egg. Runny or "
        "firm — the great Canadian debate. "
        "With or without raisins.\n\n"
        "*Nanaimo Bars*\n"
        "Three layers: chocolate coconut "
        "base, custard centre, chocolate "
        "ganache top. No baking required. "
        "Named after a town in BC.\n\n"
        "_Best enjoyed with a double-double._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🏠 *Five hidden towns across Canada*\n\n"
        "*Lunenburg (Nova Scotia)*\n"
        "A UNESCO World Heritage fishing "
        "town. Colourful waterfront, fresh "
        "lobster and the Bluenose legacy. "
        "Fall colours at their finest.\n\n"
        "*Elora (Ontario)*\n"
        "A limestone gorge, heritage "
        "buildings and artists' studios. "
        "The Grand River runs through. "
        "Quiet enough to hear it.\n\n"
        "*Tofino (British Columbia)*\n"
        "Surfing, old-growth rainforest "
        "and storm watching on the Pacific. "
        "A fishing village turned haven "
        "for those who love wild coast.\n\n"
        "*Kimberley (British Columbia)*\n"
        "A former mining town in the "
        "Rockies. Bavarian Platzl, skiing "
        "and mountain biking. Quiet seasons "
        "are the best seasons.\n\n"
        "*Saint-Irénée (Quebec)*\n"
        "A village on the St. Lawrence "
        "where the river becomes the sea. "
        "Domaine Forget concerts, autumn "
        "leaves and Charlevoix cheese.\n\n"
        "_Book ahead for Thanksgiving "
        "weekend._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glossary", callback_data="glossary"), types.InlineKeyboardButton(text="❓ FAQ", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))
    text = ("🏛 *Summary*\n\n"
        "From this menu you can:\n\n"
        "• Read *today's picks* and our stories.\n"
        "• Browse sections: Culture, Food, "
        "Travel, Science.\n"
        "• Check the glossary and FAQ.\n"
        "• Learn about us and get in touch.\n\n"
        "For the full edition, use the "
        "button below.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📖 *A short glossary*\n\n"
        "*Newsroom* — the team that selects "
        "and prepares stories.\n\n"
        "*Editorial* — an opinion piece that "
        "opens a section.\n\n"
        "*Photojournalism* — storytelling "
        "built around photographs.\n\n"
        "*Evergreen content* — stories whose "
        "relevance does not depend on the "
        "news of the day.\n\n"
        "*Correspondent* — a journalist "
        "reporting from the field.\n\n"
        "*Column* — a recurring section "
        "dedicated to a specific topic.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("❓ *Frequently asked questions*\n\n"
        "*Is this bot official?*\n"
        "CA Daily Read is an independent "
        "editorial project.\n\n"
        "*How often is it updated?*\n"
        "The selection is refreshed seasonally.\n\n"
        "*How do I mute notifications?*\n"
        "From Telegram chat settings.\n\n"
        "*Can I share a story?*\n"
        "Yes, using Telegram sharing options.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))
    text = ("✏️ *Contact*\n\n"
        "For editorial correspondence:\n"
        "• E-mail: hello@cadailyread.ca\n\n"
        "*Publisher*\n"
        "CA Daily Read Inc.\n"
        "100 King Street West\n"
        "Toronto, ON M5X 1A9\n"
        "Canada\n\n"
        "Reader feedback on working days.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"))
    text = ("🏛 *About CA Daily Read*\n\n"
        "CA Daily Read is an independent "
        "editorial project dedicated to "
        "culture, food, travel and "
        "technology in Canada.\n\n"
        "The editorial team selects quality "
        "content every day for an informed "
        "break from the daily routine.\n\n"
        "This Telegram edition is designed "
        "for comfortable reading in chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Welcome! Tap *Today's picks* to begin.", parse_mode="Markdown", reply_markup=markup)


print("CA Daily Read Bot is running...")
bot.infinity_polling()
