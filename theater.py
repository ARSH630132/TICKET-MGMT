#THEATER SEATING 

import numpy as np
matrix = np.full((5, 10),"AVAILABLE")
print(matrix)

print("\nPRESS BOOK TO BOOK SEAT ")
print("PRESS CHECK TO CHECK SEAT IS AVAILABLE OR NOT ")
print("PRESS CANCEL TO CANCEL BOOKING ")
print("PRESS PRICE TO CHECK REVENUE ")

#FUNCTION FOR BOOKING
def book():
    while True:
        try:
            row=int(input("ENTER ROW NUMBER : "))
            column=int(input("ENTER COLUMN NUMBER : "))
            if(0<=row<=5 and 0<=column<=9):
              if(matrix[row][column]=="AVAILABLE"):
                matrix[row][column]="BOOKED"
                print("SEAT BOOKED SUCESSFULLY ")
                break
              elif(matrix[row][column]=="BOOKED"):
                print("SEAT ALREADY BOOKED ")
                break
            else:
                print("VALID ROW AND COLUMN")
        except ValueError:
            print("ROW AND COLUMN SHOULD BE INTEGER : ")
            book()
        except IndexError:
            print("PLEASE ENTER A VALID ROW AND COLUMN : ")
            book()

#FUNCTION FOR CHECKING
def check():
    while True:
        try:
            row=int(input("ENTER ROW NUMBER : "))
            column=int(input("ENTER COLUMN NUMBER : "))
            if(0<=row<=5 and 0<=column<=9):
              if(matrix[row][column]=="AVAILABLE"):
                print("SEAT IS AVAILABLE ")
                break
              elif(matrix[row][column]=="BOOKED"):
                print("SEAT ALREADY BOOKED ")
                break
            else:
                print("VALID ROW AND COLUMN")
        except ValueError:
            print("ROW AND COLUMN SHOULD BE INTEGER : ")
            check()
        except IndexError:
            print("PLEASE ENTER A VALID ROW AND COLUMN : ")
            check()


#FUNCTION FOR CANCELLING
def cancel():
    while True:
        try:
            row=int(input("ENTER ROW NUMBER : "))
            column=int(input("ENTER COLUMN NUMBER : "))
            if(0<=row<=5 and 0<=column<=9):
              if(matrix[row][column]=="AVAILABLE"):
                print("SEAT NOT BOOKED ")
                break
              elif(matrix[row][column]=="BOOKED"):
                matrix[row][column]="AVAILABLE"
                print("SEAT CANCELLATION SUCCESSFULLY ")
                break
            else:
                print("VALID ROW AND COLUMN")
        except ValueError:
            print("ROW AND COLUMN SHOULD BE INTEGER : ")
            cancel()
        except IndexError:
            print("PLEASE ENTER A VALID ROW AND COLUMN : ")
            cancel()


#FUNCTION FOR PRICE
def price():
   d=0
   e=0
   for i in range(len(matrix)): 
      for j in range(len(matrix[0])): 
        if(0<=(i)<=2 and (i)=="BOOKED"):
           d=d+1
        f=500*d
        if((3<=(i)<=4 and (i)=="BOOKED")):
           e=e+1
        g=e*300
        print(f"TOTAL REVENUE ={g+e} ")

#MAIN FUNCTION         
def main():
  while True:
    try:
      yee=input("PRESS ACCORDING TO OPERATION : ").upper()
      break
    except ValueError:
      print("PLEASE SELECT RIGHT OPERATION : ") 
  if (yee=="BOOK"):
   book() 
   main()
  elif(yee=="CHECK"):
   check()
   main()
  elif(yee=="CANCEL"):
   cancel()
   main()
  elif(yee=="PRICE"):
   price()
   main()
  else:
   print("SELECT A VALID OPERATION : ")
   main()
main()         
    



