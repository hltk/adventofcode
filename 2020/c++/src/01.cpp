#include "advent.h"

#include <array>

constexpr std::size_t target = 2020;

ret_t solve01(input_t inp) {
	std::array<std::uint32_t, 1 << 11> counts{};
	int cur = 0;
	for (const auto c : inp) {
		if ('0' <= c && c <= '9') {
			cur = cur * 10 + (c - '0');
		} else {
			counts[cur]++;
			cur = 0;
		}
	}
	std::int32_t p1{};
	for (std::size_t i = 0; i <= target; ++i) {
		std::size_t j = target - i;
		if (counts[i] >= (1 + (i == j)) && counts[j] >= 1) {
			p1 = i * (target - i);
			break;
		}
	}
	std::int32_t p2{};
	for (std::size_t i = 0; i <= target; ++i) {
		for (std::size_t j = 0; i + j <= target && j <= i; ++j) {
			std::size_t k = target - i - j;
			if (counts[i] >= (1 + (j == i) + (k == i)) &&
			    counts[j] >= (1 + (i == j) + (j == k)) &&
			    counts[k] >= 1) {
				p2 = i * j * k;
			}
		}
	}
	return {std::to_string(p1), std::to_string(p2)};
}
