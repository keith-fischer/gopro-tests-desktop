/**
 * Created by keithfisher on 11/25/14.
 */

/**
var Db = require('mongodb').Db;
var Server = require('mongodb').Server;
var dbPort = 27017;
var dbHost = 'localhost';
var dbName = 'db_suite_8554';

var DataBase = function () {
};

module.exports = DataBase;

DataBase.GetDB = function () {
    if (typeof DataBase.db === 'undefined') {
        DataBase.InitDB();
    }
    return DataBase.db;
}

DataBase.InitDB = function () {
    DataBase.db = new Db(dbName, new Server(dbHost, dbPort, {}, {}), { safe: false, auto_reconnect: true });

    DataBase.db.open(function (e, d) {
        if (e) {
            console.log(e);
        } else {
            console.log('connected to database :: ' + dbName);
        }
    });
}

DataBase.Disconnect = function () {
    if (DataBase.db) {
        DataBase.db.close();
    }
}

DataBase.BsonIdFromString = function (id) {
    var mongo = require('mongodb');
    var BSON = mongo.BSONPure;
    return new BSON.ObjectID(id);
}
*/