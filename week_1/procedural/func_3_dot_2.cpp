#include <iostream>
#include <array>

template <typename Ta, typename Tb>
Ta prod(Ta* s_a, Ta* e_a, Tb* s_b) {
    Ta dot = 0.0;
    Ta* a = s_a;
    Tb* b = s_b;
    for(; a != e_a; a++, b++) {
        dot += (*a) * (*b);
    }
    return dot;
}

int main() {
    std::array<double, 3> a, b;
    a = {0, 1, 2};
    b = {3, 4, 5};

    auto res = prod(a.begin(), a.end(), b.begin());

    std::cout << res << std::endl;

    return 0;
}