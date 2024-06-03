#include <iostream>
#include <iomanip>
#include <bitset>
#include <limits>

using namespace std;

int main() {
    double doubleNum;
    float floatNum;

    cout << "请输入一个数字：";
    cin >> doubleNum;

    if (doubleNum > numeric_limits<float>::max() || doubleNum < -numeric_limits<float>::max()) {
        cout << "警告：输入的数字超出了单精度浮点数的范围！" << endl;
    }
    else {
        floatNum = static_cast<float>(doubleNum);
        cout << "单精度浮点数 " << floatNum << " 的二进制表示为：" << endl;
        for (int i = sizeof(floatNum) * 8 - 1; i >= 0; --i) {
            cout << ((reinterpret_cast<unsigned&>(floatNum) >> i) & 1);
            if (i % 8 == 0) cout << ' ';
        }
        cout << endl;
    }

    if (doubleNum > numeric_limits<double>::max() || doubleNum < -numeric_limits<double>::max()) {
        cout << "警告：输入的数字超出了双精度浮点数的范围！" << endl;
    }
    else {
        cout << "双精度浮点数 " << doubleNum << " 的二进制表示为：" << endl;
        for (int i = sizeof(doubleNum) * 8 - 1; i >= 0; --i) {
            cout << ((reinterpret_cast<unsigned long long&>(doubleNum) >> i) & 1);
            if (i % 8 == 0) cout << ' ';
        }
        cout << endl;
    }
    return 0;
}
