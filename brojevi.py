
print(" ____  __.  _____  .____     ____  __.____ ___.____       _______________________ __________ ")
print("|    |/ _| /  _  \ |    |   |    |/ _|    |   |    |     /  _  \__    ___\_____  \\______   ")
print("|      <  /  /_\  \|    |   |      < |    |   |    |    /  /_\  \|    |   /   |   \|       _/ ")
print("|    |  \/    |    |    |___|    |  \|    |  /|    |___/    |    |    |  /    |    |    |   ")
print("|____|__ \____|__  |_______ |____|__ |______/ |_______ \____|__  |____|  \_______  |____|_  / ")
print("        \/       \/        \/       \/                \/       \/                \/       \/ ")


while True:

    print ("  IZBOR  ")
    print ("------------------")
    print (" A - zbrajanje")
    print (" B - oduzimajne")
    print (" C - množenje")
    print (" D - dijelenje")
    print (" X - izlaz")
    izbor = input (" >>  ")

    if izbor == "a" or izbor == "A" :
        prvibroj = int (input(" Prvi pribrojnik "))
        drugibroj = int (input(" Drugi pribrojnik "))

        rezultat = prvibroj + drugibroj
    if izbor == "b" or izbor == "B" :
        prvibroj = int (input(" umanjenik "))
        drugibroj = int (input(" umanjitelj "))
        rezultat = prvibroj - drugibroj
    if izbor == "c" or izbor == "C" :
        prvibroj = int (input(" faktor 1 "))
        drugibroj = int (input(" faktor 2 "))

        rezultat = prvibroj * drugibroj
    if izbor == "d" or izbor == "D" :
        prvibroj = int (input(" djeljenik "))
        drugibroj = int (input(" djelitelj "))

        rezultat = prvibroj / drugibroj
    if izbor == "X" or izbor == "x":
        rezultat = 0
        break       
    else:
        print (rezultat)