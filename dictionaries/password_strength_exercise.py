def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"
    result = []
    for password in passwords:
        password_strength = {'length': False, 'digit': False, 'lowercase': False,'uppercase': False,  'special_char': False}
        if len(password) >= 8:
            password_strength['length'] = True
            
        for char in password:
            if char.isdigit():
                password_strength['digit'] = True
            if char.isupper():
                password_strength['uppercase'] = True
            if char.islower():
                password_strength['lowercase'] = True
            if char in special_characters:
                password_strength['special_char'] = True
        result.append((password, password_strength))
    return result

passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
