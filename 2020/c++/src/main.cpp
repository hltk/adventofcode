#include <chrono>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>

#include "advent.h"

static input_t read_input(std::string);

std::vector<std::function<ret_t(input_t)>> days{solve01, solve02, solve03};

int main() {
	for (std::size_t i = 0; i < days.size(); ++i) {
		std::stringstream filename;
		filename << "input/";
		filename << std::setw(2) << std::setfill('0') << i + 1;
		filename << ".in";

		auto inp = read_input(filename.str());

		auto begin = std::chrono::steady_clock::now();
		auto [p1, p2] = days[i](inp);
		auto end = std::chrono::steady_clock::now();

		auto elapsed =
		    std::chrono::duration_cast<std::chrono::microseconds>(
			end - begin);

		std::cout << "Day " << i + 1 << ": ";
		std::cout << elapsed.count() << "µs" << '\t';
		std::cout << std::setw(16) << std::setfill(' ');
		std::cout << p1 << ' ';
		std::cout << std::setw(16) << std::setfill(' ');
		std::cout << p2 << std::endl;
	}
}

static input_t read_input(const std::string fname) {
	std::ifstream file(fname, std::ios::binary | std::ios::ate);
	if (!file.is_open()) {
		std::cerr << "failed to open " << fname << std::endl;
		std::exit(1);
	}
	std::streamsize size = file.tellg();
	file.seekg(0, std::ios::beg);

	std::vector<char> buffer(size);
	if (!file.read(buffer.data(), size)) {
		std::cerr << "read error" << std::endl;
		std::exit(1);
	}
	return buffer;
}
