# convert farhenite into the celcious

farh_ = float(input("Farhnite value: "))
cel = (farh_ - 32) * 5.0/9.0

print("In Degree Celcious:", cel)

if cel > 40:
    print("So HOT!")

elif (25 >= cel and cel >= 22):
        print("Absolute Room Temperature!")

elif 40 > cel and cel > 1:
    print("Normal Temperarture")

elif cel <= 0:
    print("Freezin Cold!") 

# Degree into the Farehnite

# cel = float(input("In Celcious value: "))
# farh_ = (cel * 9.0/5.0) + 32

# print("In Farehnite:", farh_)

