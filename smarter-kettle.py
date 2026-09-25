import time
from smarter import SmarterClient

# IP-Adresse deines Smarter SMK20 im WLAN
KETTLE_IP = "192.168.0.80"

def main():
    # Verbindung zum Wasserkocher aufbauen (Standardport 2081)
    client = SmarterClient(KETTLE_IP)
    
    print("Verbinde mit Smarter iKettle...")
    if not client.connect():
        print("Verbindung fehlgeschlagen!")
        return

    # 1. Status auslesen
    status = client.get_status()
    print(f"Aktuelle Temperatur: {status.temperature}°C")
    print(f"Wasserstand: {status.water_level}%")
    print(f"Status: {'Heizt' if status.is_heating else 'Bereit'}")

    # 2. Wasser auf 85°C erhitzen
    # Parameter: Zieltemperatur in °C, Warmhaltezeit in Minuten (0-20)
    target_temp = 85
    keep_warm_time = 5

    print(f"Starte Erhitzen auf {target_temp}°C (Warmhalten: {keep_warm_time} Min)...")
    client.start_heating(temperature=target_target_temp, keep_warm=keep_warm_time)

    # Kurz warten und erneuten Status prüfen
    time.sleep(2)
    status = client.get_status()
    print(f"Neuer Status - Heizt: {status.is_heating}")

    # Verbindung trennen
    client.disconnect()

if __name__ == "__main__":
    main()
