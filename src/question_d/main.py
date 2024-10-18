#add import
import question_d

def main():
    week=int(input("Enter a number that corresponds with a day of the week or type -1 to exit "))

    while week != -1:
        print(question_d.get_day_of_week(week))
        week=int(input("Enter a number that corresponds with a day of the week or type -1 to exit "))

main()
