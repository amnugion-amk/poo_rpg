import playerClass
import utilities

utilities.addHeader("CHARACTER CREATION")

targname = input("Enter your name:  ")
targage = int(input("Enter your age:    "))
targgender = input("Enter your gender (M) or (F):  ")

plr = playerClass.plr(targname, targage, targgender)
print(f"Player Stats: {plr.name}, {plr.age}, ({plr.gender})")