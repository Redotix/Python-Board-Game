# Simple function to add a 0.5 to both members of a coordinate tuple.
def offsettocenter(coordinate):

    coordinate = (float(coordinate[0]) + 0.5, float(coordinate[1]) + 0.5)
    return coordinate
