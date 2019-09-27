#  By Scout Crooke, 9/25/29, this program works on daily function exercises


def make_hexagon_top():
    print("  ________")
    print(" /        \\")
    print("/          \\")


def make_haxagon_bottom():
    print("\\          /")
    print(" \\________/") \



def make_punctuation():
    print(" _\"_\'_\"_\'_\"_")


make_hexagon_top()
make_haxagon_bottom()
make_punctuation()
make_hexagon_top()
make_haxagon_bottom()
make_punctuation()
make_haxagon_bottom()
make_hexagon_top()
make_punctuation()
make_haxagon_bottom()


def happy_bd_ty():
    print("Happy Birthday to you")


def happy_bd_db(name):
    print("Happy Birthday dear", name)


for x in range(2):
    happy_bd_ty()

happy_bd_db("Brian")
happy_bd_ty()


def plus(x, y):
    print(x, "+", y, "=", x + y)


def main():
    plus(8, 9)
    plus(6, 5)
    plus(2, 4)


main()
