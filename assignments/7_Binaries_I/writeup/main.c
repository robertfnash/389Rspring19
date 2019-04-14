/*
 * Name: Robert Nash
 * Section: 0201
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Robert Nash
 */

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
