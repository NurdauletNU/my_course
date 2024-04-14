module.exports = {
  devServer: {
    proxy: {
      '/todos': {
        target: 'http://localhost:8000'
      }
    }
  }
}
