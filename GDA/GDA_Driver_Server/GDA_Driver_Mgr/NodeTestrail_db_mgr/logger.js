/**
 * Created by keithfisher on 4/28/14.
 */
//var utils = require('utils');
var log4js = require('log4js');
//var dt="ZZZ";//utils.UtilFN_GetDateTimeNow();
log4js.configure({


    appenders: [
        { type: 'console' },
        { type: 'file', filename: "/Automation/TestResults/Node/_NodeResult.log", category: 'cuc' }
    ]
});

var logger  = log4js.getLogger('cuc');
logger.setLevel('DEBUG');

Object.defineProperty(exports, "LOG", {
    value:logger,
});

