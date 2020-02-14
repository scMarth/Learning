// required plugins
const gulp = require('gulp'),
  less = require('gulp-less'),
  csso = require('gulp-csso'),
  concat = require('gulp-concat'),
  terser = require('gulp-terser'), // apparently gulp-uglify-es is
                                   // deprecated? they say to use this
  jshint = require('gulp-jshint'),
  server = require('gulp-webserver'),
  os = require('os'),
  connect = require('gulp-connect'),
  clean = require('gulp-clean');

// config
const paths = {
  html: 'src/index.html',
  css: 'src/less/*.less',
  js: 'src/js/**/*.js',
  json: 'src/json/*.json',
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

// html
gulp.task('html', () => {
  return gulp.src(paths.html)
    .pipe(gulp.dest(paths.dest))
});

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

// json
gulp.task('json', () => {
  return gulp.src(paths.json)
    .pipe(gulp.dest('build/json'))
});

// server
gulp.task('server', () => {
  connect.server({
    port: 6000,
    root: './',
    open: true
  })

  var browser = os.platform === 'linux'? 'google-chrome'
    : (
      os.platform() === 'darwin' ? 'google-chrome' : (
        os.platform() === 'win32' ? 'chrome' : 'firefox')
          );
  return gulp.src('./')
    .pipe(open({app: '/Applications/Google/Whale.app', uri: 'http://localhost:6000/'}));
});

// clean
gulp.task('clean', () => {
  return gulp.src(paths.dest, options.src.clean)
    .pipe(clean())
});

gulp.task('watch', () => {
  gulp.watch(paths.js, gulp.series('js'));
  gulp.watch(paths.css,  gulp.series('css'));
  gulp.watch(paths.html, gulp.series('html'));
});

gulp.task('default', gulp.series('clean', gulp.parallel('html', 'css', 'js', 'json')));