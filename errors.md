# Compilation of Errors

## MSVC
- Missing .lib when creating .dll files

With no exported symbols .lib file is not created. (In case of shared libraries, .lib is essentially an import file)

https://stackoverflow.com/questions/64088046/missing-lib-file-when-creating-shared-library-with-cmake-and-visual-studio-2019

- Can't have function implementation in .h files if included in multiple files, duplicate implementation

- Unresolved external symbol / missing type specifier /Unknown override specifier /uses undefined struct
  - try forward declaration, also check again for symbol that's not there when compiling
  - mostly because circular dependencies
  - if declaring a struct that use value type of another struct, compiler need to know the size of that another struct

- initial value of reference to non-const must be an lvalue
  - comes from when you are trying to bind a non-const reference to a temporary object. trying to assign a temporary object, constructed inside some function, to non const reference. `lvalue` = existing object in memory.`rvalue` = temporary non existing object

- a designator cannot be used with a non-aggregate type
  - your class / struct has a member that have a constructor, so your class needs to have constructor. implicitly, the compiler add default constructor, so you can't use designator

- attempting to reference a deleted function / (declared implicitly) cannot be referenced -- it is a deleted function
  - you make a constructor, but by the nature of constructor, it has to be copied. one of the member of your class have a deleted copy function, so it can't be copied. Which implicitly also delete the class copy function