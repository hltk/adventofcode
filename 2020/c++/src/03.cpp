#include "advent.h"

#include <array>

std::array<std::array<int, 2>, 5> slopes{
    std::array<int, 2>{3, 1}, std::array<int, 2>{1, 1},
    std::array<int, 2>{5, 1}, std::array<int, 2>{7, 1},
    std::array<int, 2>{1, 2}};

ret_t solve03(input_t inp) {
	std::uint32_t cols = 0;
	while (inp[cols] != '\n')
		++cols;
	std::size_t pos{};
	for (const auto c : inp) {
		if (c != '\n') {
			inp[pos++] = c;
		}
	}
	std::uint32_t rows = pos / cols;
	std::uint32_t p1{};
	for (std::size_t i = 0, j = 0; i < rows;) {
		p1 += inp[i * cols + j] == '#';
		i += slopes[0][1];
		j += slopes[0][0];
		j %= cols;
	}
	std::uint32_t p2(1);
	for (std::size_t k = 0; k < slopes.size(); ++k) {
		std::uint32_t c{};
		for (std::size_t i = 0, j = 0; i < rows;) {
			c += inp[i * cols + j] == '#';
			i += slopes[k][1];
			j += slopes[k][0];
			j %= cols;
		}
		p2 *= c;
	}
	return {std::to_string(p1), std::to_string(p2)};
}
