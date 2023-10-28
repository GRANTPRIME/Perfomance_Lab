import sys
import math

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        center_x, center_y = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return center_x, center_y, radius

def read_points(file_path):
    with open(file_path, 'r') as file:
        points = []
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def point_position(center_x, center_y, radius, point):
    distance = math.sqrt((point[0] - center_x) ** 2 + (point[1] - center_y) ** 2)
    if math.isclose(distance, radius, rel_tol=1e-9):
        return "0 - точка лежит на окружности"
    elif distance < radius:
        return "1 - точка внутри"
    else:
        return "2 - точка снаружи"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python circle_point_position.py <circle_file> <points_file>")
    else:
        circle_file = sys.argv[1]
        points_file = sys.argv[2]

        center_x, center_y, radius = read_circle_data(circle_file)
        points = read_points(points_file)

        for point in points:
            position = point_position(center_x, center_y, radius, point)
            print(position)
