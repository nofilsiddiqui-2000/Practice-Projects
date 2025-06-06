cmake_minimum_required(VERSION 3.10)
project(cpp_interview_example LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(frame_processor
    src/GrayscaleProcessor.cpp
)

target_include_directories(frame_processor PUBLIC include)

add_executable(example src/main.cpp)

target_link_libraries(example PRIVATE frame_processor)
