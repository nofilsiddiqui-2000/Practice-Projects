#ifndef FRAME_H
#define FRAME_H

#include <vector>
#include <cstdint>

struct Frame {
    int width;
    int height;
    std::vector<uint8_t> data;
};

#endif // FRAME_H
