import itertools

# Function to calculate the total distance of a tour
def calculate_total_distance(tour, distances):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    total_distance += distances[tour[-1]][tour[0]]  # Return to the starting city
    return total_distance

# the number of cities
num_cities = int(input("Enter the number of cities: "))

# distances matrix
distances = []
print("Enter distances between cities (separate values by space):")
for i in range(num_cities):
    row = [int(x) for x in input().split()]
    distances.append(row)

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    shortest_tour = None
    shortest_distance = float('inf')

    for tour in itertools.permutations(cities):
        tour_distance = calculate_total_distance(tour, distances)
        if tour_distance < shortest_distance:
            shortest_distance = tour_distance
            shortest_tour = tour

    return shortest_tour, shortest_distance
shortest_tour, shortest_distance = traveling_salesman_bruteforce(distances)

print("Shortest Tour:", shortest_tour)
print("Shortest Distance:", shortest_distance)
