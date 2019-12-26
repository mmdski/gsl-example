if build_machine.system() == 'windows'
    gsl = cc.find_library('gsl',
        dirs : meson.current_source_dir(),
        static : true)
    cblas = cc.find_library('cblas',
        dirs : meson.current_source_dir(),
        static : true)

elif build_machine.system() == 'linux'
    gsl = cc.find_library('gsl')
    cblas = cc.find_library('gslcblas')

endif
