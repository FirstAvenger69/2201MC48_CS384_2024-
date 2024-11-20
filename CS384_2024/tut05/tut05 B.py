def main():

  par = input("Enter the string: ")

  f = True

  Emp = []

  for i in par:

    if (i == '(' or i == '{' or i == '['):
      Emp.append(i)

    elif(i == ')'):
      if Emp[-1] == '(':
        Emp.pop()

      else:
        f = False
        break

    elif(i == '}'):
      if Emp[-1] == '{':
        Emp.pop()

      else:
        f = False
        break

    elif(i == ']'):
      if Emp[-1] == '[':
        Emp.pop()

      else:
        f = False
        break

  if(f and not len(Emp)):

    print("IT IS BALANCED")

  else:

    print("NOT BALANCED")

main()