add_test(NAME eyu.help COMMAND Eyu::eyu --help)
set_tests_properties(
  eyu.help
  PROPERTIES PASS_REGULAR_EXPRESSION "Usage: eyu"
)
add_test(NAME eyu.version COMMAND Eyu::eyu --version)
set_tests_properties(
  eyu.version
  PROPERTIES PASS_REGULAR_EXPRESSION "Eyu ${PROJECT_VERSION}"
)
