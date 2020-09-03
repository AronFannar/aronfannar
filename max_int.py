num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = 0

while num_int >= 0:
    if num_int > max_int: #Ef nýja talan er stærri en gamla þá er ný hæsta innslegna tala vistuð
        max_int = num_int #Endurstillt ný hæsta tala
    num_int = int(input("Input a number: ")) #Læt notanda slá inn tölu aftur

print("The maximum is", max_int)  #Prenta út hæstu töluna
