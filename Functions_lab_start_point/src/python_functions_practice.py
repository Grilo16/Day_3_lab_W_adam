
def return_10():
    return 10

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x ,y):
    return x * y

def divide(x, y):
    return x/y

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(sInt1, sInt2):
    sInt1 = int(sInt1)
    sInt2 = int(sInt2)
    return sInt1 + sInt2

def number_to_full_month_name(key):
    months = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }
    return months[key]

def number_to_short_month_name(key_for_short_name):
    # First get january back from the integer 1 and store it in a varible
    month = number_to_full_month_name(key_for_short_name)
    # get the first 3 characters from january and store it in a variable
    first_three = month[0:3]
    # return variable
    return first_three


# we need a function to cube a integer 
def volume_of_cube(integer):
    # return the cubed value
    return integer ** 3


def reverse_string(string):
    return string[::-1]


def fahrenheit_to_celsius(temperatureF):
    return float("{0:.1f}".format((temperatureF - 32)*(0.5556)))