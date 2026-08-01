cmake_minimum_required(VERSION 3.28)

project(
  Eyu
  VERSION 0.1.0
  HOMEPAGE_URL "https://github.com/michaelchern/Eyu"
  DESCRIPTION "A minimal, expressive scripting language"
  LANGUAGES CXX
)

option(EYU_BUILD_TESTS "Build the Eyu test suite" ON)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

include(CompilerWarnings)

add_executable(eyu app/main.cpp)
add_executable(Eyu::eyu ALIAS eyu)

target_compile_features(eyu PRIVATE cxx_std_20)
target_compile_definitions(eyu PRIVATE EYU_VERSION="${PROJECT_VERSION}")

eyu_enable_compiler_warnings(eyu)

set_target_properties(
  eyu
  PROPERTIES
    CXX_EXTENSIONS OFF
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)

if(EYU_BUILD_TESTS)
  include(CTest)

  if(BUILD_TESTING)
    add_subdirectory(tests)
  endif()
endif()
