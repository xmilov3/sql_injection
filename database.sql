CREATE DATABASE bsui_lab06;

USE bsui_lab06;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO users (username, password) VALUES
('admin', 'admin123'),
('user1', 'password1'),
('user2', 'password2');
