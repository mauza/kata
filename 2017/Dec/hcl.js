const launchChrome = require('@serverless-chrome/lambda')
const CDP = require('chrome-remote-interface')
 
module.exports.handler = function handler (event, context, callback) {
  launchChrome({
    flags: ['--window-size=1280x1696', '--hide-scrollbars']
  })
  .then((chrome) => {
    // Chrome is now running on localhost:9222
 
    CDP.Version()
      .then((versionInfo) => {
        callback(null, {
          versionInfo,
        })
      })
      .catch((error) => {
        callback(error)
      })
  })
  // Chrome didn't launch correctly 😢
  .catch(callback)
}