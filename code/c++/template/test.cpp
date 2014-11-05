#include <iostream>
#include <string>

using namespace std;

namespace test {

// 1. 类模板
template <class T1, class T2>
class testClass {
private:
    T1 I;
    T2 J;
public:
    testClass(T1 a, T2 b);
    void show();
};

// 2. 函数模板
template <class T> 
T max(T a, T b)
{
    return (a > b) ? a : b;
}

template <class T1, class T2>
testClass<T1, T2>::testClass(T1 a, T2 b): I(a), J(b) {}

template <class T1, class T2>
void testClass<T1, T2>::show()
{
    cout << I << "|" << J << endl;
}

// 3. 非类型模板参数
template<typename T, int MAXSIZE>
class Stack {
    private:
        T elems[MAXSIZE];
};

} // end for test namespace

int main(void)
{
    int a = 1, b = 5;
    double x = 3, y = 8;
    cout << test::max(a, b) << endl;
    cout << test::max(x, y) << endl;

    test::testClass<int, int> class_ii(10, 12);
    class_ii.show();
    test::testClass<int, double> class_id(13, 5.5);
    class_id.show();

    test::Stack<int, 64> istack;
    return 0;
}

