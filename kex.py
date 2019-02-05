import sys, math, hashlib, random, time

# must be of the form 4k + 3 = 4(k+1) - 1
 
def bin2num(x):
  res = 0
  for c in x:
    res = (res<<8) ^ ord(c)
  return res

def num2bin(x):
  res = ''
  while x > 0:
    res = chr(x % 256) + res
    x /= 256
  return res

#prime = nextPrime(115 * 2**160)
prime = 2**160 * 115 + 86427

a = prime - 31
b = 0
c = 17

def inv(b,m):
  s = 0
  t = 1
  a = m
  while b != 1:
    q = a/b
    aa = b
    b = a % b
    a = aa
    ss = t
    t = s - q*t
    s = ss
  if t < 0:
    t = t + m
  return t


def genP(x,a,b):
   if (4*a*a*a + 27*b*b) % prime == 0:
      b = b + 1
   while pow(c*x**3 + a*x + b, (prime - 1)/2, prime) != 1:
     x = x + 1
   y = pow(c*x**3 + a*x + b, (prime + 1)/4, prime)
   return [x % prime, (y) % prime]

def dpoint(P):
  x = P[0]
  y = P[1] 
  s = ((3*c*(x**2) + a) * inv(2*y, prime)) % prime
  xr = (cinv*s**2 - 2*x) % prime
  yr = (-y + s * (x-xr)) % prime
  return [xr , yr]

def addP(P,Q):
  if P == Q:
    return dpoint(P)
  x1 = P[0]
  x2 = Q[0]
  y1 = P[1] 
  y2 = Q[1] 
  while x1 < x2:
     x1 = x1 + prime
  while y1 < y2:
     y1 = y1 + prime
  s = ((y1-y2) * inv(x1-x2, prime)) % prime
  xr = cinv*s**2 - x1 - x2
  yr = s * (x1-xr) - y1 
  return [xr % prime, yr % prime]

def mulP(P,n):
  isFirst = True
  resP = P
  if n < 0:
    resP[1] = prime - resP[1]
    n = (-1)*n 
  bsize = 20
  while 2**bsize < n:
     bsize = bsize + 1
  PP = resP
  for b in range(bsize + 1):
     if (n & (1 << b) != 0):   
         if isFirst:
            resP = PP
            isFirst = False
         else:
            resP = addP(resP,PP)
     PP = dpoint(PP) 
  return resP

cinv = inv(c, prime)
P = genP(a+17,a,b)
P = mulP(P,4)

message = "message160"

k = 347358457457843758345789434783457
number = bin2num(message)
print "Message converted to a number: \n", number
x = number
if pow (c*x**3 + a*x, (prime-1)/2, prime) != 1:
   x = prime - x

P_0 = [x, pow (c*x**3 + a*x, (prime+1)/4, prime)]

E_Alice = mulP(P_0, k)

print "\nEncrypted point is sent to Alice: \n", E_Alice

kk = 7678688789789789

E_Bob = mulP(E_Alice, kk)
print "\nDecrypted Point\n", E_Bob

D1 = mulP(E_Bob, inv(k, prime+1))
print "\nSingle encrypted point is send to Alice: \n", D1

mm = mulP(D1, inv(kk, prime+1))[0]
if mm > (prime)/2:
   mm = prime - mm
mm = num2bin(mm)
print "\nEncrypred by Alice: ", mm

print "Does it work, is mm = message? ", mm == message
