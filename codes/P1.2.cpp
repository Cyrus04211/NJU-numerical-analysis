#include <iostream>
#include <limits>
#include <cmath>

using namespace std;

int main() {
    // 计算单精度浮点数的机器精度
    float single_epsilon = 1.0f;
    while (1.0f + single_epsilon / 2 != 1.0f) {
        single_epsilon /= 2.0f;
    }

    // 计算双精度浮点数的机器精度
    double double_epsilon = 1.0;
    while (1.0 + double_epsilon / 2 != 1.0) {
        double_epsilon /= 2.0;
    }

    // 计算单精度浮点数的最小值和最大值
    float single_min = 1.0f;
    float single_max = 1.0f;

    while (single_min / 2.0f != 0.0f) {
        single_min /= 2.0f;
    }

    while (single_max == single_max * 2.0f - single_max) {
        single_max *= 2.0f;
    }
    //single_max = 2.0f * single_max - 1;

    // 计算双精度浮点数的最小值和最大值
    double double_min = 1.0;
    double double_max = 1.0;

    while (double_min / 2.0 != 0.0) {
        double_min /= 2.0;
    }

    while (double_max == double_max * 2.0 - double_max) {
        double_max *= 2.0;
    }
    //double_max = double_max * 2.0 - 1;

    cout << "单精度浮点数的机器精度: " << single_epsilon << endl;
    cout << "单精度浮点数的下溢值: " << single_min << endl;
    cout << "单精度浮点数的上溢值: " << single_max << endl;
    cout << "单精度浮点数的理论机器精度: " << numeric_limits<float>::epsilon() << endl;
    cout << "单精度浮点数的理论下溢值: " << numeric_limits<float>::denorm_min() << endl;
    cout << "单精度浮点数的理论上溢值: " << numeric_limits<float>::max() << endl;
    cout << endl;
    cout << "双精度浮点数的机器精度: " << double_epsilon << endl;
    cout << "双精度浮点数的下溢值: " << double_min << endl;
    cout << "双精度浮点数的上溢值: " << double_max << endl;
    cout << "双精度浮点数的理论机器精度: " << numeric_limits<double>::epsilon() << endl;
    cout << "双精度浮点数的理论下溢值: " << numeric_limits<double>::denorm_min() << endl;
    cout << "双精度浮点数的理论上溢值: " << numeric_limits<double>::max() << endl;

    return 0;
}
