#include "advent.h"

#include <array>

constexpr std::uint32_t CACHE_SZ = 3e7;

std::array<std::uint32_t, CACHE_SZ> h;

constexpr std::uint32_t P1_TARGET = 2020;
constexpr std::uint32_t P2_TARGET = 30000000;

ret_t solve15(input_t inp) {
	h.fill(-1);

	std::uint32_t t = 1;
	std::uint32_t num{}, lnum = -1;
	for (const auto c : inp) {
		if ('0' <= c && c <= '9') {
			num = num * 10 + (c - '0');
		} else {
			if (lnum != -1) {
				h[lnum] = t++ - 1;
			}
			lnum = num;
			num = 0;
		}
	}
	std::uint32_t p1_ans;
	for (; t < P2_TARGET; ++t) {
		if (t == P1_TARGET) {
			p1_ans = lnum;
		}
		if (h[lnum] != -1) {
			num = (t - 1) - h[lnum];
		} else {
			num = 0;
		}
		h[lnum] = t - 1;
		lnum = num;
	}
	return {std::to_string(p1_ans), std::to_string(lnum)};
}
