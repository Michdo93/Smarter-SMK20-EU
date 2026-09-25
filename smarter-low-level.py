import socket
import time

KETTLE_IP = "192.168.0.80"
PORT = 2081  # Port für iKettle 2.0 / Smarter Coffee

def send_smarter_command(command_hex):
    """Sendet ein Byte-Array an den Wasserkocher und liest die Antwort."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3.0)
        sock.connect((KETTLE_IP, PORT))

        # Befehl senden
        sock.sendall(command_hex)
        
        # Antwort empfangen
        response = sock.recv(1024)
        sock.close()
        return response
    except Exception as e:
        print(f"Fehler bei Socket-Verbindung: {e}")
        return None

# --- Befehle definieren ---
# Hex-Aufbau für "Kochen auf 85°C" (0x15 = Start, 0x55 = 85 in Hex, 0x00 = KeepWarm Off, 0x7e = Endbyte)
CMD_HEAT_85 = bytes([0x15, 0x55, 0x00, 0x7e])
CMD_STOP = bytes([0x14, 0x7e])

# Beispielaufruf:
print("Sende Heizbefehl (85°C)...")
res = send_smarter_command(CMD_HEAT_85)
if res:
    print(f"Antwort vom Wasserkocher (Hex): {res.hex()}")
