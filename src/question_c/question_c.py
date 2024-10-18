#write functions here, don't add input('') statements here!

def get_person_category(age):
    if 0<=age<=1:
        return "infant"
    elif 1<age<13:
        return "child"
    elif 13<=age<20:
        return "teenager"
    elif 20<=age<=125:
        return "adult"
    else:
        return "invalid age"