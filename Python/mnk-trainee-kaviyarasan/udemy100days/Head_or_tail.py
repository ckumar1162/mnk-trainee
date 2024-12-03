

import random

ramdom_num = random.random()*10
print(ramdom_num)

random_int = random.randint(1,20)
print(random_int)

random_float = random.uniform(1,5)
print(random_float)

random_int_h_t = random.randint(0,1)
if random_int_h_t == 1:
    print("head")
else:
    print("tail")