import time
import winsound
from win10toast import ToastNotifier

def timer(message, minutes):
    notificator = ToastNotifier()
    if minutes > 1:
        notificator.show_toast("Alarm", f"O Alarme vai desligar em {minutes} minutos...", duration=50)
    else:
        notificator.show_toast("Alarm", f"O Alarme vai desligar em {minutes} minuto...", duration=50)

    
    time.sleep(minutes * 60)
    winsound.Beep(frequency=2500, duration=1000)
    notificator.show_toast(f"Alarm", message, duration=50)


if __name__ == "__main__":
    minutes = int(input("Digite o tempo do timer: "))
    text = ""
    if minutes > 1: text = "minutos"
    else: text = "minuto"
    message = f"Alarme foi Concluído em {minutes} {text}!"
    
    timer(message, minutes)
    