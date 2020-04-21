import sys
import string
import itertools

n = int(sys.argv[1])

character_list = string.ascii_letters + string.digits + string.punctuation

products = itertools.product(character_list, repeat = n)

for product in list(products):
  print("".join(product))
