def check_palindrome(a):
    # We need to know how many characters are in the number so let's first convert it to a string
    a = str(a)
    # evaluating it's size
    string_size = len(a)
    # at first, let's assume it's not a palindrome
    palindrome = False

    if string_size % 2 != 0:
        stop = int((string_size - 1) / 2)
    else:
        stop = int(string_size / 2)
        
    # Checking all numbers
    for i in range(0,stop+1):
        if a[i] != a[-i-1]:
            palindrome = False
            break
        elif i == stop:
            palindrome = True

    return palindrome

numbers_to_use = list(range(1,99))
largest_palindrome_yet = 0

# here the loops check the product and, if is is bigger than the number we currently have, 
# it checks if it's a palindrome
for i in range(len(numbers_to_use)+1,0,-1):
    for ii in range(len(numbers_to_use)+1,0,-1):
        possible_palindrome = i*ii
        # check if the multiplication is larger than the largest_pal_yet
        if possible_palindrome > largest_palindrome_yet:
            # check if it's a palindrome
            palindrome = check_palindrome(possible_palindrome)
            if palindrome:
                largest_palindrome_yet = possible_palindrome
                a=i
                b=ii

print ("The largest palindrome we can build is ",largest_palindrome_yet," , which is the product of ", a, " and ", b)