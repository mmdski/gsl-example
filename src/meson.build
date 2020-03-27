sources = ['example.c']
gsl_dep = dependency('gsl')

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
