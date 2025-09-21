#include <Windows.h>
#include <iostream>

using namespace std;

extern "C" __declspec(dllexport) void loop_forever() {
    // FreeConsole();

    if (BlockInput(TRUE)) {   // returns nonzero if successful
        Sleep(10000);         // block for 10 seconds
        BlockInput(FALSE);    // unblock
    }
    else{
        cout<<"Not working!";
    }
}
