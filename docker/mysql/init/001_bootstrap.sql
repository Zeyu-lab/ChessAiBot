CREATE TABLE IF NOT EXISTS app_metadata (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    `key` VARCHAR(128) NOT NULL UNIQUE,
    `value` VARCHAR(512) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO app_metadata (`key`, `value`)
VALUES ('schema_bootstrap_version', '0.1B')
ON DUPLICATE KEY UPDATE `value` = VALUES(`value`);