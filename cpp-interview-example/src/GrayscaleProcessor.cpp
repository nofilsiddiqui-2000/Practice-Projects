#include "GrayscaleProcessor.h"

void GrayscaleProcessor::process(Frame& frame) {
    if (frame.data.size() != static_cast<size_t>(frame.width * frame.height * 3)) {
        return;
    }

    for (int y = 0; y < frame.height; ++y) {
        for (int x = 0; x < frame.width; ++x) {
            size_t index = static_cast<size_t>((y * frame.width + x) * 3);
            auto r = frame.data[index];
            auto g = frame.data[index + 1];
            auto b = frame.data[index + 2];
            auto gray = static_cast<uint8_t>((r + g + b) / 3);
            frame.data[index] = frame.data[index + 1] = frame.data[index + 2] = gray;
        }
    }
}
