#ifndef SCHIZO_SORT_RANDOMARRAYGENERATOR_H
#define SCHIZO_SORT_RANDOMARRAYGENERATOR_H
#include <random>
#include <vector>

inline std::vector<std::vector<int>> GenerateRandomArrayCollection(std::vector<int> sizes)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution dis(0, 1000000);

    std::vector<std::vector<int>> randomArrayCollection;

    for (auto size : sizes)
    {
        std::vector<int> tempArray;
        for (int i = 0; i < size; ++i)
        {
            tempArray.push_back((dis(gen)));
        }

        randomArrayCollection.push_back(tempArray);
    }

    return randomArrayCollection;
}

#endif //SCHIZO_SORT_RANDOMARRAYGENERATOR_H
