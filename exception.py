# exception number

#queen = int(input ("what's your fav number ?\n"))
#print(queen)

while True:
    try:
        number = int(input("what's your fav number ?\n"))
        print(25/number)
        break
    except ValueError:
        print("make sure and enter a number.\n")
    except ZeroDivisionError:
        print("Don't pick Zero.\n")
    except:
        break
    finally:
        print("Loop Complete ")




