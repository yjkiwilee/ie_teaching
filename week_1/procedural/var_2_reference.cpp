#include <iostream>

int main() {
    double d = 5.0;
    double& r_d = d;

    std::cout << d << std::endl;
    
    r_d = 6.0;

    std::cout << d << std::endl;

    return 0;
}