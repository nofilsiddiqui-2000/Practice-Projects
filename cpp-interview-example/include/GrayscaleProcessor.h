#ifndef GRAYSCALEPROCESSOR_H
#define GRAYSCALEPROCESSOR_H

#include "IFrameProcessor.h"

class GrayscaleProcessor : public IFrameProcessor {
public:
    void process(Frame& frame) override;
};

#endif // GRAYSCALEPROCESSOR_H
