sm = int(input("Entering starting mileage: "))
em = int(input("Entering ending mileage: "))
te = float(input("Entering time elapsed in hours: "))
avg_speed = (em - sm)/te
print("Your average speed was",avg_speed,"mph.")