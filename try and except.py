num=4

try:
    sum = num/0

except NameError:
    print("Variable is not defined.")
except ZeroDivisionError:
    print("Dividing by zero error")
else:
    print("success")

finally:
    print("progrsm executed")