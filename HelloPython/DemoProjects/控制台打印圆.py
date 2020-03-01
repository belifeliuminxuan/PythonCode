R = 100
for i in range(2 * R + 1):
   ban = int((R ** 2 - (R - i) ** 2) ** 0.5)
   start = round(R - ban)
   midnum_ = round(2 * ban)  
   print(' ' * start + '*' +' ' * midnum_ + '*')