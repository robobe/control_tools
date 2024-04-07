def interpolate(x, x1, x2, y1, y2):
    y_range = y2 - y1
    x_range = x2 - x1
    y = y1 + (x-x1)*(y_range/x_range)
    return y

def interpolate_with_limits(x, x1, x2, y1, y2):
    y = interpolate(x, x1, x2, y1, y2)
    if y<y1:
        return y1
    if y>y2:
        return y2
