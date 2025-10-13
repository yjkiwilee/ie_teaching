#include <iostream>

void swap_vars(double& a, double& b) {
    double tmp = std::move(a);
    a = std::move(b);
    b = std::move(tmp);
}

int main() {
    double a = 1, b = 2;

    std::cout << "a = " << a << ", b = " << b << std::endl;

    swap_vars(a, b);

    std::cout << "a = " << a << ", b = " << b << std::endl;

    return 0;
}