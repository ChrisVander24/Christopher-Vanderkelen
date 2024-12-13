def calculate_mpg(miles, gallons):
  if gallons == 0:
    return 0
  return miles / gallons

def main()
while True:
    destination = input("Enter destination city (or 'done' to stop): ")
    if destination.lower() == 'done':
        break
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))
    mpg = calculate_mpg(miles, gallons)
    print(f"{destination}: {miles} miles, {mpg:.2f} MPG")
    trips_count += 1
print(f"Total trips: {trips_count}")