#include <iostream>
#include <cmath>
#include <random>

int main() {
    // Part 1

    /* const double x = 0.3, y = 0.4;
    const double r = std::sqrt(std::pow(x, 2.0) + std::pow(y, 2.0));

    std::cout << r << std::endl; */

    // Part 2

    /* std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<double> unif(-1.0, 1.0);

    const int N = 10000;
    double x, y;
    int count = 0;
    
    for(int i = 0; i < N; i++) {
        x = unif(gen);
        y = unif(gen);
        
        if(std::sqrt(std::pow(x, 2.0) + std::pow(y, 2.0)) < 1) {
            count++;
        }
    }

    const double est_pi = static_cast<double>(count) / static_cast<double>(N) * 4.0;

    std::cout << est_pi << std::endl; */

    // Part 3

    /* const int N = 1000;

    double sum = 0;

    for(int n = 1; n <= N; n++) {
        sum += 1.0 / static_cast<double>(n * n);
    }

    const double est_pi = std::sqrt(sum * 6.0);

    std::cout << est_pi << std::endl; */

    return 0;
}