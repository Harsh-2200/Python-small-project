import phonenumbers

number = "9876543210"

num = phonenumbers.parse(number , "IN" )                #IN --> Country History,INDIA

print(num)
print(type(num))
print(phonenumbers.is_valid_number(num))
print(phonenumbers.is_possible_number(num))
print(phonenumbers.format_number(num , phonenumbers.PhoneNumberFormat.E164))
print(phonenumbers.format_number(num , phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print(phonenumbers.format_number(num , phonenumbers.PhoneNumberFormat.NATIONAL))
print('--------------------------------------------------------------------------')



