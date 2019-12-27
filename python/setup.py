from setuptools import setup, Extension
from Cython.Build import cythonize
import platform

if platform.system() == 'Linux':
    extension_kwargs = {
        'sources': ['example.pyx'],
        'include_dirs': ["../include/"],
        'libraries': ["gsl", "gslcblas"],
        'extra_objects': ["../build/src/libexample.a"]
    }

ext_modules = [
    Extension("example", **extension_kwargs)
]

setup(name="example",
      ext_modules=cythonize(ext_modules)
      )
