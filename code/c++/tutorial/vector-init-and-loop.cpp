#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    unsigned int i;
    vector<int> first;
    vector<int> second(4, 100);
    vector<int> third(second.begin(), second.end());
    vector<int> fourth(third);

    int myints[] = {1, 4, 7, 10};
    vector<int> fifth(myints, myints + sizeof(myints) / sizeof(int));

    cout << "The content of fifth are: ";
    for (vector<int>::iterator it = fifth.begin(); it < fifth.end(); ++it)
    {
        cout << " " << *it;
    }
    cout << endl;

    return 0;
}
