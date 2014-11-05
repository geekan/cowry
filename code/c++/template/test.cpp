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
    cout << test::max(a, b) << endl;
    return 0;
}

