# Password Card Generator
You need a Keyword for a Password card to work!   

## How it works
To get the password you take one character at a time.  

To get the row: Look in what row your character appears      
To get the column: Look at what position your character is.   

Then you take what is in [column] in [row] and put it on the end of the password   
Do that for every character in your keyword, and you got yourself a secure password

Example:
```
|    | ABC   | DEF   | GHI   | JKL   | MNO   | PQR   | STU   | VWX   | ZY   | .   |
|----|-------|-------|-------|-------|-------|-------|-------|-------|------|-----|
|  1 | 3T,   | 2C8   | 2lk   | ZMJ   | br]   | sPj   | ,X1   | ZMq   | IAp  | LPG |
|  2 | h2R   | ?XH   | wng   | UkQ   | 7}g   | }'j   | TBg   | hC3   | Hub  | ?pA |
|  3 | GSI   | r0z   | rtm   | n9N   | OID   | B6T   | noV   | P9n   | g,k  | ZRU |
|  4 | wVc   | 1'?   | K6N   | kc%   | EY}   | ]8K   | ImI   | '[Z   | Mv;  | cd1 |
|  5 | nz#   | h}a   | pX6   | ?1;   | D89   | F39   | rDU   | 3l8   | n7T  | 9Qq |
|  6 | U4x   | H[j   | ?Fe   | tJi   | Q.d   | T!6   | .rx   | _'s   | YVh  | q_' |
|  7 | Jyi   | hyN   | 73{   | {73   | Wez   | %{C   | IJ}   | QVm   | ipj  | YK, |
|  8 | LlX   | fYO   | YUg   | !ne   | 1n{   | H{\   | 9_F   | !?!   | rbx  | b#a |
```
Our keyword is: VerySafe

So we look in what row does V, the first letter, appear in -> row VWX     
Now we look at what position the V (the first letter) is -> 1

So we append the 3 characters that are in row VWX at 1 (ZMq)     
Our password right now is: ZMq

And repeat!

so we look in what row e, the second letter, does appear in -> row DEF        
now we look at what position the e, the second letter, is -> 2      

so we append the 3 characters that are in row DEF at 2 (?XH)        
Our password right now is: ZMq?XH     
...   
...    
Our password right now is: ZMq?XHB6TMv;rDUU4xhyNfYO    
