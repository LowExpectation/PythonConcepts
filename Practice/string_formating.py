format_string="I am {} years old"
gift="I got {}{:.3f}"
age=31
currency_sign="$"
value_gift=1000000

if age > 30:
    format_string="I am {}"
    age=str("way to old")

    print(format_string.format(age))
pass
    
print(gift.format(currency_sign,value_gift))

user_input=input("What is your age? ")
print(format_string.format(user_input))
