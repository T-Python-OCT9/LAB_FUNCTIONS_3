
Hr = int(input("Enter highr number "))
Lor = int(input("Enter lower number "))
def is_prime(a):
    return all(a % i 
    for i in range(2, a))
prime = []
for i in range(Lor, Hr):
  if is_prime(i):
    prime .append(i)
print(prime)