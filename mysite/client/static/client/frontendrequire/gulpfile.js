// Import the dependencies 
var gulp = require('gulp'), 
less = require('gulp-less'), 
//minifyCSS = require('gulp-minify-css'); 
ts = require("gulp-typescript");

// Define a task to compile bootstrap.less 
lessf = function(){ 
return gulp.src(['*/*.less']). 
pipe(less()). 
//pipe(minifyCSS({})). 
pipe(gulp.dest('./js/')); 
}; 


// Watch for changes in the less folder 
watchless = function () { 
    gulp.watch('**/*.less', lessf); 
};

watchts = function () { 
    gulp.watch('**/*.ts', tsf); 
};

var tsProject = ts.createProject("tsconfig.json");

tsf = function(){
    return gulp.src(['*/*.ts']).pipe(tsProject()).js.pipe(gulp.dest("./js/"));
}


watchhtml = function () { 
    gulp.watch('**/*.ts', tsf); 
};

htmlf = function(){
    return gulp.src(['*/*.html']).pipe(gulp.dest("./js/"));
}

exports.watch = gulp.series(lessf, tsf, htmlf, gulp.parallel(watchless, watchts, watchhtml))
