# Writeup 7 - Binaries I

Name: Robert Nash
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Robert Nash

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*

```c

printf("

#include<stdio.h>

int main () {
	int b = 0x1ceb00da;
	int a = 0xfeedface;

	printf("a = %d\n", a);
	printf("b = %d\n", b);

	a = a ^ b;

	b = b ^ a;

	a = a ^ b;

	printf("a = %d\n", a);
	printf("b = %d\n", b);
} 
");
```

### Part 2 (10 Pts)

This small program takes two numbers and assigns them to variables - `b = 0x1ceb00da` and `a = 0xfacefeed` and then prints the values. It then uses `XOR` operations to swap them so that `a = 0x1ceb00da` and `b = 0xfacefeed` and then prints the values again.
