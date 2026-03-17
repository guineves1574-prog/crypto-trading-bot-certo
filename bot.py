import time

running_bots = {}

def run_bot(user_id):
    running_bots[user_id] = True

    while running_bots.get(user_id):
        print(f"Rodando bot do usuário {user_id}")
        time.sleep(60)

def stop_bot(user_id):
    running_bots[user_id] = False
