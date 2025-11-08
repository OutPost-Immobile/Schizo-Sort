#ifndef SCHIZO_SORT_TIMERESULT_H
#define SCHIZO_SORT_TIMERESULT_H

class TimeResult
{
private:
    double registeredTime = 0.0;
    int arraySize = 0;

public:
    double GetTime()
    {
        return registeredTime;
    }

    int GetArraySize()
    {
        return arraySize;
    }

    void SetTime(double time)
    {
        registeredTime = time;
    }

    void SetArraySize(int size)
    {
        arraySize = size;
    }
};

#endif //SCHIZO_SORT_TIMERESULT_H