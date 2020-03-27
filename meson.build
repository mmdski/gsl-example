project('gsl-example', 'c',
    default_options : ['c_std=c99', 'c_args=-Wall', 'b_ndebug=if-release'],
    version : '0.0.0')

inc = include_directories('include')

cc = meson.get_compiler('c')

glib_dep = dependency('glib-2.0')

subdir('src')
subdir('app')
