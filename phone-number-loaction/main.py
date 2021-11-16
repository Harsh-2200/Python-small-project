import phonenumbers
from phonenumbers import geocoder , carrier , timezone

number = input("Enter Mobile no. : ")

num = phonenumbers.parse(number , "IN" )                #IN --> Country History,INDIA

print(num)
print(type(num))
print(phonenumbers.is_valid_number(num))
print(phonenumbers.is_possible_number(num))
print(phonenumbers.format_number(num , phonenumbers.PhoneNumberFormat.E164))
print(phonenumbers.format_number(num , phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print(phonenumbers.format_number(num , phonenumbers.PhoneNumberFormat.NATIONAL))
print('--------------------------------------------------------------------------')

msg = "hey there! I'm Harsh call me at 9876543210 or 1234567890"
for match in phonenumbers.PhoneNumberMatcher(msg,"IN"):
    print(match)


print('--------------------------------------------------------------------------')
loc = geocoder.description_for_number(num, "en")
print(loc)


print('--------------------------------------------------------------------------')
ser = carrier.name_for_number(num , 'en')
print(ser)


print('--------------------------------------------------------------------------')
time = timezone.time_zones_for_number(num)
print(time)



