-- SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.

CREATE TRIGGER update_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		UPDATE users SET NEW.valid_email = 0 WHERE id = NEW.id;
	END IF;
END;
