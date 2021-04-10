// Import the dependencies 
var gulp = require('gulp'), 
less = require('gulp-less'), 
minifyCSS = require('gulp-minify-css'); 
// Define a task to compile bootstrap.less 
lessf = function(){ 
return gulp.src(['*/*.less']). 
pipe(less()). 
pipe(minifyCSS({})). 
pipe(gulp.dest('./css/')); 
}; 


// Watch for changes in the less folder 
watchf = function () { 
    gulp.watch('**/*.less', lessf); 
};

watchts = function () { 
    gulp.watch('**/*.ts', tsf); 
};

var ts = require("gulp-typescript");
var tsProject = ts.createProject("tsconfig.json");

tsf = function(){
    return tsProject.src().pipe(tsProject()).js.pipe(gulp.dest("js"));
}

exports.watch = gulp.series(lessf, tsf, gulp.parallel(watchf, watchts))
