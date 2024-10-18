#add import
import question_b

def main():
    numb=int(input("Enter a number here to check if number is prime or enter 0 to quit "))

    while numb != 0:
        print(question_b.is_prime(numb))
        numb=int(input("Enter a number here to check if number is prime or enter 0 to quit "))
main()