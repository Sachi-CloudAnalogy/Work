#generate password of length 10

from random import sample
import string

value = string.ascii_letters + string.digits +string.punctuation  #[a-z,A-Z,0-9,all symbols]
length = 10
sequence = sample(value, length)   #return list of given length of random choosen values from a sequence
str = ""
for i in sequence:
    str += i

print(str)
