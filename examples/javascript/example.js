// insecure_code.js

const http = require('http');
const url = require('url');
const fs = require('fs');
const vm = require('vm');
const mysql = require('mysql');

const server = http.createServer((req, res) => {
    const queryObject = url.parse(req.url, true).query;

    // 代码注入漏洞
    if (queryObject.eval) {
        let code = queryObject.eval;
        vm.runInThisContext(code); // 执行用户输入的代码
    }

    // 文件路径遍历漏洞
    if (queryObject.file) {
        let filename = queryObject.file;
        fs.readFile('/var/www/' + filename, 'utf8', (err, data) => {
            if (err) throw err;
            res.end(data);
        });
    }

    // SQL注入漏洞
    if (queryObject.userId) {
        let userId = queryObject.userId;
        let connection = mysql.createConnection({...});
        let query = `SELECT * FROM users WHERE id = '${userId}'`;
        connection.query(query, (error, results, fields) => {
            if (error) throw error;
            res.end(JSON.stringify(results));
        });
    }

    // 硬编码的密码
    const password = 'P@ssw0rd!';
    console.log('Password is:', password);
});

server.listen(8080);
