#include <iostream>
#include <limits>
#include <cmath>

using namespace std;

int main() {
    // ���㵥���ȸ������Ļ�������
    float single_epsilon = 1.0f;
    while (1.0f + single_epsilon / 2 != 1.0f) {
        single_epsilon /= 2.0f;
    }

    // ����˫���ȸ������Ļ�������
    double double_epsilon = 1.0;
    while (1.0 + double_epsilon / 2 != 1.0) {
        double_epsilon /= 2.0;
    }

    // ���㵥���ȸ���������Сֵ�����ֵ
    float single_min = 1.0f;
    float single_max = 1.0f;

    while (single_min / 2.0f != 0.0f) {
        single_min /= 2.0f;
    }

    while (single_max == single_max * 2.0f - single_max) {
        single_max *= 2.0f;
    }
    //single_max = 2.0f * single_max - 1;

    // ����˫���ȸ���������Сֵ�����ֵ
    double double_min = 1.0;
    double double_max = 1.0;

    while (double_min / 2.0 != 0.0) {
        double_min /= 2.0;
    }

    while (double_max == double_max * 2.0 - double_max) {
        double_max *= 2.0;
    }
    //double_max = double_max * 2.0 - 1;

    cout << "�����ȸ������Ļ�������: " << single_epsilon << endl;
    cout << "�����ȸ�����������ֵ: " << single_min << endl;
    cout << "�����ȸ�����������ֵ: " << single_max << endl;
    cout << "�����ȸ����������ۻ�������: " << numeric_limits<float>::epsilon() << endl;
    cout << "�����ȸ���������������ֵ: " << numeric_limits<float>::denorm_min() << endl;
    cout << "�����ȸ���������������ֵ: " << numeric_limits<float>::max() << endl;
    cout << endl;
    cout << "˫���ȸ������Ļ�������: " << double_epsilon << endl;
    cout << "˫���ȸ�����������ֵ: " << double_min << endl;
    cout << "˫���ȸ�����������ֵ: " << double_max << endl;
    cout << "˫���ȸ����������ۻ�������: " << numeric_limits<double>::epsilon() << endl;
    cout << "˫���ȸ���������������ֵ: " << numeric_limits<double>::denorm_min() << endl;
    cout << "˫���ȸ���������������ֵ: " << numeric_limits<double>::max() << endl;

    return 0;
}
