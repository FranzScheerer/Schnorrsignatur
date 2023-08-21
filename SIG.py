"""
     All cryptography is basically trivial. We do not need any
     US standards, usually developed by the Secret Service.
     
     We can do everything ourselves. I did everything myself. Here
     is the result. A hash function and the digital signature.
     
     Below is the message, digitally signed by me,
     based on my password. This signature is verified at the end.
     
     The signature can be checked using the public key (y).
     But only I can create the signature, because my password is required.

     Die gesamte Krypthographie ist im Grunde trivial. Wir brauchen keine
     US-amerikanischen Standards, in der Regel vom Geheimdienst entwickelt.
     
     Wir können alles selber machen. Ich habe alles selber gemacht. Hier
     ist das Ergebnis. Eine Hashfunktion und die digitale Signatur.
     
     Es folgt die Nachricht, die digital von mir unterschrieben wurde,
     ausgehend von meinem Passwort. Diese Signatur wird am Ende überprüft.
     
     Mittels des öffentlichen Schlüssels (y) kann die Signatur geprüft
     werden. Aber nur ich kann die Signatur erstellen, weil dazu mein 
     Passwort benötigt wird.
"""

passw = "REPLACE BY YOUR OWN PASSWORD !!!"
passw = input("Passwort eingeben: ")     
msg = '''

Es ist ja wahrlich nicht allein Bhakdi. In seinem Verein MWGFD
und in vielen anderen Organisation haben sich weltweit zehntausende
Ärzte, Wissenschaftler und auch Juristen zusammengeschlossen, 
die gemeinsam vor den Gefahren der Impfung warnen und die Verbrechen
zur Anklage bringen.

ZEHN - MEHR BRAUCHEN WIR NICHT ZU WISSEN!

Wer es vor zwei Jahren Telegram nicht geglaubt hat, glaubt es 
vielleicht jetzt der ARD.

#UrsulavonderLeyen hat unter Umgehung
aller Regeln für jeden EU-Bürger 10 Impfdosen bei 
Pfizer bestellt: https://pic.twitter.com/ijnRRS8xmp

In Worten ZEHN - der helle Wahnsinn !!!

Aber natürlich kann es auch nicht sein, dass eine 
einzelne Person alleine über derartige Summen entscheidet.

Es zeigt, dass die EU abgeschafft werden MUSS!

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Aggressive ‘Turbo Cancers” in Young People Linked to Immune-Suppressing Shots, Says Dr. Ryan Cole<br><br>“A colleague [breast pathologist] of mine in Sweden ... noticed young women developing cancer after the rollout of the injections, and she noticed that these cancers were more… <a href="https://t.co/aceSAkJ4IB">pic.twitter.com/aceSAkJ4IB</a></p>&mdash; The Vigilant Fox 🦊 (@VigilantFox) <a href="https://twitter.com/VigilantFox/status/1693295527150977486?ref_src=twsrc%5Etfw">August 20, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
========================================================
import sys
import hashlib
import base64

if len(sys.argv) > 1:
  pw = sys.argv[1]
  if len(sys.argv) > 2:     
   f = open('in', 'rb')
   x = list(base64.a85decode(f.read()))
  else:
   f = open('in', 'rb')
   x = list(f.read())
  f.close()
  cnt = len(x) - 1
  md = hashlib.sha3_256(pw.encode())
  ix = 0
  while (cnt >= 0):
     if ix == 0:
        bs = md.digest()
        md.update('#'.encode())
     if len(sys.argv) > 2:    
        md.update(str(x[cnt]).encode())
     x[cnt] = x[cnt] ^ bs[ix]
     if len(sys.argv) == 2:    
        md.update(str(x[cnt]).encode())
     cnt = cnt - 1
     ix = (ix + 1) % len(bs)
  f = open('out', 'wb')
  if len(sys.argv) == 2:     
    f.write(base64.a85encode(bytes(x)))
  else:
    f.write(bytes(x))
  f.close()
else:
  print("Das Passwort wurde nicht angegeben")

'''

class HASH:
  def update(H):
    H.i = (H.i + H.w) % 256
    H.j = H.s[(H.j + H.s[H.i]) % 256]
    H.s[H.i], H.s[H.j] = H.s[H.j], H.s[H.i]

  def shuffle(H):
    for v in range(256):
        HASH.update(H)    
    H.w = (H.w + 2) % 256
    H.a = 0

  def absorb_nibble(H,x):
    if H.a == 240:
        HASH.shuffle(H)
    H.s[H.a], H.s[240 + x] = H.s[240 + x], H.s[H.a]
    H.a = H.a + 1

  def absorb_byte(H,b):
    HASH.absorb_nibble(H, b % 16)
    HASH.absorb_nibble(H, b >> 4)

  def h(H, msg, outlen):
    H.s = list(range(256))   
    H.a = H.i = H.j = 0
    H.w = 1
    for c in msg.encode():
       HASH.absorb_byte(H,c)
    HASH.shuffle(H)
    HASH.shuffle(H)
    HASH.shuffle(H)
    out = 0
    for v in range(outlen):
        HASH.update(H)
        out = (out << 8) + H.s[H.j]
    return out   

# hash128
def h16(x):
  ha = HASH()
  return HASH.h(ha,x,16)     
# hash256
def h32(x):
  ha = HASH()
  return HASH.h(ha,x,32)     

# The greatest common divisor
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a 
#
# The primes as used for the Digital Signature Algorithm (DSA),
# the Schnorr Signature or the key exchange (DH) or other applications. 
# They can be calculated pseudo random from a password.
# Primes can be found of any disired size.
# 
# bitlenP = 384 
# bitlenQ = 256
# It's enough!
#

def genPrimes(password):
   m = 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31
   h = 2 * m   # to ensure that (h*q + 1) is odd 
   while h < (1<<128):
      h = h * 2 
   # To ensure that that q is odd.
   q = 2 * h32(password) + 1

   while True:
       q = q + 2           # next odd number
       if gcd(q,m) != 1:   # divisable by a prime smaller or equal 31
          continue
       if pow(17,q-1,q) != 1: # Prime test by Fermat for q
          continue
       p = h*q + 1           # p-1 = h*q  
       if pow(7,p-1,p) != 1: # Prime test for p
          continue
       break
   return [p, q]

pq = genPrimes("This is my password") 
p = pq[0]
q = pq[1]
h = (p-1)//q
print("Length of prime numbers (decimal digits) ", len(str(p)), ',', len(str(q)))
# The generator aof a groupt of order q.
g = pow(2, h, p)
# Printout of generated code
print('g = ', g)
print('p = ', p)
print('q = ', q)

assert( pow(g,q,p) == 1 )
assert( pow(23,q-1,q) == 1 )
assert( pow(17,p-1,p) == 1 )

# The private key
x = h32(passw)

# The public key
y = pow(g, x, p)
print("y = ", y)


k = h32(passw + msg)
r = pow(g,k,p)

e = h16(str(r) + msg)
s = pow(k - x*e, 1, q) 
SIG = [e,s]
print("SIG = ", SIG)


'''
  ===============================    ============================================= ==============
  ===============================    ============================================= ==============
                   The following part of the script may be
                   copied to a separate file for verfication. 
    
                   Copy the generated code below the lines:
  ===============================    ============================================= ==============
  ===============================    ============================================= ==============
'''

y =  647399072525100553937688981621020711554556370403311549380461996737655671772678615352957137074732654942878578698034
SIG =  [333381963029089246886381176434121640678, 5156981185539256487613493797546953655858987582948691114087245820529778803122]
print("Prüfe die Nachricht:\n", msg)
e = SIG[0]
s = SIG[1]

rv = pow(pow(g,s,p) * pow(y,e,p), 1,  p)
ev = h16(str(rv) + msg)
assert(ev ==  e)  

print()
print("The signature was verified.")





















































