// required plugins
const gulp = require('gulp'),
      csso = require('gulp-csso'),
      concat = require('gulp-concat'),
      terser = require('gulp-terser'),
      jshint = require('gulp-jshint'),
      connect = require('gulp-connect'),
      clean = require('gulp-clean');
     
// config
const paths = {
    html: 'src/index.html',
    css: 'src/css/*.css',
    js: 'src/js/**/*.js',
    json: 'src/json/*.json',
    lib: 'src/lib/*.js',
    images: 'src/images/**/*.png',
    dest: 'build'
},
options = {
    jshint_reporter: [
        {
          verbose: true
        }
    ],
    src: {
        clean: {
            allowEmpty: true
        },
        js: {
            sourcemaps: false
        }
    },
    dest: {
        js: {
            sourcemaps: false // disable printing of info that can be used to
                              // map code within compressed file back to its
                              // original source
        }
    },
    terser: {
        toplevel: true // mangles top level variable names and drops unused
                       // functions and variables
    }
}

// html
gulp.task('html', () => {
    return gulp.src(paths.html)
        .pipe(gulp.dest(paths.dest))
        .pipe(connect.reload());
});

// images
gulp.task('images', () => {
    return gulp.src(paths.images)
        .pipe(gulp.dest('build/images'));
});

// json
gulp.task('json', () => {
    return gulp.src(paths.json)
        .pipe(gulp.dest('build/json'));
});

// lib
gulp.task('lib', () => {
    return gulp.src(paths.lib)
        .pipe(gulp.dest('build/lib'));
})

// css
gulp.task('css', () => {
    return gulp.src(paths.css)
        .pipe(concat('app.styles.min.css'))
        .pipe(csso())
        .pipe(gulp.dest('build/css'))
        .pipe(connect.reload());
});

// js
gulp.task('js', () => {
    return gulp.src(paths.js, options.src.js)
        .pipe(jshint())
        .pipe(jshint.reporter('default', options.jshint_reporter))
        .pipe(concat('app.min.js'))
        .pipe(terser(options.terser))
        .pipe(gulp.dest('build/js', options.dest.js))
        .pipe(connect.reload());
});

// clean
gulp.task('clean', () => {
    return gulp.src(paths.dest, options.src.clean)
        .pipe(clean())
});

gulp.task('server', function() {
    connect.server({
        root: paths.dest,
        // root: 'test',
        livereload: true
    });
});

gulp.task('watch', function(){
    gulp.watch(paths.js, gulp.series('js'));
    gulp.watch(paths.css,  gulp.series('css'));
    gulp.watch(paths.html, gulp.series('html'));
});

// gulp.task('default', gulp.series('clean', gulp.parallel('html', 'images', 'lib', 'json', 'css', 'js')));
gulp.task('default', gulp.parallel('server', 'watch'));