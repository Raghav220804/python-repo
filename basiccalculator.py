operation = int(input("Select operation : \n"
                      "1.Add \n"
                      "2.Subtract\n"
                      "3.Multiply\n"
                      "4.Divide\n"))

if operation == 1:
      num1 = input("Enter a number : ")
      num2 = input("Enter another number : ")
      a = float(num1) + float(num2)
      print("Sum = ", a)
elif operation == 2:
      num1 = input("Enter a number : ")
      num2 = input("Enter another number : ")
      c = float(num1) - float(num2)
      print("Difference" , c)
elif operation == 3:
      num1 = input("Enter a number : ")
      num2 = input("Enter another number : ")
      b = float(num1) * float(num2)
      print("Product = ",b )
elif operation == 4:
      num1 = input("Enter a number : ")
      num2 = input("Enter another number : ")
      d = float(num1)/float(num2)
      print("Quotient = ",d)







