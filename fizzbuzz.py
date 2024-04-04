def fizzbuzz(number):
    if number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    elif number %3 and number % 5 == 0:
        return "Fizzbuzz"
    else: 
        return number
    
for i in range(100):
    print(fizzbuzz(i))
