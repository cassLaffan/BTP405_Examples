#include <iostream>

/*
* Let's take a look at nomial typing in one of the stronger
* typed languages, C++. Remember, nominal languages 
*/

// Let's write a function that only takes ints as args
int add(int a, int b){
	return a + b;
}

int main(){
	// Calling the function as expected
	int expected = add(3, 7);
	std::cout << expected << std::endl;

	// Now, the following line will NOT spit out a compile-time error
	int result = add('a', 'b');
	std::cout << result << std::endl;
	
	// But the following line will
	//int nextResult = add("Number One", "Number Two");

	// There are implicit conversions between ints and characters
	// but not for strings

	return 0;
}