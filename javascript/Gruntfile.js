module.exports = function(grunt) {

    require('load-grunt-tasks')(grunt);

    grunt.initConfig({

        babel: {
            options: {
                sourceMap: true
            },
            dist: {
                files: {
                    "dist/blackjack.js": "src/blackjack.js"
                }
            }
        }

    });

    grunt.registerTask('default', ['babel']);

}