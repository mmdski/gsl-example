sources = ['example.c']
gsl_dep = dependency('gsl')
glib_dep = dependency('glib-2.0')

if target_machine.system() == 'windows'
    examplelib = static_library('example',
                             [sources],
                             include_directories : inc,
                             dependencies : [gsl_dep, glib_dep],
                             name_prefix : '', name_suffix : 'lib')
else
    examplelib = static_library('example',
                             sources,
                             include_directories : inc,
                             dependencies : [gsl_dep, glib_dep])
endif
