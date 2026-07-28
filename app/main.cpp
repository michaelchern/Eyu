#include <iostream>
#include <string_view>

#ifndef EYU_VERSION
#define EYU_VERSION "unknown"
#endif

namespace {

constexpr std::string_view kProgramName{"eyu"};
constexpr std::string_view kVersion{EYU_VERSION};

void print_help()
{
    std::cout << "Usage: " << kProgramName << " [options] [script]\n\n"
              << "Options:\n"
              << "  -h, --help       Show this help message\n"
              << "  -v, --version    Show the Eyu version\n";
}

} // namespace

int main(int argc, char* argv[])
{
    if (argc > 1) {
        const std::string_view argument{argv[1]};

        if (argument == "-h" || argument == "--help") {
            print_help();
            return 0;
        }

        if (argument == "-v" || argument == "--version") {
            std::cout << "Eyu " << kVersion << '\n';
            return 0;
        }

        std::cerr << "eyu: script execution is not implemented yet\n";
        return 64;
    }

    std::cout << "Eyu " << kVersion << " development shell\n"
              << "The compiler and virtual machine are not implemented yet.\n";
    return 0;
}
