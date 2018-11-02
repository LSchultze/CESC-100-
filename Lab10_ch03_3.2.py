rectangle1_L = input("Enter rectangle 1's length.")
rectangle1_W = input("Enter rectangle 1's width.")
rectangle2_L = input("Enter rectangle 2's length.")
rectangle2_W = input("Enter rectangle 2's width.")
rectangle1_L = int(rectangle1_L)
rectangle1_W = int(rectangle1_W)
rectangle2_L = int(rectangle2_L)
rectangle2_W = int(rectangle2_W)
rectangle1_area = rectangle1_L*rectangle1_W
rectangle2_area = rectangle2_L*rectangle2_W
if rectangle1_area > rectangle2_area:
    print("The first rectangle has a greater area than the second.")
elif rectangle1_area < rectangle2_area:
    print("The second rectangle has a greater area than the first.")
else:
    print("The rectangles have the same area!")