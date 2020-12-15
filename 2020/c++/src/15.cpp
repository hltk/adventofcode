#include "advent.h"

#include <array>

static constexpr std::uint32_t P1_INDEX = 2020 - 1;
static constexpr std::uint32_t P2_INDEX = 30000000 - 1;

static std::array<std::uint32_t, P2_INDEX> last_time;

ret_t solve15(input_t input) {
	last_time.fill(-1);

	std::uint32_t time = 0;
	std::uint32_t cur = 0, prev = -1;
	for (const auto c : input) {
		if ('0' <= c && c <= '9') {
			cur = cur * 10 + (c - '0');
		} else {
			if (prev != -1) {
				last_time[prev] = time++;
			}
			prev = cur;
			cur = 0;
		}
	}
	for (; time < P1_INDEX; ++time) {
		cur = last_time[prev] != -1 ? time - last_time[prev] : 0;
		last_time[prev] = time;
		prev = cur;
	}
	std::uint32_t p1_ans = prev;
	for (; time < P2_INDEX; ++time) {
		cur = last_time[prev] != -1 ? time - last_time[prev] : 0;
		last_time[prev] = time;
		prev = cur;
	}
	return {std::to_string(p1_ans), std::to_string(prev)};
}
