def computepay():
    hours = int(input('Enter Hours: '))
    rateperhour = float(input('Enter Rate Per Hours: '))
    if hours > 40:
        grosspay = ((((hours-40)*rateperhour)*1.5)+rateperhour*40)
    else:
        grosspay = hours*rateperhour
    return grosspay

print(computepay())
#hello from my side