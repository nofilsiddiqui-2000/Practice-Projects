#include <iostream>
#include <fstream>
#include <future>
#include <memory>
#include <thread>
#include <algorithm>

#include "GrayscaleProcessor.h"

Frame generateDummyFrame(int width, int height) {
    Frame frame{width, height, std::vector<uint8_t>(width * height * 3)};
    std::generate(frame.data.begin(), frame.data.end(), [] { return rand() % 256; });
    return frame;
}

void saveFrame(const Frame& frame, const std::string& filename) {
    std::ofstream out(filename, std::ios::binary);
    out.write(reinterpret_cast<const char*>(frame.data.data()), frame.data.size());
}

int main() {
    constexpr int width = 640;
    constexpr int height = 480;

    auto processor = std::make_unique<GrayscaleProcessor>();
    auto frame = std::make_shared<Frame>(generateDummyFrame(width, height));

    auto future = std::async(std::launch::async, [processor = std::move(processor), frame] {
        processor->process(*frame);
    });

    future.wait();
    saveFrame(*frame, "output_frame.bin");

    std::cout << "Frame processed and saved to output_frame.bin" << std::endl;
    return 0;
}
