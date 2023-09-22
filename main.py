passw = "REPLACE BY YOUR OWN PASSWORD !!!"
#passw = input("Passwort eingeben: ")
#
#  Die Nachricht, die ich unterschrieben habe, the message that I signed
#
message = '''
<blockquote class="twitter-tweet"><p lang="de" dir="ltr">💥 
Sahra Wagenknecht ENTHÜLLT! 🧨 
<a href="https://twitter.com/hashtag/NordStream?src=hash&amp;ref_src=twsrc%5Etfw">#NordStream</a>
-Sprengung: GROSSER <a href="https://twitter.com/hashtag/BETRUG?src=hash&amp;ref_src=twsrc%5Etfw">#BETRUG</a>
D... <a href="https://t.co/DoZmAbECBu">https://t.co/DoZmAbECBu</a> via 
<a href="https://twitter.com/YouTube?ref_src=twsrc%5Etfw">@YouTube</a>
<a href="https://twitter.com/hashtag/ichteileundteile?src=hash&amp;ref_src=twsrc%5Etfw">#ichteileundteile</a></p>&mdash;
Franz Scheerer (@twxxfranz) 
<a href="https://twitter.com/twxxfranz/status/1705189242895217017?ref_src=twsrc%5Etfw">September 22, 2023</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Das Fliegen mit geimpften Piloten ist gefährlicher, weil diese Piloten ein höheres Risiko 
für Herzerkrankungen und Schlaganfälle haben.

Nein, keine Verschwörungstheorie sondern Fakt. Einen besseren Beweis könnte es kaum geben.

<blockquote class="twitter-tweet"><p lang="de" dir="ltr">Eine Quelle hier 
:<a href="https://t.co/QQGzuCX7Vj">https://t.co/QQGzuCX7Vj</a></p>&mdash;
Klaus Heimann (@KlausHeimann) 
<a href="https://twitter.com/KlausHeimann/status/1696915024411787335?ref_src=twsrc%5Etfw">August 30, 2023</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Die Schnorrsignatur ist sicher, weil der private Schlüssel x sicher
(One-Time-Pad) verschlüsselt wird.
                         
                         s = k + x*e              (modulo q) 
                         
Nur wenn k sich wiederholt, könnte x berechnet werden. Das ist jedoch 
praktisch  ausgeschlossen. Der Wert von e und damit der Signatur ist 
praktisch für unterschiedliche Nachrichten immer verschieden.

Sonst kann x nur aus der Gleichung

                         y = g ^ x                (modulo q) 

bestimmt werden. Das ist praktisch unmöglich (Logarithmus-Problem).
Die Schnorr-Signatur erfordert KEINE elliptischen Kurven.

Wir können 'e' durch minus 'e' ersetzen. Es macht keinen wesentlichen
Unterschied, aber die Gleichung zur Prüfung der Signatur wird
noch etwas einfacher (ohne Inverse).

                    e := hash (g ^ k, m) = hash(r,m)
                    k einmalige Zufallszahl
                    r  = g ^ k                  (modulo p)
                    (g ^ s) (y ^ e) = g ^ k = r (modulo p)
===================================================================
                         
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">
Ursula von der Leyen is married to the German doctor Heiko von der Leyen… 
who is director of Orgenesis, which is owned by Pfizer… the same company 
that Ursula signed a 71 billion euro contract with to buy an astronomical 
4.6 billion doses (10 per citizen) 
<a href="https://t.co/axny0fDrko">pic.twitter.com/axny0fDrko</a></p>&mdash; 
Pelham (@Resist_05) 
<a href="https://twitter.com/Resist_05/status/1691250933613862912?ref_src=twsrc%5Etfw">August 15, 2023</a>
</blockquote> 
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Hash of public key:  58471779221732556597096814364884027037
Hash of public key:  58471779221732556597096814364884027037 (Vergleichswert Twitter Profile, berechnet)

Mediziner und Wissenschaftler für Gesundheit, Freiheit und Demokratie
---------------------------------------------------------------------
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

Es zeigt, dass EU und WHO abgeschafft werden müssen!
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
     
     Es folgt die Nachricht (message), die von mir unterschrieben wurde,
     ausgehend von meinem Passwort. Diese Signatur wird am Ende überprüft.
     
     Mittels des öffentlichen Schlüssels (y) kann die Signatur geprüft
     werden. Aber nur ich kann die Signatur erstellen, weil dazu mein 
     Passwort benötigt wird.
"""

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


k = h32(passw + message)
r = pow(g,k,p)

e = h16(str(r) + message)
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
SIG =  [139316941845205048378151048476589928526, 3831349419217454965310689182171108305563278497169422727004257448564451137346]

print("Prüfe die Nachricht:\n", message)
print("\nHash of public key ", h16(str(y)))

e = SIG[0]
s = SIG[1]

rv = pow(pow(g,s,p) * pow(y,e,p), 1,  p)
ev = h16(str(rv) + message)

#
# The change, that (ev) is randomly equal to (e) 
# is 1 / 2 ^ {128}
#
assert(ev ==  e)  

print()
print("The signature was verified.")


















































