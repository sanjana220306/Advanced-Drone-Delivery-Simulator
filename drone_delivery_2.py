import math

print("🚁 DRONE DELIVERY SIMULATOR 🚁")
print("----------------------------------")

# Base location
base_x = 0
base_y = 0

# Drone settings
battery = 100  # battery percentage
speed = 60     # km per hour (normal speed)

# User input
start_x = float(input("Enter start X coordinate: "))
start_y = float(input("Enter start Y coordinate: "))

dest_x = float(input("Enter destination X coordinate: "))
dest_y = float(input("Enter destination Y coordinate: "))

weather = input("Enter weather (clear/rain/windy): ").lower()

# Weather impact
if weather == "rain":
    speed *= 0.7
elif weather == "windy":
    speed *= 0.8
elif weather == "clear":
    pass
else:
    print("Unknown weather condition. Assuming clear.")

# Distance calculation
distance = math.sqrt((dest_x - start_x)**2 + (dest_y - start_y)**2)

# Battery usage (1% per km)
battery_used = distance
battery -= battery_used

# Time calculation
if speed > 0:
    time = distance / speed
else:
    time = 0

print("\n📊 DELIVERY REPORT")
print("----------------------")
print(f"Distance to destination: {distance:.2f} km")
print(f"Estimated time: {time:.2f} hours")
print(f"Battery remaining: {battery:.2f}%")

# Battery safety check
if battery < 20:
    print("\n⚠ Battery too low! Returning to base...")
    
    return_distance = math.sqrt((dest_x - base_x)**2 + (dest_y - base_y)**2)
    return_time = return_distance / speed
    
    print(f"Return distance: {return_distance:.2f} km")
    print(f"Return time: {return_time:.2f} hours")
else:
    print("\n✅ Delivery Successful!")
input("Press Enter to exit...")