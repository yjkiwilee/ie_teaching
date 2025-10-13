#include <iostream>

int main() {
    int sum = 0;
    const double pi = 3.14;
    double max_circumference = 0.0;
    for (int i = 0; i < 10; i++) {
        double radius = static_cast<double>(i);
        double circumference  = 2 * pi * radius;
        
        if(circumference > max_circumference) {
            max_circumference = circumference;
        }
    }
    std::cout << "largest circumference is " << max_circumference << std::endl;
}