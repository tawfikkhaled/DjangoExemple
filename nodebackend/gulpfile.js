// Import the dependencies 
const { dest } = require('gulp');
var gulp = require('gulp'), 
less = require('gulp-less'), 
//minifyCSS = require('gulp-minify-css'); 
ts = require("gulp-typescript");


var distPath = './dist/'
var lessPath = './src/**/*.less'
var tsPath = './src/**/*.ts'
var htmlPath = './src/**/*.html'

// Define a task to compile bootstrap.less 
lessf = function(){ 
return gulp.src([lessPath]). 
pipe(less()). 
//pipe(minifyCSS({})). 
pipe(gulp.dest(distPath)); 
}; 


// Watch for changes in the less folder 
watchless = function () { 
    gulp.watch(lessPath, lessf); 
};

watchts = function () { 
    gulp.watch(tsPath, tsf); 
};

var tsProject = ts.createProject("tsconfig.json");

tsf = function(){
    return gulp.src([tsPath]).pipe(tsProject()).js.pipe(gulp.dest(distPath));
}


watchhtml = function () { 
    gulp.watch(htmlPath, htmlf); 
};

htmlf = function(){
    return gulp.src([htmlPath]).pipe(gulp.dest(distPath));
}

exports.watch = gulp.series(lessf, tsf, htmlf, gulp.parallel(watchless, watchts, watchhtml))
