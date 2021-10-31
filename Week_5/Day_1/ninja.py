class Phone:
    def __init__(self, phone_number):
        self.number = phone_number
        self.call_history = []
        self.messages = []

    def phone_call(self, other_phone):
        call_string = f'Call from: {self.number} to:{other_phone.number}'
        self.call_history.append(call_string)
        other_phone.call_history.append(call_string)

    def show_call_history(self):
        for record in self.call_history:
            print(f'\n{record}')

    def send_message(self, other_phone, content):
        if content:
            message = {
                'to': other_phone.number,
                'from': self.number,
                'content': content
            }
            self.messages.append(message)
            other_phone.messages.append(message)
        else:
            print('you can\'t send empty messages')

    def show_outgoing_messages(self):
        print('SHOWING OUTGOING MESSAGES:')
        for message in self.messages:
            if message['from'] == self.number:
                print(f'Sender: {message["to"]}\nContent:{message["content"]}')
        print('------- End ------\n')

    def show_incoming_messages(self):
        print('SHOWING INCOMING MESSAGES:')
        for message in self.messages:
            if message['to'] == self.number:
                print(
                    f'Sender: {message["from"]}\nContent:{message["content"]}')
        print('------- End ------\n')

    def show_messages_from(self, other_number):
        print(f'SHOWING MESSAGES FROM {other_number}:')
        for message in self.messages:
            if message['from'] == other_number:
                print(f'Content: {message["content"]}')
        print('------- End ------\n')


phone1 = Phone('0543212234')
phone2 = Phone('0544567890')
phone3 = Phone('0544567343')
phone1.phone_call(phone2)
phone2.phone_call(phone1)
phone1.show_call_history()
phone1.send_message(phone2, 'Message 1')
phone2.send_message(phone3, 'Super interesting Message #2 ')
phone3.send_message(phone1, 'Super interesting Message #3')
phone2.send_message(phone1, 'bland message #4')

phone1.show_incoming_messages()
phone2.show_outgoing_messages()
phone3.show_messages_from('0544567890')
