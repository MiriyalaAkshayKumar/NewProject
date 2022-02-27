print("Painting the wall")

height = int(input("Please enter height of the wall: "))
width = int(input("Please enter width of the wall: "))
coverage = 5
number_of_cans=0
def cal_area(height,width):
    number_of_cans=height*width / 5
    print(f"Number of cans required: {float(number_of_cans)}")

cal_area(height,width)

