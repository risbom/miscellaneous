//-----------------------------------------------------------------------------
// ass-a2.c
//
// Assignment 2 Prime Counter
//
// Author: Boris Malinic 11736063
//
// Latest Changes: 28.10.2019 
//-----------------------------------------------------------------------------
//

#include <stdio.h>
#include <stdint.h>
unsigned int countPrimes(uint32_t array[], unsigned int array_size);

int main(void)
{
  unsigned int Size = 0;
  unsigned int Test[Size];
  unsigned int PrimeCount = 0;

  PrimeCount = countPrimes(Test,Size);
  printf("The number of primes in your chosen array is %d.\n", PrimeCount);

  return 0;
}
unsigned int countPrimes(uint32_t array[], unsigned int array_size)
{ 

  unsigned int counter = 0;
  int element;
  int divider;
  int primeTest;
  printf("Enter the array size please: \n");
  scanf("%u", &array_size);
  printf("Enter the numbers of the array: \n");
  for (element=0; element<array_size; element++)
  {
    scanf("%d", &array[element]);
  }
  for (element=0; element<array_size; element++)
  {
    primeTest=0;
    for (divider=2; divider<array[element] || array[element]<2; divider++)
    {
      if (array[element]%divider==0 || array[element]<2)
      {
        primeTest=1;
        break;
      }
    }
    if (primeTest==0)
      
      counter ++;   
  }
  
  return counter;
}