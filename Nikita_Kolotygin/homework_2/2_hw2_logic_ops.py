import math
# 2TRUE + 2FALSE
fir = 1
sec = 9
print(bool(fir+sec>9 and fir>0))
print(bool(math.sqrt(sec) and math.sqrt(fir)))

print(bool(fir+5>0 and sec-5<0))
print(bool(fir != sec/sec) and sec != fir/fir)

print(bool(sec == 9 or fir == 9))
print(bool(sec>1 or fir>sec))
print(bool(fir == sec-fir or sec == math.sqrt(sec)))
print(bool(fir == sec or sec == 1))

#strings
print(bool("Alphabet" and None))