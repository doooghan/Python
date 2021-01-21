def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    fist_name = input("First name: ")
    if fist_name == 'q':
        break

    last_name = input("Last name: ")
    if last_name == 'q':
        break

    musician = get_formatted_name(fist_name, last_name)
    print("\nHello " + musician + "!")
