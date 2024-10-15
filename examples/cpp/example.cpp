// insecure_code.cpp

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>

void commandInjection() {
    char command[256];
    std::cout << "Enter command: ";
    std::cin >> command;
    system(command);  // 命令注入漏洞
}

void bufferOverflow() {
    char buffer[8];
    std::cout << "Enter input: ";
    std::cin >> buffer;  // 缓冲区溢出漏洞
    std::cout << "You entered: " << buffer << std::endl;
}

void hardcodedPassword() {
    const char* password = "P@ssw0rd!";
    std::cout << "Password is: " << password << std::endl;
}

int main() {
    commandInjection();
    bufferOverflow();
    hardcodedPassword();
    return 0;
}
