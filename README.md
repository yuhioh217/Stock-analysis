Koa2-Vue-Stock-App

=================

Stock Analysis by KE Jiang

Features
-

* Use koa2/Vue/Webpack and muse-ui/moment.

Howto
-

Need to install the webpack and electron first(npm install -g).

'npm install' to install the dependencies.
'npm run build' to build the bundle.js.
'npm run start' to run the koa2 service with nodemon.

## Project Structure
```
.
├── bin               // Start the app.js with babel.
├── routes            // Server API Routings.
├── src               // Theme system with React.
│   ├── externals     // CSS/JS files from third-party.
│   ├── images        // image files.
│   └── js            // Javascript files.
│   └── css           // CSS files.
│   └── components    // vue components
└── views             // Theme templates of page(html/jade).
```

## Node modules
* [babel](https://babeljs.io/) Use Async/Await and other stable ES7 features
  * babel-core >>For Test functions
  * babel-polyfill >>Help Mocha to run js written in babel
  * babel-preset-es2015 >>ES6 features
  * babel-preset-stage-3 >>Stable ES7 features(Async/Await)
* [Koa](http://koajs.com/)
  * koa-bodyparser
  * koa-convert >>Use legacy middlewares from koa
  * koa-logger >>Development routes action logger
  * koa-router
* [nodemon](http://nodemon.io/) >> Automatically reload changes

License
-
Licensed under the MIT License

Authors
-
Copyright(c) 2017 KE Jiang<<yuihoh217@gmail.com>>
