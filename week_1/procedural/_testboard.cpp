#include <iostream>
#include <cmath>
#include <vector>

int main() {
    const int n = 100;
    std::vector<double> vec(n, 1.0);
    const double rn = 1.0 / static_cast<double>(n);
    double mean = 0.0;
    for (size_t i = 0; i < n; i++) {
        mean += rn * vec[i];
    }
    std::cout << "mean is " << mean << std::endl;

    return 0;
}