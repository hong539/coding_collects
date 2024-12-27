a = 1
b = 0
try:
    r = a % b
    print(r)
except ValueError:
    print("2")
except Exception:
    print("3")
finally:
    print("4")