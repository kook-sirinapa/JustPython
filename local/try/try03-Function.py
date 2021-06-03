def get_box_area_print(width, length, height):
    box_area = width * length * height
    print(box_area)

get_box_area_print(4, 4, 2)
get_box_area_print(1, 1, 1)

"""Function get box area  with validation w l h > 0
    """
def get_box_area_return(width, length, height):
    if width < 0 or length < 0 or height <0:
        return 0
    box_area = width * length * height
    return box_area

box1= get_box_area_return(-4, 4, 2)
box2= get_box_area_return(5, 5, 5)
print(box1, box2)