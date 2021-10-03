banaan = input("vindt u ook bananen lekker?")
poging = 1
print(poging)

while banaan != "quit":
    banaan = input("vindt u ook bananen lekker?")
    poging = poging + 1
    print(poging)
    if banaan == "quit":
        quit()
