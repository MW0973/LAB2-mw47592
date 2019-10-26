# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def czyszczenie():
  # sleep for 2 seconds after printing output 
    sleep(2) 
  
      # now call function we defined above 
    clear() 


while(True):

  print("1. Dodawanie")
  print("2. Odejmowanie")
  print("3. Mnozenie")
  print("4. Dzielenie")
  print("0. Wyjdz")
  

  wybor=int(input("Wybierz dzialanie lub wyjscie: "))

  if wybor==1:
    x=float(input("Pierwsza liczba: "))
    y=float(input("Druga liczba: "))
    print(x, "+", y,"=", (x+y))
    czyszczenie()
  elif wybor==2:
    x=float(input("Pierwsza liczba, odjemna: "))
    y=float(input("Druga liczba, odjemnik: "))
    print(x, "-", y,"=", (x-y))
    czyszczenie()
  elif wybor==3:
    x=float(input("Pierwsza liczba: "))
    y=float(input("Druga liczba: "))
    print(x, "*", y,"=", (x*y))
    czyszczenie()
  elif wybor==4:
    x=float(input("Pierwsza liczba, dzielna: "))
    y=float(input("Druga liczba, dzielnik: "))
    print(x, "/", y,"=", (x/y))
    czyszczenie()
  elif wybor==0:
    exit=input("Czy napewno chcesz wyjsc? Y/N  ")
    if exit=="Y"or exit=="y":
      czyszczenie()
      break
  

  else:
    print("Nie ma takiej pozycji w menu")