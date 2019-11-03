//-----------------------------------------------------------------------------
// ass-a1.c
//
// Assignment 1 Bodymassindex (BMI) calculator
//
// Author: Boris Malinic 11736063
//
// Latest Changes: 23.10.2019 
//-----------------------------------------------------------------------------
//

#include <stdio.h>

int main (void)
{
  float weight; 
  float height;
  float bmi;
    
  printf("Bitte geben Sie Ihr Gewicht in kg ein: \n");
  scanf("%f", &weight);

  printf("Bitte geben Sie Ihre Körpergröße in cm ein: \n");
  scanf("%f", &height);
    
  float heightinmeters;
  heightinmeters = height / 100;

  bmi = weight / (heightinmeters*heightinmeters);
  printf("BMI: %.1f\n",bmi);

  char *category;

  if (bmi < 16.0)
  {  
    category = "Starkes Untergewicht";
  }

  else if (bmi >= 16.0 && bmi < 17.0)
  {
    category = "Mäßiges Untergewicht";
  }

  else if (bmi >= 17.0 && bmi < 18.5)
  {
    category = "Leichtes Untergewicht";
  }

  else if (bmi >= 18.5 && bmi < 25.0)
  {
    category = "Normalgewicht";
  }
    
  else if (bmi >= 25.0 && bmi < 30.0)
  {
    category = "Präadipositas";
  }
    
  else if (bmi >= 30.0 && bmi < 35.0)
  {
    category = "Adipositas Grad I";
  }

  else if (bmi >= 35.0 && bmi < 40.0)
  {
    category = "Adipositas Grad II";
  }

  else if (bmi >= 40)
  {
    category = "Adipositas Grad III";
  }

  printf("Kategorie: %s\n", category);

  return 0;
}