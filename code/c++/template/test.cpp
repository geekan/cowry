#include <iostream>
#include <string>

using namespace std;

namespace test {

template <class T> 
T max(T a, T b)
{
    return (a > b) ? a : b;
}

}

int main(void)
{
    int a = 1, b = 5;
    double x = 3, y = 8;
    cout << test::max(a, b) << endl;
    cout << test::max(x, y> << endl;
    return 0;
}

