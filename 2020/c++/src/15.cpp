#include "advent.h"

#include <array>

static constexpr std::uint32_t P1_INDEX = 2020 - 1;
static constexpr std::uint32_t P2_INDEX = 30000000 - 1;

static std::array<std::uint32_t, P2_INDEX> last_index;

ret_t solve15(input_t input) {
	last_index.fill(-1);

	std::uint32_t index = 0;
	std::uint32_t current = 0, previous = -1;

	for (const auto c : input) {
		if ('0' <= c && c <= '9')
			current = current * 10 + (c - '0');
		else {
			if (previous != -1)
				last_index[previous] = index++;
			previous = current;
			current = 0;
		}
	}

	auto calculate = [&index, &previous ](const auto end) -> auto {
		for (; index < end; ++index) {
			std::uint32_t current = 0;
			if (last_index[previous] != -1)
				current = index - last_index[previous];
			last_index[previous] = index;
			previous = current;
		}
		return previous;
	};

	auto p1_answer = calculate(P1_INDEX);
	auto p2_answer = calculate(P2_INDEX);

	return {std::to_string(p1_answer), std::to_string(p2_answer)};
}
