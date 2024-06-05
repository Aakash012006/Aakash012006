# i. Function to square elements of a list
def square_elements(input_list):
    return [x ** 2 for x in input_list]

# ii. Function to provide weather advice
def weather_advice(temperature):
    if temperature < 0:
        return "Stay inside, it's freezing!"
    elif 0 <= temperature <= 15:
        return "Wear a coat."
    elif 16 <= temperature <= 25:
        return "A light jacket is enough."
    else:
        return "It's warm, dress lightly."

# Test the functions
input_list = [1, 2, 3, 
