/* globals _comma_separated_list_of_variables_ */


var server = require("./server");
var router = require("./router");
var requestHandlers = require("./requestHandlers");


var handle = {};

//handle["/"] = requestHandlers.start;
//handle["start"] = requestHandlers.start;
//handle["upload"] = requestHandlers.upload;
//handle["RunApp"] = requestHandlers.RunApp;
//handle["CostGuard"] = requestHandlers.CostGuard;
//handle["Transaction"] = requestHandlers.Transaction;
//handle["Report"] = requestHandlers.Report;
//handle["Api"] = requestHandlers.Api;
//handle["PhoneProv"] = requestHandlers.PhoneProv;
//handle["MEIDManager"] = requestHandlers.MEIDManager;
//handle["GoProTestMgr"] = requestHandlers.GoProTestMgr;
//handle["TestRailMgr"]=requestHandlers.TestRailMgr;
//handle["HTTPClient"]=requestHandlers.HTTPClient;
//handle["ETATestDriver"]=requestHandlers.ETATestDriver;//mac
//handle["MTPTestDriver"]=requestHandlers.MTPTestDriver;//win

//handle["CameraTTY"]=requestHandlers.CameraTTY;
handle["gettestrun"]=requestHandlers.gettestrun;
handle["reporttestcase"]=requestHandlers.reporttestcase;
handle["startwebsocketserver"]=requestHandlers.startwebsocketserver;

server.start(router.route, handle);

