const { src, dest, parallel } = require('gulp');
// const pug = require('gulp-pug');
const less = require('gulp-less');
const uglify = require('gulp-uglify'); // doesn't support let expressions
const minifyCSS = require('gulp-csso');
const concat = require('gulp-concat');

// function html() {
//   return src('client/templates/*.pug')
//     .pipe(pug())
//     .pipe(dest('build/html'))
// }

function css() {
  return src('src/less/*.less')
    .pipe(less())
    .pipe(minifyCSS())
    .pipe(dest('build/css'))
}

function js() {
  return src('src/js/1.js', { sourcemaps: true })
    .pipe(uglify('app.min.js'))
    .pipe(dest('build/js', { sourcemaps: true }))
}

exports.js = js;
exports.css = css;
// exports.html = html;
// exports.default = parallel(html, css, js);
exports.default = parallel(css, js);