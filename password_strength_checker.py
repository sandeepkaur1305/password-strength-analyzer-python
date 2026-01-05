import getpass
def occurence(key,feature):
    """
    Prints feedback if a required character type is missing.
    """
    if key<1:
        print(f"include {feature} ")
    else:
        pass
def password_strength(passw):
    """
    Analyzes password strength based on length and character diversity.
    """
    lower_count=0
    upper_count=0
    digit_count=0
    special_count=0
    try: 
        if not passw:
            print("Password cannot be empty.")
            return
        if len(passw)<=8:
            print("Set a long password!!")
            return
        for item in passw:
            if item.isalpha():
                if item.islower():
                    lower_count+=1
                else:
                    upper_count+=1
            elif item.isdigit():
                digit_count+=1
            else:
                special_count+=1
        # Strength decision
        if lower_count>=1 and upper_count>=1 and digit_count>=1 and special_count>=1:
            print("Password strength: STRONG")
        
        else:
            print("Password strength: WEAK")
            print("Suggestions to improve your password:")
            occurence(lower_count,"lower characters")
            occurence(upper_count,"upper characters")
            occurence(special_count,"special characters")
            occurence(digit_count,"digits")

    except Exception as e:
        # Controlled error handling (no crash, no sensitive output)
        print("Password analysis failed due to an internal error.")
# Secure input (masked)
password_input = getpass.getpass("Enter password: ")

# Analyze password
password_strength(password_input)

# Clear sensitive data from memory
del password_input

        
