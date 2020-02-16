# gsl-example

## Building on Windows

1. Clone the gsl-example repository.

1. Download and install [C++ Built Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) from Microsoft.

1. Clone [this](https://github.com/BrianGladman/gsl) gsl repository.

1. From a Developer Command Prompt, navigate to the `build.vc` directory in the gsl repository.

1. Build the gslhdrs project.
    ```
    >MSBuild gslhdrs\gslhdrs.vcxproj -property:Configuration=Release
    ```
1. Build the cbls project.
    ```
    >MSBuild cblaslib\cblaslib.vcxproj -property:Configuration=Release
    ```

1. Build the gslib project.
    ```
    >MSBuild gsllib\gsllib.vcxproj -property:Configuration=Release
    ```

1. Copy the cblas and gsl library files to the `lib` directory of this project. The files are located in `gsl\bluild.vc\lib\<Win32|x64>\Release`.

    * cblas.lib
    * cblas.pdb
    * gsl.lib
    * gsl.pdb

1. Copy the header files from the gsl project to `include\gsl` directory in this repository.

1. In a Developer Command Prompt, navigate to this repository and create a Python virtual environment, activate the environment, and install the requirements.

1. Build and run the executable file.

    ```
    (env) > meson build && ninja -C build
    (env) > build\app\app.exe
    J0(5) = -1.775967713143382642e-01

    ```

1. Build and test the Python extension.

    Navigate to the `python` directory.

    Run the build command.
    ```
    (env) python>python setup.py build_ext --inplace
    ```

    Import the module and test the bessel function.
    ```
    (env) python>python
    Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from example import bessel
    >>> bessel(5)
    -0.17759677131433826
    >>>
    ```

