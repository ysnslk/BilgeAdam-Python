from random import choice, randint
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
    return choice(bot_list)

def roll_dice() -> int:
    return radiant(2, 12)

def gain_daily_chips() -> int:
    return radiant(1000, 2000)

def is_bet_valid(current_bet: int, safe: int) -> bool:
    if minimum_bet <= current_bet <= safe:
        return True
    else:
        return False

def login(user_name: str, password: str) -> dict:
   is_active = False
   user_id = ''
   for i in range(1, len(user_dict) + 1):
       if user_dict.get(str(i)).get('user_name') == user_name and user_dict.get(str(i)).get('password') == password:
           is_active = True
           user_id = str(i)
           break
   if is_active:
       return user_dict.get(user_id)
   else:
       return {}

def main():
    auth_user = login(
        input('Username: '),
        input('Password: ')
    )

    if auth_user != {}:
        print(f'Welcome {auth_user.get("user_name")}')
    else:
        print('Invalid Credantial...!')