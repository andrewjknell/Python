def reverse(list):
   first = 0
   last = len(list)-1
   while first<last:
       temp = list[first]
       list[first] = list[last]
       list[last] = temp
       first += 1
       last -= 1

   return list

print(reverse([1,2,3,4,5]))




   