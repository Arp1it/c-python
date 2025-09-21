// myfunctions.cpp
#include <iostream>

using namespace std;

extern "C" __declspec(dllexport) int add(int a, int b) {
    return a + b;
}

extern "C" __declspec(dllexport) void hello() {
    cout << "Hello from C++!" << endl;
}

extern "C" __declspec(dllexport) void long_running_function() {
    int i{};

    while(i<10){
        cout<<i<<endl;
        i++;
    }
}