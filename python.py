def personal_info(first_name, last_name, date_of_birth, email):
    at_index = email.index('@')
    masked_information = {
        "first_name": first_name[:2] + "*" * (len(first_name) - 2),
        "last_name": last_name[:2] + "*" * (len(last_name) - 2),
        "date_of_birth": date_of_birth[:2] + "*" * (len(date_of_birth) - 2),
        "email": email[:2] + "@" + "*" * (at_index - 2) + email[at_index:at_index],
        
    }
    return masked_information

first_name = "Diana"
last_name = "Mongina"
date_of_birth = "1998-15-02"
email = "dianahmongina2@gmail.com"


masked_values = personal_info(first_name, last_name, date_of_birth, email)
print(masked_values)
