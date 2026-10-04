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
    return types.InlineKeyboardButton(text="📰 Read now", url="https://techrazvitie.info/click?key=04423451acd741459fcc34014b3cbc85")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📰 *Welcome to SG Daily Read.*\n\n"
        "Every day a curated selection of "
        "culture, food, travel, science "
        "and technology — to read at your "
        "own pace in chat.\n\n"
        "Tap *Today's picks* to begin.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Culture — exhibitions to visit", callback_data="culture"),
        types.InlineKeyboardButton(text="🍜 Food — hawker classics", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Explore — five hidden spots", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📋 *Today's picks*\n\n"
        "Three stories selected for today. "
        "Each one complete in chat.\n\n"
        "*Culture* — exhibitions to visit: five "
        "must-see shows at Singapore museums.\n\n"
        "*Food* — hawker classics: four "
        "dishes every Singaporean knows.\n\n"
        "*Explore* — five hidden spots in "
        "Singapore for a weekend adventure.\n\n"
        "Tap a title to read the full story.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🎨 *Exhibitions to visit: five "
        "must-see shows in Singapore*\n\n"
        "Museums open the new season.\n\n"
        "*National Gallery Singapore*\n"
        "A major retrospective of Southeast "
        "Asian modern art. Rare works from "
        "private collections and unpublished "
        "archival material.\n\n"
        "*ArtScience Museum*\n"
        "Where art meets technology. New "
        "immersive installations exploring "
        "the boundary between digital "
        "and physical worlds.\n\n"
        "*Asian Civilisations Museum*\n"
        "Trade routes that shaped Asia. "
        "Ceramics, textiles and maps "
        "spanning four centuries of "
        "maritime exchange.\n\n"
        "*Singapore Art Museum (SAM)*\n"
        "Contemporary art from emerging "
        "Southeast Asian voices. Video, "
        "installation and photography "
        "in dialogue with the city.\n\n"
        "*Peranakan Museum*\n"
        "Straits Chinese heritage in full "
        "colour. Beadwork, porcelain and "
        "the stories behind the objects.\n\n"
        "_Check museum websites for timings._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🍜 *Hawker classics: four dishes "
        "every Singaporean knows*\n\n"
        "Singapore's hawker culture is "
        "UNESCO-recognised heritage.\n\n"
        "*Hainanese Chicken Rice*\n"
        "Poached chicken, fragrant rice "
        "cooked in chicken stock, chilli "
        "sauce, ginger paste and dark "
        "soy. The national dish. Simple "
        "and perfect.\n\n"
        "*Laksa*\n"
        "Thick rice noodles in a rich "
        "coconut curry broth with prawns, "
        "fishcake and cockles. Spicy, "
        "creamy and unforgettable.\n\n"
        "*Char Kway Teow*\n"
        "Flat rice noodles wok-fried with "
        "Chinese sausage, prawns, bean "
        "sprouts and egg. High heat, "
        "smoky wok hei flavour.\n\n"
        "*Roti Prata*\n"
        "Crispy flatbread served with "
        "fish or mutton curry. Pulled "
        "and flipped until layers form. "
        "Any time of day or night.\n\n"
        "_Best enjoyed at your nearest "
        "hawker centre._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Today's picks", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🏠 *Five hidden spots in Singapore*\n\n"
        "*Pulau Ubin*\n"
        "A short bumboat ride from Changi "
        "Point. Kampung houses, wild boar "
        "and mangrove trails. Old Singapore "
        "preserved on one island.\n\n"
        "*Haw Par Villa*\n"
        "Over a thousand statues depicting "
        "Chinese mythology. The Ten Courts "
        "of Hell. Surreal, free and unlike "
        "anything else on the island.\n\n"
        "*Henderson Waves*\n"
        "The highest pedestrian bridge in "
        "Singapore. Undulating wooden curves "
        "connecting two hilltop parks. "
        "Best at sunset.\n\n"
        "*Tiong Bahru*\n"
        "Art deco flats from the 1930s. "
        "Independent bookshops, specialty "
        "coffee and the old wet market "
        "downstairs. Heritage with a pulse.\n\n"
        "*Coney Island*\n"
        "A nature park off Punggol. "
        "Casuarina trees, quiet beaches "
        "and no cars. Cycling trails "
        "through untouched coastal forest.\n\n"
        "_Visit on weekday mornings for "
        "fewer crowds._")
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
        "Explore, Science.\n"
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
        "SG Daily Read is an independent "
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
        "• E-mail: hello@sgdailyread.sg\n\n"
        "*Publisher*\n"
        "SG Daily Read Pte. Ltd.\n"
        "1 Raffles Place\n"
        "Singapore 048616\n\n"
        "Reader feedback on working days.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"))
    text = ("🏛 *About SG Daily Read*\n\n"
        "SG Daily Read is an independent "
        "editorial project dedicated to "
        "culture, food, travel and "
        "technology in Singapore.\n\n"
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


print("SG Daily Read Bot is running...")
bot.infinity_polling()
