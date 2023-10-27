#include "factors.h"
#include <iostream>
#include <fstream>
#include <cmath>

std::vector<std::pair<int, int>> factorise(int number) {
    std::vector<std::pair<int, int>> factors;
    for (int i = 2; i <= sqrt(number); ++i) {
        if (number % i == 0) {
	    factors.emplace_back(i, number / i);
        }
    }
    return factors;
}


void factorise_file(const std::string& file_path) {
    std::ifstream file(file_path);
    if (!file) {
        std::cerr << "Failed to open the file: " << file_path << std::endl;
        return;
    }

    int number;
    while (file >> number) {
        std::vector<std::pair<int, int>> factors = factorise(number);
        for (const auto& factor : factors)
        {
            std::cout << number << " = " << factor.first << " * " << factor.second << std::endl;
        }
    }
}
