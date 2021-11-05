import random


class Game:
    def __init__(self):
        self.result = {
            'win': 0,
            'loose': 0,
            'draw': 0
        }

        while True:
            self.user_item = self.get_user_item()
            self.computer_item = self.get_computer_item()
            self.get_game_result(self.user_item, self.computer_item)

    def get_user_item(self):
        while True:
            user_item = input('g. Play a new game\nx. Exit\n')
            if user_item in 'xX':
                print('byeeeee')
                print(self.result)
                exit()
            elif user_item.lower() == 'g':
                user_item = input(
                    'select (r)ock, (p)aper or (s)cissors:\n').lower()
                return user_item

    def get_computer_item(self):
        rps = ['r', 'p', 's']
        return random.choice(rps)

    def get_game_result(self, user_item, computer_item):
        result = f"You selected {user_item}. The computer selected {computer_item}."
        if user_item == computer_item:
            self.result['draw'] += 1
            return print(f'{result} You draw')
        elif user_item in 'rR' and computer_item == 'p':
            self.result['loose'] += 1
            return print(f'{result} You loose')
        elif user_item in 'rR' and computer_item == 's':
            self.result['win'] += 1
            return print(f'{result} You win')
        elif user_item in 'pP' and computer_item == 's':
            self.result['loose'] += 1
            return print(f'{result} You loose')
        elif user_item in 'pP' and computer_item == 'r':
            self.result['win'] += 1
            return print(f'{result} You win')
        elif user_item in 'sS' and computer_item == 'r':
            self.result['loose'] += 1
            return print(f'{result} You loose')
        elif user_item in 'sS' and computer_item == 'p':
            self.result['win'] += 1
            return print(f'{result} You win')
        else:
            print('not a valid choice')


def play():
    g = Game()


play()
