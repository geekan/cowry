#include <iostream>
using namespace std;

class A {
public:
    void output();
    void a();
};

class B {
public:
    void output();
};

class C: public A, public B {
public:
    void show();
};

void A::output()
{
    cout << "Class A" << endl;
}

void A::a()
{
    cout << "A::a" << endl;
}

void B::output()
{
    cout << "Class B" << endl;
}

int main(void)
{
    C c;
    c.A::output();
    c.a();
    return 0;
}
