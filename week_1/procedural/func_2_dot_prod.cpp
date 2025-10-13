#include <iostream>
#include <array>

double prod(const std::array<double, 3> a, const std::array<double, 3> b) {
    return
        a[0] * b[0] +
        a[1] * b[1] +
        a[2] * b[2];
}

double prod(const double a, const double b) {
    return a * b;
}

int main() {
    std::array<double, 3> a, b;
    a = {0, 1, 2};
    b = {3, 4, 5};

    std::cout << prod(a, b) << std::endl;

    return 0;
}