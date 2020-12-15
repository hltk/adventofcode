#include "advent.h"

#include <array>

constexpr std::uint32_t P1_TARGET = 2020 - 1;
constexpr std::uint32_t P2_TARGET = 30000000 - 1;

std::array<std::uint32_t, P2_TARGET> h;

ret_t solve15(input_t inp) {
	h.fill(-1);

	std::uint32_t t = 0;
	std::uint32_t num{}, lnum = -1;
	for (const auto c : inp) {
		if ('0' <= c && c <= '9') {
			num = num * 10 + (c - '0');
		} else {
			if (lnum != -1) {
				h[lnum] = t++;
			}
			lnum = num;
			num = 0;
		}
	}
	std::uint32_t p1_ans;
	for (; t < P1_TARGET; ++t) {
		num = h[lnum] != -1 ? t - h[lnum] : 0;
		h[lnum] = t;
		lnum = num;
	}
	p1_ans = lnum;
	for (; t < P2_TARGET; ++t) {
		num = h[lnum] != -1 ? t - h[lnum] : 0;
		h[lnum] = t;
		lnum = num;
	}
	return {std::to_string(p1_ans), std::to_string(lnum)};
}
