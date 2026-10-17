-- Evaluación N.° 2 - Backend
-- Script 3: Otorgar permisos del usuario sobre la base de datos del proyecto

GRANT ALL PRIVILEGES ON stockpyme_db.* TO 'stockpyme_user'@'localhost';
FLUSH PRIVILEGES;
