import random
# Basit Barbut oyunu
# bots = ['ahmet','mehmet','ayşe'] login olan kullanıcıya bu listeden random rakip rakip atanacak
# minimum_bet = 100 yani 50 chip bet yapılamayacak
# Kullanıcıların kasası olacak. Kazanırsa yaptığı bahis iki katı olacak. Kaybederse yaptığı bahis hesaptan düşecek.
# Login işlemi olsun
# Kullanıcı login olduğunda daily chip hediye edilsin (1000, 2000) arasında olsujn

bots = ['ahmet','mehmet','ayşe']
minimum_bet = 100
user_dict = {
    '1': {
        'user_name': 'beast',
        'password': '123',
        'safe': 1200
    },
    '2': {
        'user_name': 'savage',
        'password': '123',
        'safe': 2000
    }
}

def assing_default_player(bot_list: list) -> str:
    return random.choice(bot_list)

def roll_dice() -> int:
    return random.radiant(2, 12)

def gain_daily_chips() -> int:
    return random.radiant(1000, 2000)

def is_bet_valid(current_bet: int, safe: int) -> bool:
    if minimum_bet <= current_bet <= safe:
        return True
    else:
        return False