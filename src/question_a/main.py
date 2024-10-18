#add import
import question_a

def main():
    st=input("Enter a string to get the reverse or type Q to quit ")
    while st !="Q" and st !="q":
        print(question_a.reverse_string(st))
        st=input("Enter a string to get the reverse or type Q to quit ")

main()
