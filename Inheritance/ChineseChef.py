from Chef import Chef  # imports Chef class from Chef file

class ChineseChef(Chef):  # child class -> (Chef) inherits Chef attributes

    def make_special_dish(self):  # overrides parent function
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")
