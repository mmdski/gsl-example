import os
import platform
import subprocess

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext

try:
    from Cython.Build import cythonize
    use_cython = True
except ImportError:
    use_cython = False

# binary build


class build_ext(_build_ext):

    def copy_glib_dll(self):

        dll_paths = {}

        glib_dll = 'glib-2.0-0.dll'
        intl_dll = 'intl.dll'

        # find the DLLs that are on the path
        for path in os.environ['PATH'].split(';'):
            glib_dll_path = os.path.join(path, glib_dll)
            intl_dll_path = os.path.join(path, intl_dll)
            if os.path.isfile(glib_dll_path) and os.path.isfile(intl_dll_path):
                dll_paths[glib_dll] = glib_dll_path
                dll_paths[intl_dll] = intl_dll_path

        # raise error if the DLLs aren't found
        if len(dll_paths) == 0:
            raise RuntimeError("Unable to find required GLib DLLs")

        ext_filename = self.get_ext_filename('example.example')
        ext_dir, _ = os.path.split(ext_filename)

        for dll, path in dll_paths.items():
            self.copy_file(path, os.path.join(ext_dir, dll))

    def finalize_options(self):

        super().finalize_options()

        if platform.system() == 'Windows':
            self.copy_glib_dll()


def pkgconfig(package, kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    output = subprocess.getoutput(
        'pkg-config --cflags --libs {}'.format(package))
    for token in output.strip().split():
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw


ext = '.pyx' if use_cython else '.c'

example_src = ['src/example.c', 'example/example.pyx']
example_inc = ['include']
extension_kwargs = {
    'sources': example_src,
    'include_dirs': example_inc,
}

extension_kwargs = pkgconfig('gsl', extension_kwargs)
extension_kwargs = pkgconfig('glib-2.0', extension_kwargs)

if platform.system() == 'Windows':
    extension_kwargs['libraries'].remove('m')

example_ext = Extension('example.example', **extension_kwargs)

setup(name="example",
      ext_modules=cythonize([example_ext], annotate=True),
      packages=['example'],
      package_data={'example': ['glib-2.0-0.dll', 'intl.dll']},
      python_requires='>2.7, <3.8',
      cmdclass={'build_ext': build_ext}
      )
