sources = ['example.c']

if target_machine.system() == 'windows'
    examplelib = static_library('example',
                             [sources],
                             include_directories : inc,
                             dependencies : [gsl, cblas],
                             name_prefix : '', name_suffix : 'lib')
else
    examplelib = static_library('example',
                             sources,
                             include_directories : inc,
                             dependencies : [gsl, cblas])
endif
