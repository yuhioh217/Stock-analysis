'use strict';

var path = require('path');
var webpack = require('webpack');
var CopyWebpackPlugin = require('copy-webpack-plugin');
var webpackTargetElectronRenderer = require('webpack-target-electron-renderer');
var loaderWithQuery = require('webpack-query-creator');
var fs = require('fs');
var nodeExternals = require('webpack-node-externals');

const museUiThemePath = path.join(
  __dirname,
  'node_modules',
  'muse-ui'
)

var nodeModules = {};
fs.readdirSync('node_modules')
.filter(function(x) {
  return ['.bin'].indexOf(x) === -1;
})
.forEach(function(mod) {
  nodeModules[mod] = 'commonjs ' + mod;
});

var options ={
  target:'node',
  entry: [
    './src/main.js'
  ],
  output: {
    path: path.join(__dirname, 'public/assets'),
    publicPath: '/assets/',
    outputPath: path.join(__dirname, 'assets'),
    filename: 'bundle.js'
  },
  plugins: [
		new webpack.ProvidePlugin({
			'window.moment': 'moment',
			'moment': 'moment'
		}),
    new CopyWebpackPlugin([
      { from: 'src/externals/', to: 'externals' },
    ])
  ],
  module: {
			loaders: [
				{ test: /\.json$/, loader: 'json-loader' },
				{
					test: /\.vue?$/,
					loaders : 'vue-loader' ,//['vue-loader','babel-loader'],
					exclude: /(node_modules|bower_components|vue\/src|vue-router|vendor)/,
          query: {
            presets: [ 'react',
              'es2015',  // ES6 features
              'stage-0', // for React.Component
              'stage-3', // Stable ES7 features(Async/Await)
            ]

          }
				},
        {
          test: /.js$/,
          loader: 'babel-loader',
          exclude: /node_modules/
        },
        {
          test: /muse-ui.src.*?js$/,
          loader: 'babel'
        },
				{ test: /\.css$/, loader: 'style-loader!css-loader' },
				{ test: /\.less$/, loader: 'style!css!less' },
				{ test: /\.png$/,  loader: "url-loader?limit=1000" },
				{ test: /\.jpg$/,  loader: "url-loader?limit=1000" },
				{ test: /\.gif$/,  loader: "url-loader?limit=1000" },
				{ test: /\.woff$/, loader: "url-loader?limit=1000" }
			]
  },
  externals: [
    //nodeExternals(),
    {jQuery: true}
  ],
  resolve: {
    alias: {
      Source: __dirname + '/src',
      'vue$': 'vue/dist/vue.common.js'
    },
    extensions: ['', '.webpack.js', '.web.js', '.js','vue']
  }
};

options.target = webpackTargetElectronRenderer(options);
module.exports = options;
