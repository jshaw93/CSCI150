# James Shaw
# temp.py
# 11/29/21

# Use of static typing within Python!  Here I am telling the interpreter that fahrenheit is and must be a float
# as well as saying that the function returns and always will return a float.
def far_to_c(fahrenheit: float) -> float:
    """
    Converts degrees in Fahrenheit to degrees in Celsius. Takes a float "degrees in Fahrenheit"
    and returns a float "degrees in Celsius".

    :param fahrenheit: float
    :return: celsius float
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def c_to_far(celsius: float) -> float:
    """
    Converts degrees in Celsius to degrees in Fahrenheit . Takes a float "degrees in Celsius"
    and returns a float "degrees in Fahrenheit".

    :param celsius: float
    :return: fahrenheit float
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def below_freez_f(temps: list) -> list:
    """
    Takes a list of Fahrenheit temperatures as a parameter and returns a list of those temperatures below freezing (32F).
    For example, [3, 1, 10] should return [29, 31, 22].

    :param temps: list
    :return: list of temperatures after being subtracted from fahrenheit freezing point
    """
    # Use of the map function and a lambda (anonymous) function to quickly and efficiently apply the correct math to
    # every object in the list.
    # A lambda function is a kind of function that isn't defined within the code as a function, but rather plugged into
    # an existing parameter that calls for a function.  This is a perfect use of lambdas as it would be a waste to write
    # an entire new function that simply takes x and subtracts it from 32.
    # Use of lambdas
    # lambda arguments : expression.
    # Returns 32 - temp
    return list(map(lambda temp: 32 - temp, temps))


def below_freez_c(temps: list) -> list:
    """
    Takes a list of Celsius temperatures as a parameter and returns a list of those temperatures below freezing (0C).
    For example, [3, 1, 10] should return [-3, -1, -10]

    :param temps: list
    :return: list of temperatures after being subtracted from celsius freezing point
    """
    return list(map(lambda temp: 0 - temp, temps))


def weather(temperature: int) -> str:
    """
    Takes an int "temperature" and returns the string:
    Too hot  (if temp is > 90)
    Just right  (if temp is >70 and temp <=90)
    Chilly  (if temp is >50 and temp <=70)
    Cold  (if temp is >32 and temp <=50)
    Freezing  (if temp <=32)

    :param temperature: int
    :return: string
    """
    if temperature > 90:
        return "Too hot"
    elif 70 < temperature <= 90:
        return "Just right"
    elif 50 < temperature <= 70:
        return "Chilly"
    elif 32 < temperature <= 50:
        return "Cold"
    else:
        return "Freezing"


if __name__ == '__main__':
    # Test cases
    print("far_to_c 1: {} degrees f, results: {:.2f} degrees c".format(10, far_to_c(10)))
    print("far_to_c 2: {} degrees f, results: {:.2f} degrees c".format(45, far_to_c(45)))
    print("c_to_far 1: {} degrees c, results: {:.2f} degrees f".format(10, c_to_far(10)))
    print("c_to_far 2: {} degrees c, results: {:.2f} degrees f".format(45, c_to_far(45)))
    temperatures = [3, 1, 10]
    temperatures1 = [33, 10, 7]
    print("below_freez_f 1: {}, results: {}".format(temperatures, below_freez_f(temperatures)))
    print("below_freez_f 2: {}, results: {}".format(temperatures1, below_freez_f(temperatures1)))
    print("below_freez_c 1: {}, results: {}".format(temperatures, below_freez_c(temperatures)))
    print("below_freez_c 2: {}, results: {}".format(temperatures1, below_freez_c(temperatures1)))
    print("weather 1: {} degrees fahrenheit, results: {}".format(42, weather(42)))
    print("weather 2: {} degrees fahrenheit, results: {}".format(87, weather(87)))
