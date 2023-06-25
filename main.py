def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = input("Please enter temperature in celsius")
    celcius = float(celcius)

    fahrenheit = ((9.0 / 5.0) * celcius) + 32.0

    print(f"Farenheit: {fahrenheit:.2f}")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
