#include <iostream>
using namespace std;

class Circle
{
    public:
    void set(double r)
    {
        Radius = r;
    }
    protected:
    double Radius;

};
class Hoop: public Circle
{
    public:
    double circumference(){
        return 2*Radius*3.14;
    }
    double area(){
        return (Radius*Radius)*3.14;
    }
};

int main(void)
{
    Hoop h;
    double radius;
    cout << "Enter the radius - > ";
    cin  >> radius;

    h.set(radius);
    double O = h.circumference();
    double P = h.area();

    cout << "For the entered radius " <<radius<<", the hoop circumference is "<<O<<"."<<endl;
    cout << "For the entered radius " <<radius<<", the hoop area is "<<P<<"."<<endl;

    return 0;
 
}

