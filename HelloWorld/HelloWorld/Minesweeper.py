from Minesweeper_Methods_Groups import print_field, create_field, select_field_constraints, load_field, safe_field


field_constraints = select_field_constraints()
fields = create_field(field_constraints)
while True:
    print_field(field_constraints, fields)
    cmd = input('> ')

    if cmd.lower() == 'help':
        print('display - to display field')
        print('number - to turn field')
        print('quit - to quit game')
        print('newgame - to create a new game')

    elif cmd.lower() == 'quit':
        break

    elif cmd.lower() == 'newgame':
        field_constraints = select_field_constraints()
        fields = create_field(field_constraints)

    elif cmd.lower() == 'safe':
        print('game saved')
        safe_field(fields)

    elif cmd.lower() == 'load':
        print('load')
        load_return = load_field()
        fields = load_return[0]
        field_constraints = load_return[1]
    else:
        try:
            t = int(cmd)
            if t < field_constraints[0]*field_constraints[1]:
                lost = fields[t].turn(field_constraints, fields, t)
                if lost:
                    yes_no = input('do you want to play again? (Y/N) ')
                    if yes_no.lower() == 'y':
                        field_constraints = select_field_constraints()
                        fields = create_field(field_constraints)

                    else:
                        break
            else:
                print('sorry - your number exceeds the field size')
        except ValueError:
            print('sorry - your command is not known')

    Number_of_closed_fields = 0
    for item in fields:
        if not item.turned:
            Number_of_closed_fields += 1
    if field_constraints[2] == Number_of_closed_fields:
        print('')
        print('')
        print('congratulations - YOU WON')
        print('')
        print('')
        yes_no = input('do you want to play again? (Y/N) ')
        if yes_no.lower() == 'y':
                field_constraints = select_field_constraints()
                fields = create_field(field_constraints)

        else:
            break

