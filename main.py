# set up the lists to store the colors and values associted with the resistors
colors_gen = ["black", "brown", "red", "oranage", "yellow", "green", "blue",
              "purple", "gray", "white"]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
multiplier = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000,
              100000000, 100000000]
num = 0


def num_of_bands():
    # this function did not end up being as used since my plan on how to do this changed
    # keeping it since it may be useful once the camera gets involved
    band_num = input("How many bands does the resistor have? ")
    while band_num.isdigit() == False:
        band_num = input("Please enter a number (ie 1 or 2) ")
    if int(band_num) >= 5:
        print("Looks like you have a tolorance and possibly a temp coeff.")
        # this is the max that the resistor can have that effects the math
        band_num = 4
    global num
    num = int(band_num)
    return int(band_num)


def band_colors():
    # getting the colors from the user
    # calls color_check to then check those colors
    print("There should be three or four bands that are closer together. ")
    print("It is very important that when you list the colors in a moment,"
        " you do so with the colors in order.")
    print("In no case should a black band be first.")
    user_colors = input("What are the colors of those bands on the resistor? "
        "Please enter the list separated by a space: ")
    colors_resistor_user = user_colors.split()
    list = color_check(colors_resistor_user)
    return list


def color_check(color_resisitor_list):
    # functions for making sure the colors given are valid
    j = 0
    for color in color_resisitor_list:
       response = check(color, j)
       j = j+1
       if response == False:
        print("One of the colors you entered was invalid"
              " please try again. ")
        return band_colors()
    print("You colors match what I have as resistor colors")
    return color_resisitor_list


def check(color, num):
    j = num
    black = "Black"
    match = False
    i = 0
    while match == False:
        i = 0
        for baseColor in colors_gen:
            if baseColor.casefold() == color.casefold():
                if j == 0 and color.casefold() == black.casefold():
                    print("Black can not be first")
                    return False
                else:
                    return True
            if match == False and i == 9:
                return False
            i = i+1


def math(user_resistor_list):
    # function for doing the math to calculate the resitance
    total = 0
    i = 0
    print("placeholder")
    for current in user_resistor_list:
        position = getPosition(current)
        if i == 0:
            total = total+digits[position]
            i = i+1
        elif i == 1:
            total = total+(digits[position]*0.1)
            i = i+1
        elif i == 2:
            total = total+(10**digits[position])
            i = i+1
        elif i > 3:
            print("these bands are tolorance and tempture which do not effect the calculation")
        else:
            print("error")
    return total


def getPosition(color):
    # get the position of the current color and return it
    i = 0
    for base_color in colors_gen:
        if base_color.casefold() == color.casefold():
            return i
        i = i+1


def main():
    print("test")
    user_list = band_colors()
    print(math(user_list))


if __name__ == "__main__":
    main()
