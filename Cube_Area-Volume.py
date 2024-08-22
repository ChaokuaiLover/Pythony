MODE = int(input("Area mode put 0 Volume mode put 1: "))
if MODE == 0:
    def area(width,length):
        a = width * length
        return a
    Area_wid = float(input("Putting the width: "))
    Area_len = float(input("Putting the length: "))
    print("The area is" ,area(Area_wid,Area_len))
elif MODE == 1:
    def volume(width,length,height):
        a = width * length * height
        return a
    Vol_wid = float(input("p utting the width: "))
    Vol_len = float(input("putting the length: "))
    Vol_hei = float(input("putting the height: "))

    print("The volume is" ,volume(Vol_wid,Vol_len,Vol_hei))
else:
    print('ERROR')