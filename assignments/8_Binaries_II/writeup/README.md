# Extra Credit Writeup - Binaries II

Name: Robert Nash
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Robert Nash

## Assignment Writeup

### Part 1 (100 Pts)

This assignment was pretty easy once I was able to load it into Ghidra. Once the binary in analyzed we go to the functions menu and select the `main` function. 

![](/Users/robertnash/Desktop/ghidra.png)

To the left, we can see Ghidra does a great job decompiling the code and that the program simply takes in an argument (the flag) and checks each character to make sure it matches. The first few characters are straight forward. The other checks are a little more intuitive.

First we know from line 8 that our flag must be 29 characters in length. So let's check them.

**Characters 1-12**
These are straightforward and are directly checked to make sure they equal the following:
`CMSC389R-{0n`
This looks like a flag so we are on the right track.

**13**
This checks that the input, when the bits are shifted 4 to the left, equals `0x33`. `0x33` shifted to the right is `3`

Our flag is now `CMSC389R-{0n3`

**14-15**
These are direct and check for `_s`

Our flag is now `CMSC389R-{0n3_s`

**16**
This says take the input at position 16 and subtract the value of 15 and that should equal 1. In other words one ascii letter about whatever was at 15 which is `s` so position 16 is `t`.

Our flag is now `CMSC389R-{0n3_st`

**17**
This says position 17 is the same as 10 which was `0`.

Our flag is now `CMSC389R-{0n3_st0`

**18**

18 is the same character as 10 but added 0x40. Checking an ASCII table gives us `p`.

Our flag is now `CMSC389R-{0n3_st0p`

**19**

This is the same as position 0xd which is `_`

Our flag is now `CMSC389R-{0n3_st0p_`

**20**
 This is compared to `l`
 
 Our flag is now `CMSC389R-{0n3_st0p_l`
 
 **21**
 This again is the same as position 10.
 
 Our flag is now `CMSC389R-{0n3_st0p_l0`
 
 **22**
 #22 is saying that its input plus 9 should be equal to the character at 13. Therefore we take the hex for ascii character 3 and subract 9.
 
 Our flag is now `CMSC389R-{0n3_st0p_l0c`
 
 **23**
The 23rd character is simply `K`

Our flag is now `CMSC389R-{0n3_st0p_l0cK`

**24-25**
The 24th character is the same as character `0xd` which is `_` and 25 is `s`

Our flag is now `CMSC389R-{0n3_st0p_l0cK_s`

**26-27**
This character is the same as character `0x13` minus 4 on the ASCII table.

We look this up and get `t`. 27 is the same as character `0x14`.

Our flag is now `CMSC389R-{0n3_st0p_l0cK_st0`

**28-29**

28 is compared to ASCII `0x50`. And our last character is `}`

Our flag is now `CMSC389R-{0n3_st0p_l0cK_st0P}`

**

![](/Users/robertnash/Desktop/flag.png)
    
