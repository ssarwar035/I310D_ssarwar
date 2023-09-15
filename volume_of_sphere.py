def calculate_volume_of_sphere(radius):
    pi = 3.14
    volume = (4/3) * pi * (radius**3)
    return volume

sphere1 = 30
volume1 = calculate_volume_of_sphere(sphere1)
print(f"The volume of this sphere is", volume1)

sphere2 = 40
volume2 = calculate_volume_of_sphere(sphere2)
print(f"The volume of this sphere is", volume2)