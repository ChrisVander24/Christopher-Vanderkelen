def calculate_price(num_tickets):
  if num_tickets >= 25:
      price_per_ticket = 50
  elif num_tickets >= 10:
      price_per_ticket = 60
  elif num_tickets >= 5:
      price_per_ticket = 70
  else:
      price_per_ticket = 75

  total_cost = num_tickets * price_per_ticket
  return price_per_ticket, total_cost

num_tickets = int(input())

if num_tickets >= 0:
  price_per_ticket, total_cost = calculate_price(num_tickets)
  print(f"{num_tickets} {price_per_ticket} {total_cost}")