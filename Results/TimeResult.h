#ifndef SCHIZO_SORT_TIMERESULT_H
#define SCHIZO_SORT_TIMERESULT_H

class TimeResult
{
private:
    int registeredTime = 0;
    int arraySize = 0;


public:
    int GetTime()
    {
        return registeredTime;
    }

    int GetArraySize()
    {
        return arraySize;
    }

    void SetTime(int time)
    {
        registeredTime = time;
    }

    void SetArraySize(int size)
    {
        arraySize = size;
    }
};

#endif //SCHIZO_SORT_TIMERESULT_H