num_books = int(input("Number of books: "))
cost_per_book = float(input("Cost per book: "))
total = num_books * cost_per_book
shipping = 0 if total > 50 else 25
print(f"Order Total: ${total:.2f}")
print(f"Shipping Charge: ${shipping:.2f}")