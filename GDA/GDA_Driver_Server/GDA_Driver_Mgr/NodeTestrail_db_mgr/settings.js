/**
 * Created by keithfisher on 1/30/15.
 */
//var npmInfo = require('./package.json');

module.exports = function(configname){
    console.log("Node Env Variable: " + process.env.NODE_ENV);

    // istanbul ignore next: don't look at the env variables
    //switch(process.env.NODE_ENV){
    switch(configname){
        case null:
        case undefined:
        case "local":
            return {
                env: 'local', //should be env/prod
                //dbURI : "mongodb://localhost/" + npmInfo.name,
                expressPort: 3000,
                loggerLevel: 'info'
            };
        case "dev":
        case "development":
            return {
                env: 'dev', //should be env/prod
                //dbURI : process.env.MONGODB_URI,
                //expressPort: process.env.PORT,
                loggerLevel: 'info'
            };
        case "test":
        case "testing":
            return {
                env: 'test', //should be env/prod, can be changed to prod when we are comfy with prod environ
                //dbURI : process.env.MONGODB_URI,
                //expressPort: process.env.PORT,
                loggerLevel: 'debug'

            };
        case "prod":
        case "production":
            return {
                env: 'prod', //should be env/prod, can be changed to prod when we are comfy with prod environ
                //dbURI : process.env.MONGODB_URI,
                //expressPort: process.env.PORT,
                loggerLevel: 'debug'

            };
        default:
            throw new Error("Environment Not Recognized");

    }
}();

//var config = require('./config.js');
//config.expressPort; //this will be equal to 3000 for local env