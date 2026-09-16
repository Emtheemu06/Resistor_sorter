# importing numbers so I have easy access to some functions
import numbers

#setting up the lists to store the colors and values associted with the resistors
colors_gen=["black","brown","red","oranage","yellow","green","blue","purple","gray","white"]
digits=[0,1,2,3,4,5,6,7,8,9]
multiplier=[1,10,100,1000,10000,100000,1000000,10000000,100000000,100000000]

def num_of_bands():
    band_num=input("How many bands does the resistor have? ")
    while band_num.isdigit()==False:
        band_num=input("Please enter a number (ie 1 or 2) ") 
    if int(band_num)>=5:
        print("Looks like you have a tolorance and possibly a temp coeff.")
        band_num=4 #this is the max that the resistor can have that effects the math
    return int(band_num)

def band_colors(band_num):
    #getting the colors from the user 
    #calls color_check to then check those colors
    print("There should be three or four bands that are closer together. ")
    user_colors=input("What are the colors of those bands on the resistor? Please enter the list separated by a space: ")
    colors_resistor=user_colors.split()

def color_check(color_resisitor):
#functions for making sure the colors given are valid
    for color in color_resisitor:
        match=False
        while match ==False:
            #insert for loop to loop through the other list and see if the colors match on in the list

  
def main():
    print("test")
    bandTest=num_of_bands()
    print(bandTest)


if __name__=="__main__" :
    main()