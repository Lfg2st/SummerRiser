import random as rn

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        print('Hey there!')
    if p_message == 'roll':
        return str(rn.randint(1, 6))
    if p_message == '!help':
        return '`This is a help message`'
    