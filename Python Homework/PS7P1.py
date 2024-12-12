loop=(input("Y if you would like to loop "))
while loop =="Y":
  p = float(input("Enter the principal amount: "))
  r = float(input("Enter the annual interest rate: "))
  total_i=0
  print("\n Year ", "Beginning Balance ", "Ending Balance")
  for y in range (1,6,1):
    i = p * r
    eb = p + i
    print("\n", y,"   ${:.2F}".format(p), "   ${:.2F}".format(eb))
    p = eb
    total_i = total_i + i
  print("\n Total interest earned: ", "{:.2F}".format(total_i))
  loop = (input("Y if you would like to loop "))