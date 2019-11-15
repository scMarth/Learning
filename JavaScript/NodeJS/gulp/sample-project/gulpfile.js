const { src, dest, parallel } = require('gulp');
const less = require('gulp-less');
const minifyCSS = require('gulp-csso');
const concat = require('gulp-concat');
const terser = require('gulp-terser'); // apparently gulp-uglify-es is deprecated? they say to use this

function css() {
  return src('src/less/*.less')
    .pipe(less())
    .pipe(minifyCSS())
    .pipe(dest('build/css'))
}

function js() {
  return src('src/js/**/*.js', { sourcemaps: true })
    .pipe(concat('app.min.js'))
    .pipe(terser({
      toplevel: true
    }))
    .pipe(dest('build/js', { sourcemaps: true }))
}

exports.js = js;
exports.css = css;
exports.default = parallel(css, js);