import math


def hl2rgb(l, a, b):

    # Hunter L a b to XYZ values
    # Enter reference values of Hunter L a b equipment provided. If not, you will get a different calibrated color value

    refX = 84.26
    refY = 89.24
    refZ = 95.29

    var_Ka = (175.0 / 198.04) * (refY + refX)
    var_Kb = (70.0 / 218.11) * (refY + refZ)

    Y = ((l / refY) ** 2) * 100.00
    X = (a / var_Ka * math.sqrt(Y / refY) + (Y / refY)) * refX
    Z = - (b / var_Kb * math.sqrt(Y / refY) - (Y / refY)) * refZ

    print("X:", X, "Y:", Y, "Z:", Z)

    # XYZ to RGB values

    var_X = X / 100
    var_Y = Y / 100
    var_Z = Z / 100
    var_R = var_X * 3.2406 + var_Y * -1.5372 + var_Z * -0.4986
    var_G = var_X * -0.9689 + var_Y * 1.8758 + var_Z * 0.0415
    var_B = var_X * 0.0557 + var_Y * -0.2040 + var_Z * 1.0570

    if var_R > 0.0031308:
        var_R = 1.055 * (var_R ** (1 / 2.4)) - 0.055
    elif var_R <= 0.0031308:
        var_R = 12.92 * var_R
    if var_G > 0.0031308:
        var_G = 1.055 * ( var_G ** (1 / 2.4 )) - 0.055
    elif var_G <= 0.0031308:
        var_G = 12.92 * var_G
    if var_B > 0.0031308:
        var_B = 1.055 * ( var_B ** (1 / 2.4 )) - 0.055
    elif var_B <= 0.0031308:
        var_B = 12.92 * var_B

    sR = round((var_R * 255), 0)
    sG = round((var_G * 255), 0)
    sB = round((var_B * 255), 0)

    print("R:", sR, "G:", sG, "B:", sB)

hl2rgb(63.37, -1.78, 4.38)  # enter you Hunter Lab values in the function. The ones provided are just an example of a gray color




