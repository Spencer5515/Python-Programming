from Chef import Chef  # imports Chef class from Chef file
from ChineseChef import ChineseChef

# Inheritance
print("=== Inheritance ===\n")

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()
