module.exports = function(grunt){

    // Project configuration.
    // concats 1.js and 2.js into scripts.js
    grunt.initConfig({
        watch: {
            js: {
                files: ['js/**/*.js'],
                tasks: ['uglify'],
            },
            css: {
                files: ['css/**/*.css'],
                tasks: ['cssmin'],
            },
        },
        uglify: {
            options: {
                mangle: {
                    toplevel: true
                }
            },
            my_target: {
                files: {
                    'build/js/scripts.min.js': ['js/1.js', 'js/2.js']
                }
            }
        },
        cssmin: {
            options: {
              mergeIntoShorthands: false,
              roundingPrecision: -1
            },
            target: {
              files: {
                'build/css/styles.min.css': ['css/main.css', 'css/theme.css']
              }
            }
          }
    });

    /*
    Load task from npm module
    */
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.registerTask('default',['uglify', 'cssmin', 'watch']);
};