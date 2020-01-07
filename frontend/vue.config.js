const path = require('path')

const resolve = dir => path.join(__dirname, dir)

const BASE_URL = process.env.NODE_ENV === 'production' ? '/iview' : '/'

module.exports = {
	devServer: {
		port: 2333,
		open: true,
		proxy: 'http://localhost:4000'
	},
	publicPath: BASE_URL,
	chainWebpack: config => {
		config.resolve.alias
			.set('@', resolve('src'))
			.set('_c', resolve('src/components'))
	},
	productionSourceMap: false
}
