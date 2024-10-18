#write functions here, don't add input('') statements here!
def test_config():
    return True

def reverse_string(string1):
    count=0
    rev=''

    while count < len(string1):
        rev=string1[count]+rev
        count+=1
    return rev