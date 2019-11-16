const { src, dest, parallel, watch, series } = require('gulp');
const less = require('gulp-less');
const minifyCSS = require('gulp-csso');
const concat = require('gulp-concat');
const terser = require('gulp-terser'); // apparently gulp-uglify-es is deprecated? they say to use this
const jshint = require('gulp-jshint');

const paths = {
  css: 'src/less/*.less',
  js: 'src/js/**/*.js'
}

function css() {
  return src(paths.css)
    .pipe(less())
    .pipe(minifyCSS())
    .pipe(dest('build/css'))
}

function js() {
  return src(paths.js, { sourcemaps: true })
    .pipe(jshint())
    .pipe(jshint.reporter('default', { verbose: true }))
    .pipe(concat('app.min.js'))
    .pipe(terser({
      toplevel: true
    }))
    .pipe(dest('build/js', { sourcemaps: true }))
}

watch(paths.js, js);
watch(paths.css, css);

exports.js = js;
exports.css = css;
exports.default = parallel(css, js);


/*

https://github.com/terser/terser#minify-options

Note, concat is called before terser because the 'toplevel' option, which mangles
top level variable names and drops unused functions and variables

To-Do:
  jshint

*/