import sys
import math

def randomEquation(x):
  return math.log(7.0 - x)

def fpi2(func, x0, tol, maxIter):
  iter = 0

  curr = x0
  upper_bound = float("inf")
  lower_bound = float("-inf")

  print(str(iter) + ": (" + str(lower_bound) + ", " + str(upper_bound) + ")")
  iter = iter + 1

  while((upper_bound - lower_bound > tol) and (iter < maxIter)):
    prev = curr
    curr = func(prev)
    if(curr == prev): # special case: x0 is a fixed point
      return curr
    elif(curr < prev):
      midpoint = (curr + prev) / 2.0
      if(midpoint < upper_bound):
        upper_bound = midpoint
    elif(curr > prev):
      midpoint = (curr + prev) / 2.0
      if(midpoint > lower_bound):
        lower_bound = midpoint
    print(str(iter) + ": (" + str(lower_bound) + ", " + str(upper_bound) + ")")
    iter = iter + 1

  return (lower_bound + upper_bound) / 2.0


def main():
  print("fpi2")
  r2 = fpi2(randomEquation, -4.0, 0.0000000001, 1000)
  print("r2: " + str(r2))

if __name__ == "__main__":
  main()
