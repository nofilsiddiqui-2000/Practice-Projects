# C++17 Interview Example

This project demonstrates a simple frame processing pipeline using modern C++17 features.
It showcases object-oriented design, smart pointers, asynchronous execution with `std::async`,
and a minimal CMake build setup.

The program generates a dummy frame, converts it to grayscale asynchronously, and
writes the result to `output_frame.bin`.

## Build and Run

```bash
mkdir build && cd build
cmake ..
make
./example
```
