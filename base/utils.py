import math


# def find_distance_between_clock_hands(A, B, H, M):
#     hour_angle = (H % 12 + M / 60) * 360 / 12
#     minute_angle = M * 360 / 60
#     angle_difference = abs(hour_angle * 60 - minute_angle)
#     angle_difference = angle_difference * (math.pi / 180)
#     distance = (A ** 2 + B ** 2 - 2 * A * B * (angle_difference / 2).cos()) ** 0.5
#
#     return distance
#
#
# with open("input.txt", "r") as file:
#     A, B, H, M = map(int, file.readline().split())
# result = find_distance_between_clock_hands(A, B, H, M)
# print(result)


def distance_between_shafts(A, B, H, M):
    hour = (H * 2 * math.pi) / 12
    minute = (M * 2 * math.pi) / 60
    cos_hour = A * math.cos(hour)
    sin_hour = A * math.sin(hour)
    cos_minute = B * math.cos(minute)
    sin_minute = B * math.sin(minute)
    d = math.sqrt((cos_minute - cos_hour) ** 2 + (sin_minute - sin_hour) ** 2)
    return d


# Given values
A = 3  # Hour axis in cm
B = 4  # Minute axis in cm
H = 0  # Hour hand position (0 corresponds to 12 o'clock)
M = 15  # Minute hand position (15 corresponds to 3 o'clock)

# Calculate distance between shafts
result = distance_between_shafts(A, B, H, M)
# print("Distance between the ends of the hour and minute shafts:", result, "cm")
print(round(result))
