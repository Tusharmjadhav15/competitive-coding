x = [32,15,22,35,45,69,41]

#mean
m = sum(x)
mean = m/len(x)
print("mean:",mean)

#median
t = int(len(x)//2)
print("median:",x[t-1])


#mode
from collections import Counter
  
# list of elements to calculate mode
n_num = [1, 2, 3, 4, 5, 5]
n = len(n_num)
  
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is : " + ', '.join(map(str, mode))
      
print(get_mode)