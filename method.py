import requests

def logTelegram(message):

    #### TELEGRAM INFO ####
    BOT_TOKEN = "6193298516:AAHMckLXP_mBDO9tmfz78AOLE9NpOqRGF2w" # Don't change it
    CHAT_ID = "YOUR CHAT_ID" # Your chatID, use https://t.me/getmyid_bot to know
    #######################

    # API bot telegram to send message
    apiURL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    try:
        requests.post(apiURL, json={'chat_id': CHAT_ID, 'text': message})
    except Exception as e:
        print(e)

def logFile(message, filename):
    # File .txt will be saved on the "log_file" directory
    with open(f"log_file/{filename}.txt", "w") as f:
            print(message, file=f)
    print(f"[+] Saved {filename}.txt")

