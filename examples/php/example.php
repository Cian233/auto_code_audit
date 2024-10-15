<?php
// insecure_code.php

// 命令注入漏洞
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    system($cmd);
}

// SQL注入漏洞
if (isset($_GET['userId'])) {
    $userId = $_GET['userId'];
    $conn = new mysqli('localhost', 'user', 'pass', 'db');
    $query = "SELECT * FROM users WHERE id = '$userId'";
    $result = $conn->query($query);
    // 处理结果
}

// 不安全的反序列化
if (isset($_POST['data'])) {
    $data = $_POST['data'];
    $obj = unserialize($data); // 可能导致任意代码执行
}

// 硬编码的密码
$password = 'P@ssw0rd!';
echo "Password is: $password";
?>
