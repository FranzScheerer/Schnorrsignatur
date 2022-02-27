/* The current date and time are Sat Feb 12 15:07:12 2022
 */

#include <time.h>
#include <stdio.h>
#include <string.h>

#define N 256
#define ROUNDS 3
 
int main(int argn, char** argv)
{
    int ii;

    int s[N], s_[N];
    int klen,t,i,j=0;
    int i2,j2;
    int r, c;
    unsigned char cout;

  if (argn != 2){
    fprintf(stderr, "decrypt: cat efile | ./a.out password  > file\n");
    return 0;
  }
  klen = strlen(argv[1]);
  for (i=0; i<N; i++){
      s[i] = (i + klen) % N;
      s_[i] = i;
  }
  for (r=0; r < ROUNDS; r++)
  {
    for (i=0;i<N; i++){
      j = (j + s[i] + argv[1][i % klen]) % N;
      t = s[i] + s[j];
      s[i] = t - s[i];
      s[j] = t - s[j];
    }
  }
  for (r=0; r < ROUNDS; r++)
  {
    for (i=0;i<N; i++){
      j = (j + s_[i] + argv[1][(i+r) % klen]) % N;
      t = s_[i] + s_[j];
      s_[i] = t - s_[i];
      s_[j] = t - s_[j];
    }
  }
  i = klen;
  j = klen;
  i2 = s[2];
  j2 = s[N-1];

  while ((c = fgetc(stdin)) != -1){
    i = (i + 1) % N;
    j = (j + s[i]) % N;
    i2 = (i2 + s[j]) % N;
    j2 = (j2 + s[i2]) % N;
    t = s_[i] + s_[j];
    s_[i] = t - s_[i];
    s_[j] = t - s_[j];
    t = s[i2] + s[j2];
    s[i2] = t - s[i2];
    s[j2] = t - s[j2];
    cout = c ^ s_[s[t % N]];
    j ^= c; 
    printf("%c", cout);    
  }
  for (r=0;r<32;r++){
    i = (i + 1) % N;
    j = (j + s[i]) % N;
    i2 = (i2 + s[j]) % N;
    j2 = (j2 + s[i2]) % N;
    t = s[i2] + s[j2];
    s[i2] = t - s[i2];
    s[j2] = t - s[j2];
    cout = c ^ s_[s[t % N]];
    fprintf(stderr, "%02x", cout);    
  }
  fprintf(stderr, "\n");    

}
 
