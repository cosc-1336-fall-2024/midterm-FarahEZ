#add import
import question_c

def main():
    yr=int(input("Enter your age to see your age catagory or type -1 to opt out "))

    while yr != -1:
        print(question_c.get_person_category(yr))
        yr=int(input("Enter your age to see your age catagory or type -1 to opt out "))

main()