from django.utils import timezone
from kamerachi.models import Order,TelegramAdminsID
from django.db.models.signals import post_save
from django.dispatch import receiver
from tg_bot.bot import bot
@receiver(post_save, sender=Order)
def order_created_handler(sender, instance, created, **kwargs):
    if created:
        print("Order Creat")
        msg = (
            f"🆕 Yangi zayafka:\n\n"
            f"👤 Ism: {instance.name}\n"
            f"📞 Tel: {instance.phone}\n"
            f"🛠 O'rnatib berish bilan: {'✅' if instance.service_included else '❌'}\n"
            f"🕒 Sana: {timezone.localtime(instance.created_at).strftime('%Y-%m-%d %H:%M')}"
        )

        for tg_id in TelegramAdminsID.objects.all():
            result = bot.send_message(chat_id=tg_id.tg_id, text=msg)
            if result:
                print(f"✅ Yuborildi: {tg_id.tg_id}")
            else:
                print(f"❌ Xatolik: {tg_id.tg_id}")

