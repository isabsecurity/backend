import threading
import os

def run_django():
    os.system("python manage.py runserver")

def run_bot():
    os.system("python manage.py bot")

if __name__ == "__main__":
    django_thread = threading.Thread(target=run_django)
    bot_thread = threading.Thread(target=run_bot)

    django_thread.start()
    bot_thread.start()

    django_thread.join()
    bot_thread.join()