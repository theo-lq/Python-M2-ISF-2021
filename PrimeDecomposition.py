value_occurence_list = lambda value_list : [[x, value_list.count(x)] for x in set(value_list)]




def product_list(value_list):
    product = 1
    for item in value_list:
        product *= item
    return product






def divisor_list(number):
    answer = [1]
    
    for candidate in range(2, number + 1):
        if number % candidate == 0:
            answer.append(candidate)
    
    return answer




def is_prime(number):
    divisor_number = len(divisor_list(number))
    return divisor_number == 2




def prime_list(number):
    prime_number_list = []
    for candidate in range(2, number + 1):
        if is_prime(candidate):
            prime_number_list.append(candidate)
    return prime_number_list    
    
    
    
    


def prime_decomposition(number):
    
    if is_prime(number):
        return number
    
    prime_number_list = prime_list(number)
    
    residual = number
    prime_decomposition_list = []
    for prime in prime_number_list:
        while residual % prime == 0 and residual > 0:
            residual = residual / prime
            prime_decomposition_list.append(prime)
    
    return prime_decomposition_list

    
    




def fancy_printing(prime_decomposition_list):
    number_exposant_list = value_occurence_list(prime_decomposition_list)
    inital_number = product_list([a[0] ** a[1] for a in number_exposant_list])
    answer = "%d = " % inital_number
    
    for number_exposant in number_exposant_list:
        answer = answer + "%d^%d * " % tuple(number_exposant)
    
    clean_answer = answer[:-3]
    return clean_answer