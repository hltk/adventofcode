appname := main

CXX=clang++
CXXFLAGS=-std=c++17 -march=native -mtune=native -O3 -Wall -Werror

srcfiles := $(shell find -name "*.cpp")

SRCS=src/*

all: $(appname)

$(appname):
	$(CXX) $(CXXFLAGS) -o $(appname) $(srcfiles)

clean:
	rm -fr $(appname)

format:
	clang-format -i $(srcfiles)
