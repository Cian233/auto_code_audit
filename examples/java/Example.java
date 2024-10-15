// InsecureCode.java

import java.io.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class InsecureCode extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // 命令注入漏洞
        String cmd = request.getParameter("cmd");
        Runtime.getRuntime().exec(cmd);

        // SQL注入漏洞
        String userId = request.getParameter("userId");
        String query = "SELECT * FROM users WHERE id = '" + userId + "'";
        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/db", "user", "pass");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            // 处理结果集
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // 不安全的反序列化
        ObjectInputStream ois = new ObjectInputStream(request.getInputStream());
        try {
            Object obj = ois.readObject();
            // 使用反序列化的对象
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        // 硬编码的密码
        String password = "P@ssw0rd!";
        System.out.println("Password is: " + password);
    }
}
