#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void)
{
	vector<string> vs;

	vs.push_back("string1");
	vs.push_back("string2");
	vs.push_back("string3");

	cout << "1. loop by index.." << endl;
	unsigned int i;
	for (i = 0; i < vs.size(); i++) {
		cout << vs[i] << endl;
	}

	cout << "2. loop by iterator" << endl;
	vector<string>::const_iterator ci;
	for (ci = vs.begin(); ci != vs.end(); ci++) {
		cout << *ci << endl;
	}

	cout << "3. reverse loop" << endl;
	vector<string>::reverse_iterator ri;
	for (ri = vs.rbegin(); ri!= vs.rend(); ri++) {
		cout << *ri << endl;
	}

	cout << "--------" << endl;

	cout << "vs size is " << vs.size() << endl;
	swap(vs[0], vs[2]);
	for (i = 0; i < vs.size(); i++) {
		cout << vs[i] << endl;
	}

	return 0;
}