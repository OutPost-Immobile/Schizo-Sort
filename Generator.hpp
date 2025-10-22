#pragma once
#ifndef GENERATOR_H
#define GENERATOR_H

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

//Generate random integer vector
std::vector<int> generateRandomIntVector(size_t size, int minValue, int maxValue) {
	std::vector<int> vec(size);
	std::srand(static_cast<unsigned int>(std::time(0)));
	for (size_t i = 0; i < size; ++i) {
		vec[i] = minValue + std::rand() % (maxValue - minValue + 1);
	}
	return vec;
}

//Generate vector with random integer vectors for testing
std::vector<std::vector<int>> generateRandomIntVectorCollection(size_t collectionSize, size_t vectorSize, int minValue, int maxValue) {
	std::vector<std::vector<int>> collection;
	for (size_t i = 0; i < collectionSize; ++i) {
		collection.push_back(generateRandomIntVector(vectorSize, minValue, maxValue));
	}
	return collection;
}
#endif // GENERATOR_H