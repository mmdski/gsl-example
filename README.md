# gsl-example

## Building on Windows

Download and install 
[C++ Built Tools][1] from Microsoft.

### Install pkg-config

#### Install GLib

GLib requires meson and ninja.

```
pip install --user meson ninja
```

1. Clone the [GLib repository][2]. Check out the latest version with Git.

1. Build, test, and install the GLib repository.

    (This will install everything with prefix `C:\`. 
    From a Developer Command Prompt,
    ```
    >mkdir build
    >cd build
    >meson .. --buildtype=release
    >ninja
    >meson test
    >meson install
    ```
1. Place `C:\bin` on your path.

#### Build and install pkg-config
1. Download the [pkg-config][3] source. Unzip the source directory.

1. Modify the `GLIB_PREFIX` variable in the `Makefile.vc` file so the value is 
`C:\`. This points the build configuration to the location of GLib.

    ```
    GLIB_PREFIX = C:\
    ```

1.  Navigate to the source directory in a Developer Command Prompt. From the 
prompt,

    ```
    >nmake /f Makefile.vc CFG=release
    ```

1. Copy the `pkg-config.exe` file from `release\x64` in the pkg-config source 
directory to `C:\bin`.

#### Build and install gsl

1. Clone [this][4] gsl repository.

1. Run a Developer Command Prompt as an administrator. Navigate to the directory
that contains the repository.

1. From the Developer Command Prompt,

```
>mkdir build
>cd build
>cmake -DARCH=64 -DNO_AMPL_BINDINGS=true -DCMAKE_INSTALL_PREFIX=C:\ ..
>cmake --build . --config Release --target gsl
>ctest
>cmake --build . --config Release --target install
```

#### Clone and build this project

1. In a Developer Command Prompt, navigate to this repository and create a Python virtual environment, activate the environment, and install the requirements.

1. Build and run the executable file.

    ```
    (env) > meson build && ninja -C build
    (env) > build\app\app.exe
    J0(5) = -1.775967713143382642e-01

    ```

1. Build and test the Python extension.

    Run the build command.
    ```
    (env) python>python setup.py build_ext --inplace
    ```

    Import the module and test the bessel function.
    ```
    (env) python>python
    Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from example.example import bessel
    >>> bessel(5)
    -0.17759677131433826
    >>>
    ```

[1]: https://visualstudio.microsoft.com/visual-cpp-build-tools/
[2]: https://github.com/GNOME/glib
[3]: https://www.freedesktop.org/wiki/Software/pkg-config/
[4]: https://github.com/ampl/gsl
