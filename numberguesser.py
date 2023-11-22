from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import random

TOKEN = '6621281346:AAF-YjiAdw8XGDusYL3pO1Dj8q0k8bTJ9pA'

def start(update, context):
    update.message.reply_text("Welcome to the Guess the Number game! I'm thinking of a number between 1 and 100. Start guessing!")
    context.user_data['number_to_guess'] = random.randint(1, 100)
    context.user_data['attempts'] = 0

def guess(update, context):
    user_guess = int(update.message.text)
    context.user_data['attempts'] += 1

    correct_number = context.user_data['number_to_guess']

    if user_guess == correct_number:
        update.message.reply_text(f"Congratulations! You guessed the correct number {correct_number} in {context.user_data['attempts']} attempts.")
        context.user_data.pop('number_to_guess')
        context.user_data.pop('attempts')
    elif user_guess < correct_number:
        update.message.reply_text("Wrong guess. Try again! Your guess is too low.")
    else:
        update.message.reply_text("Wrong guess. Try again! Your guess is too high.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, guess))
    print("Bot is ready. Polling for updates...")

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
