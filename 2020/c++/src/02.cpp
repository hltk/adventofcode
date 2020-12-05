#include "advent.h"

ret_t solve02(input_t inp) {
	std::uint32_t p1{}, p2{};
	for (std::size_t iter = 0; iter < inp.size(); ++iter) {
		uint32_t a{}, b{};
		while (inp[iter] != '-') {
			a = a * 10 + (inp[iter++] - '0');
		}
		iter++;
		while (inp[iter] != ' ') {
			b = b * 10 + (inp[iter++] - '0');
		}
		iter++;
		char c = inp[iter];
		iter += 3;
		uint32_t cp1{};
		uint8_t cp2{};
		for (uint32_t pos = 1; inp[iter] != '\n'; pos++, iter++) {
			if (inp[iter] == c) {
				if (a == pos || b == pos) {
					cp2 ^= 1;
				}
				cp1++;
			}
		}
		p1 += a <= cp1 && cp1 <= b;
		p2 += cp2;
	}
	return {std::to_string(p1), std::to_string(p2)};
}
