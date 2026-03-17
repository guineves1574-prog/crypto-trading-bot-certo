bots = {}

def start_user_bot(user_id):
    from app.bot import run_bot
    import threading

    if user_id in bots:
        return "Já rodando"

    thread = threading.Thread(target=run_bot, args=(user_id,))
    bots[user_id] = thread
    thread.start()

    return "Bot iniciado"

def stop_user_bot(user_id):
    from app.bot import stop_bot

    stop_bot(user_id)
    bots.pop(user_id, None)

    return "Bot parado"

def get_status(user_id):
    return user_id in bots
