   ### Armstrong Numbers

while True :
    number = input("Enter a positive integer number to learn if it is an 'Armstrong Number': ")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, "is invalid entry. enter numberic value!")
    elif int(number) >= 0 :
        for i in range(digits) :
            summ = summ + int(number[i]) ** digits
        if summ == int(number) :
            print(number, "is an 'Armstrong Number'.")
            break
        else :
            print(number, "is NOT an 'Armstrong Number'.")
            break
