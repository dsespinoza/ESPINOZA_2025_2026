import math
gravity= 9.8
degrees= int(input("Enter launch angle (degrees): "))
distance= int(input("Enter maximum distance (meters): "))
radians=(math.radians(degrees))
r=radians*2
sin=(math.sin(r))
initial_velocity= (math.sqrt(distance*gravity/sin))
z=round(initial_velocity, 2)
print(f"Required launch speed: {z} m/s")