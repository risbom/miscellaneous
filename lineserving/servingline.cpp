#include <iostream>
#include <string>
#include "windows.h"
#include <queue>
using namespace std;

int main (void)
{
cout <<" ___________________________ "<<endl;
cout <<"|/ / / / / / / / / / / / / /|"<< endl;
cout <<"|  Line for drinks serving  |"<< endl;
cout <<"|/ / / / / / / / / / / / / /|"<< endl;
cout <<"|___________________________|"<< endl;
cout <<"|___________________________|"<< endl;

    string namefirst;
    string namesecond;
    string namethird;

cout << " Enter the first persons name - ";
cin  >> namefirst;

cout << " Enter the second persons name - ";
cin  >> namesecond;

cout << " Enter the first persons name - ";
cin  >> namethird;

cout << "" <<endl<<endl;

    queue <string> names;
    names.push (namefirst);
    names.push (namesecond);
    names.push (namethird);

    cout << "There is currently "  << names.size () << " in line. " <<endl;
    Sleep(2000);
    
    cout << "The person at the front is "  << names.front () << " . " <<endl;
    Sleep(2000);

    cout << "The person at the end is "  << names.back () << " . " <<endl<<endl;
    Sleep(2000);
    
    cout << names.front () << " is served!" <<endl<<endl;
    Sleep(2000);
    names.pop();
    
    cout << "There is currently "  << names.size () << " in line. " <<endl;
    Sleep(2000);
    
    cout << "The person at the front is "  << names.front () << " , and the person at the end is " << names.back () << " . " <<endl <<endl;
    Sleep(2000);

    cout << names.front () << " is served!" <<endl<<endl;
    Sleep(2000);

    cout << "There is still "  << names.front () << " in the line." <<endl;
    Sleep(2000);

    cout << names.front () << " took his/her drink!" <<endl<<endl;
    Sleep(2000);

    cout << "The line is empty! " <<endl <<endl;
    cout << "Come again! " <<endl <<endl;

    system("PAUSE");
    return 0;

}