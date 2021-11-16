from classroom import ClassRoom


def main():

    print('Welcome to the teaching platform\n______________________')
    new_class = input(
        'would you like to CREATE or IMPORT a classroom (select create/import): ')
    if new_class == 'import':
        filename = input(
            'what file would you like to load? (no extension please)')
        c = ClassRoom.from_json(filename+'.json')

    else:
        subj = input('what is you class\'s subject? ')
        name = input('what is your name? ')
        c = ClassRoom(subj, name)
    # c = ClassRoom.from_json('pythonclass.json')
    while True:
        choice = input('''
        A. Add a student
        R. Remove a student
        E. Enrolled students
        J. Export data to json
        T. Take attendance
        S. Show attendance
        D. Search attendance (by date) 
        X. Exit
        ''')
        if choice in 'xX':
            print(f'Goodbye {c.teacher}')
            break

        elif choice in 'Aa':
            c.add_student()
        elif choice in 'jJ':
            filename = input(
                'what would you like to name the file? (no extension please)')

            c.to_json(filename+'.json')

        elif choice in 'rR':
            c.remove_student()
        elif choice in 'Tt':
            c.take_attendance()
        elif choice in 'Ss':
            c.show_students()
        elif choice == 'populate':
            num = int(input('how many students? '))
            c.populate_class(num)


main()
