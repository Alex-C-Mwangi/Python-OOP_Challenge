from pet import Pet
def main():
    if __name__ == "__main__":
        my_pet = Pet("Phany") #Giving pet name.
        my_pet.get_status() #Checks the hunger, energy and happiness of pet
        my_pet.eat() #Testing eat method
        my_pet.get_status()
        my_pet.train("Jump") #Training new trick
        my_pet.show_tricks() #Shows ist of tricks learnt
main()
