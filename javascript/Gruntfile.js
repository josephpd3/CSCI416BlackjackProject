module.exports = function(grunt) {

    require('load-grunt-tasks')(grunt);

    grunt.initConfig({

        babel: {
            options: {
                sourceMap: true
            },
            dist: {
                files: {
                    "dist/poker.js": "src/poker.js"
                }
            }
        }

    });

    grunt.registerTask('default', ['babel']);

}