# def describe_pet(animal_type, pet_name):
#     """显示宠物信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet('hamster', 'harry')
# # 关键字实参
# describe_pet(pet_name='willie', animal_type='dog')

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('willie')
describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', 'hamster')  # error
describe_pet('harry', animal_type='hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
