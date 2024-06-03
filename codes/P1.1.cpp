#include <iostream>
#include <iomanip>
#include <bitset>
#include <limits>

using namespace std;

int main() {
    double doubleNum;
    float floatNum;

    cout << "������һ�����֣�";
    cin >> doubleNum;

    if (doubleNum > numeric_limits<float>::max() || doubleNum < -numeric_limits<float>::max()) {
        cout << "���棺��������ֳ����˵����ȸ������ķ�Χ��" << endl;
    }
    else {
        floatNum = static_cast<float>(doubleNum);
        cout << "�����ȸ����� " << floatNum << " �Ķ����Ʊ�ʾΪ��" << endl;
        for (int i = sizeof(floatNum) * 8 - 1; i >= 0; --i) {
            cout << ((reinterpret_cast<unsigned&>(floatNum) >> i) & 1);
            if (i % 8 == 0) cout << ' ';
        }
        cout << endl;
    }

    if (doubleNum > numeric_limits<double>::max() || doubleNum < -numeric_limits<double>::max()) {
        cout << "���棺��������ֳ�����˫���ȸ������ķ�Χ��" << endl;
    }
    else {
        cout << "˫���ȸ����� " << doubleNum << " �Ķ����Ʊ�ʾΪ��" << endl;
        for (int i = sizeof(doubleNum) * 8 - 1; i >= 0; --i) {
            cout << ((reinterpret_cast<unsigned long long&>(doubleNum) >> i) & 1);
            if (i % 8 == 0) cout << ' ';
        }
        cout << endl;
    }
    return 0;
}
