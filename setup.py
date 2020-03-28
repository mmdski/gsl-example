from setuptools import setup, Extension
from Cython.Build import cythonize
import platform
import subprocess


def pkgconfig(package, kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    output = subprocess.getoutput(
        'pkg-config --cflags --libs {}'.format(package))
    for token in output.strip().split():
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw


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
      packages=['example']
      )
