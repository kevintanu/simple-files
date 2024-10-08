# Compilation of Errors

## MSVC
- Missing .lib when creating .dll files

With no exported symbols .lib file is not created. (In case of shared libraries, .lib is essentially an import file)

https://stackoverflow.com/questions/64088046/missing-lib-file-when-creating-shared-library-with-cmake-and-visual-studio-2019

- Can't have function implementation in .h files if included in multiple files, duplicate implementation

- Unresolved external symbol / Unknown override specifier
  - try forward declaration, also check again for symbol that's not there when compiling
  - mostly because circular dependencies

- initial value of reference to non-const must be an lvalue
  - comes from when you are trying to bind a non-const reference to a temporary object. trying to assign a temporary object, constructed inside some function, to non const reference. `lvalue` = existing object in memory.`rvalue` = temporary non existing object