#include "advent.h"

#include <array>

static constexpr std::uint32_t P1_INDEX = 2020 - 1;
static constexpr std::uint32_t P2_INDEX = 30000000 - 1;

static std::array<std::uint32_t, P2_INDEX> last_index;

ret_t solve15(input_t input) {
	last_index.fill(-1);

	std::uint32_t index = 0;
	std::uint32_t cur = 0, prev = -1;
	for (const auto c : input) {
		if ('0' <= c && c <= '9') {
			cur = cur * 10 + (c - '0');
		} else {
			if (prev != -1) {
				last_index[prev] = index++;
			}
			prev = cur;
			cur = 0;
		}
	}
	for (; index < P1_INDEX; ++index) {
		cur = last_index[prev] != -1 ? index - last_index[prev] : 0;
		last_index[prev] = index;
		prev = cur;
	}
	std::uint32_t p1_ans = prev;
	for (; index < P2_INDEX; ++index) {
		cur = last_index[prev] != -1 ? index - last_index[prev] : 0;
		last_index[prev] = index;
		prev = cur;
	}
	return {std::to_string(p1_ans), std::to_string(prev)};
}
