# Compilation of Errors

## MSVC
- Missing .lib when creating .dll files

With no exported symbols .lib file is not created. (In case of shared libraries, .lib is essentially an import file)

https://stackoverflow.com/questions/64088046/missing-lib-file-when-creating-shared-library-with-cmake-and-visual-studio-2019