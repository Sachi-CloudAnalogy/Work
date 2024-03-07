#verifying email

from email_validator import validate_email

email = "sachi123@gmail.com"
email2 = "abcgmail.com"

def validate(email):
    try:
        value = validate_email(email)   #return object that need to be normalised
        if email == value.normalized:
            print("Valid")
    except:
        print("Error")    
    
validate(email) 
validate(email2)  