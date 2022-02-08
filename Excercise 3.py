building_type = input("What is the building type? \n"
                      "('1' for commercial and '2' for residential) : ")
length = input("What is the length (in metres): ")
width = input("What is the width (in metres): ")

VOLUME = eval(f"{length}*{width}*{depth}")

if building_type == 1:
    depth = 0.5
else:
    depth = 0.25

print(f"Total volume of concrete needed is {VOLUME}")
