#ifndef IFRAMEPROCESSOR_H
#define IFRAMEPROCESSOR_H

#include "Frame.h"

class IFrameProcessor {
public:
    virtual ~IFrameProcessor() = default;
    virtual void process(Frame& frame) = 0;
};

#endif // IFRAMEPROCESSOR_H
