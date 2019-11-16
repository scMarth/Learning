// required plugins
const gulp = require('gulp'),
  less = require('gulp-less'),
  csso = require('gulp-csso'),
  concat = require('gulp-concat'),
  terser = require('gulp-terser'), // apparently gulp-uglify-es is
                                   // deprecated? they say to use this
  jshint = require('gulp-jshint'),
  clean = require('gulp-clean');

// config
const paths = {
  css: 'src/less/*.less',
  js: 'src/js/**/*.js',
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
};

// css
gulp.task('css', () => {
  return gulp.src(paths.css)
    .pipe(less())
    .pipe(concat('app.styles.min.css'))
    .pipe(csso())
    .pipe(gulp.dest('build/css'))    
});

// js
gulp.task('js', () => {
  return gulp.src(paths.js, options.src.js)
    .pipe(jshint())
    .pipe(jshint.reporter('default', options.jshint_reporter))
    .pipe(concat('app.min.js'))
    .pipe(terser(options.terser))
    .pipe(gulp.dest('build/js', options.dest.js))
});

// clean
gulp.task('clean', () => {
  return gulp.src(paths.dest, options.src.clean)
    .pipe(clean())
});

gulp.task('watch', function(){
  gulp.watch(paths.js, gulp.series('js'));
  gulp.watch(paths.css,  gulp.series('css'));
});

gulp.task('default', gulp.series('clean', gulp.parallel('css', 'js')));