try: #kod kotoriy vivodit oshibki
    num1 = int(input("vvedi pervoe chislo"))
    num2 = int(input("vvdedi vtoroe chislo"))
    print("num1/num2 =", num1/num2)

except ZeroDivisionError:
    print("na nol delit nelzya!")

except ValueError:
    print("vi vveli ne cisla")

except Exception:
    print("xz chto za oshibka")

else :
    print("vse okey")

finally:
    print("ya tut")