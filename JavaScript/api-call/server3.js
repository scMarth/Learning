const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();
const port = 3000;

const sql = require('msnodesqlv8');
var config = {
    server: 'localhost\\SQLEXPRESS01',
    database: 'FamilyTree',
    driver: 'msnodesqlv8',
    options: {
        trustedConnection: true
    }
}

sql.connect(config, function(err){
    if (err)
        console.log(err);
    var request = new sql.Request();
    request.query('select * from Members', function(err, records){
        if (err)
            console.log(err);
        else
            console.log(records);
    })
})