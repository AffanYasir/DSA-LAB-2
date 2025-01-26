import math

num1, num2 = 12, 15
gcd = math.gcd(num1, num2)
lcm = (num1 * num2) // gcd
print("GCD:", gcd)
print("LCM:", lcm)
