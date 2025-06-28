# DROP TABLE IF EXISTS Fahrzeug;
# DROP TABLE IF EXISTS Modell;
# DROP TABLE IF EXISTS MarkeModell;
# DROP TABLE IF EXISTS Marke;
# DROP TABLE IF EXISTS Kraftstoff;
# DROP TABLE IF EXISTS Getriebe;
# DROP PROCEDURE IF EXISTS p_insert_fahrzeug;


CREATE TABLE IF NOT EXISTS Marke (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE
);

# insert  into Marke (name)
# VALUES ("Audi"), ("BMW"), ("Cheverolet"), ("DAF"), ("Harley-Daivdson"),
#        ("Honda"), ("Kia"), ("Mercedes-Benz"), ("Scania"), ("Volkswagen");


CREATE TABLE IF NOT EXISTS Modell (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE
);

# INSERT INTO Modell (name)
# VALUES ("A3"), ("Q7");


CREATE TABLE IF NOT EXISTS MarkeModell (
    id INT PRIMARY KEY AUTO_INCREMENT,
    marke_id INT,
    modell_id INT,
    FOREIGN KEY (marke_id) REFERENCES Marke (id) ON DELETE CASCADE ,
    FOREIGN KEY (modell_id) REFERENCES Modell (id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Kraftstoff(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE
);

# INSERT INTO Kraftstoff (name) VALUES ("Diesel"), ("Benziner");

CREATE TABLE IF NOT EXISTS Getriebe(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE
);

# INSERT INTO Getriebe (name) VALUES ("Automatik"), ("Schaltung");


CREATE TABLE IF NOT EXISTS Fahrzeug(
    id INT PRIMARY KEY AUTO_INCREMENT,
    bild TEXT,
    leistung SMALLINT,
    verbrauch TINYINT,
    anzahl_tueren TINYINT,
    anzahl_sitze TINYINT,
    farbe VARCHAR(100),
    grundpreis DECIMAL(10, 2),
    marke_modell_id INT,
    kraftstoff_id INT,
    getriebe_id INT,
    FOREIGN KEY (marke_modell_id) REFERENCES MarkeModell(id) ON DELETE  CASCADE ,
    FOREIGN KEY (kraftstoff_id) REFERENCES Kraftstoff(id) ON DELETE  CASCADE ,
    FOREIGN KEY (getriebe_id) REFERENCES Getriebe(id) ON DELETE  CASCADE
);

CALL p_insert_marke_model("Audi", "A3");
CALL p_insert_marke_model("BMW", "M3");
#
#
#
#
CALL p_insert_fahrzeug("assets/cars/audi_a3.png", "Audi", "A3",
                       "Benziner", "Automatik", 120, 10, 4, 5, "Schwarz", 30000);
#
CALL p_insert_fahrzeug("assets/cars/bmw_m3.png", "BMW", "M3",
                       "Benziner", "Automatik", 320, 15, 4, 5, "Weiß", 56000);
#



# DROP PROCEDURE IF EXISTS p_insert_fahrzeug;
# DELIMITER $$
# CREATE PROCEDURE IF NOT EXISTS p_insert_fahrzeug(
#     IN in_bild TEXT,
#     IN in_marke_name VARCHAR(100),
#     IN in_modell_name VARCHAR(100),
#     IN in_kraftstoff_name VARCHAR(100),
#     IN in_getriebe_name VARCHAR(100),
#     IN in_leistung SMALLINT,
#     IN in_verbrauch TINYINT,
#     IN in_anzahl_tueren TINYINT,
#     IN in_anzahl_sitze TINYINT,
#     IN in_farbe VARCHAR(100),
#     IN in_grund_preis DECIMAL(10, 2)
# )
# BEGIN
#     DECLARE v_marke_modell_id INT;
#     DECLARE v_kraftstoff_id INT;
#     DECLARE v_getriebe_id INT;
#
#     -- MarkeModell ID ermitteln
#     SELECT MM.id INTO v_marke_modell_id
#     FROM MarkeModell MM
#         JOIN Marke M ON M.id = MM.marke_id
#         JOIN Modell MO ON MO.id = MM.modell_id
#     WHERE M.name = in_marke_name AND MO.name = in_modell_name;
#
#     -- Kraftstoff ID
#     SELECT id INTO v_kraftstoff_id
#     FROM Kraftstoff
#     WHERE name = in_kraftstoff_name;
#
#     -- Getriebe ID
#     SELECT id INTO v_getriebe_id
#     FROM Getriebe
#     WHERE name = in_getriebe_name;
#
#     -- Fahrzeug einfügen
#     INSERT INTO Fahrzeug (
#         bild,
#         leistung,
#         verbrauch,
#         anzahl_tueren,
#         anzahl_sitze,
#         farbe,
#         grundpreis,
#         marke_modell_id,
#         kraftstoff_id,
#         getriebe_id
#     ) VALUES (
#         in_bild,
#         in_leistung,
#         in_verbrauch,
#         in_anzahl_tueren,
#         in_anzahl_sitze,
#         in_farbe,
#         in_grund_preis,
#         v_marke_modell_id,
#         v_kraftstoff_id,
#         v_getriebe_id
#     );
#
# END$$
#
# DELIMITER ;

DROP PROCEDURE IF EXISTS p_delete_fahrzeug_by_modell;

DELIMITER $$

CREATE PROCEDURE IF NOT EXISTS p_delete_fahrzeug_by_modell(
    IN in_model_name VARCHAR(100)
)
BEGIN
    DECLARE v_marke_model_id INT;

    SELECT MM.id INTO v_marke_model_id
    FROM MarkeModell MM
    JOIN Marke MA ON MM.marke_id = MA.id
    JOIN Modell MO ON MM.modell_id = MO.id
    WHERE MO.name = in_model_name;

    DELETE FROM Fahrzeug WHERE marke_modell_id = v_marke_model_id;
    DELETE FROM MarkeModell WHERE id = v_marke_model_id;
    DELETE FROM Modell WHERE name = in_model_name;

END$$

DELIMITER ;

# DELIMITER $$
# CREATE PROCEDURE IF NOT EXISTS p_get_fahrzeuge()
#
# BEGIN
#     SELECT
#         F.id,
#         M.name as marke,
#         MO.name as modell,
#         F.bild,
#         K.name as kraftstoff,
#         G.name as getriebe,
#         F.leistung,
#         F.verbrauch,
#         F.anzahl_tueren,
#         F.anzahl_sitze,
#         F.farbe,
#         F.grundpreis
#     FROM Fahrzeug F
#     JOIN MarkeModell MM on MM.id = F.marke_modell_id
#     JOIN Marke M ON MM.marke_id = M.id
#     JOIN Modell MO ON MM.modell_id = MO.id
#     JOIN Kraftstoff K ON F.kraftstoff_id = K.id
#     JOIN Getriebe G ON F.getriebe_id = G.id;
#
# END$$
#
#
# DELIMITER ;




# DELIMITER $$
# CREATE PROCEDURE IF NOT EXISTS p_get_fahrzeug_by_modell(
#     IN in_modell_name VARCHAR(100)
# )
#
# BEGIN
#     SELECT
#         F.id,
#         M.name as marke,
#         MO.name as modell,
#         F.bild,
#         K.name as kraftstoff,
#         G.name as getriebe,
#         F.leistung,
#         F.verbrauch,
#         F.anzahl_tueren,
#         F.anzahl_sitze,
#         F.farbe,
#         F.grundpreis
#     FROM Fahrzeug F
#     JOIN MarkeModell MM on MM.id = F.marke_modell_id
#     JOIN Marke M ON MM.marke_id = M.id
#     JOIN Modell MO ON MM.modell_id = MO.id
#     JOIN Kraftstoff K ON F.kraftstoff_id = K.id
#     JOIN Getriebe G ON F.getriebe_id = G.id
#     WHERE MO.name = in_modell_name;
#
# END$$
# DELIMITER ;



# DROP PROCEDURE p_insert_marke_model;
#
#
# DELIMITER $$
#
# CREATE PROCEDURE p_insert_marke_model (
#     IN in_marke VARCHAR(100),
#     IN in_modell VARCHAR(100)
# )
# BEGIN
#     DECLARE v_marke_id INT;
#     DECLARE v_modell_id INT;
#
#     -- Hole Marke-ID oder erstelle sie
#     SELECT id INTO v_marke_id
#     FROM Marke
#     WHERE name = in_marke;
#
#     IF v_marke_id IS NULL THEN
#         INSERT INTO Marke (name) VALUES (in_marke);
#         SET v_marke_id = LAST_INSERT_ID();
#     END IF;
#
#     -- Hole Modell-ID oder erstelle sie
#     SELECT id INTO v_modell_id
#     FROM Modell
#     WHERE name = in_modell;
#
#     IF v_modell_id IS NULL THEN
#         INSERT INTO Modell (name) VALUES (in_modell);
#         SET v_modell_id = LAST_INSERT_ID();
#     END IF;
#
#     -- Verknüpfen (falls Kombination noch nicht existiert)
#     IF NOT EXISTS (
#         SELECT 1 FROM MarkeModell
#         WHERE marke_id = v_marke_id AND modell_id = v_modell_id
#     ) THEN
#         INSERT INTO MarkeModell (marke_id, modell_id)
#         VALUES (v_marke_id, v_modell_id);
#     END IF;
#
# END$$
#
# DELIMITER ;
#
#
# call p_insert_marke_model("Hellriser", "A34");
# call p_insert_marke_model("Hellriser", "A35");
#
#
# DELIMITER $$
#
# CREATE PROCEDURE IF NOT EXISTS p_insert_marke(
#     IN m_marke_name VARCHAR(100)
# )
# BEGIN
#     IF NOT EXISTS(
#         SELECT 1 FROM Marke
#                  WHERE m_marke_name = name
#     ) THEN
#         INSERT INTO Marke (name) VALUES (m_marke_name);
#     end if;
# END$$
# DELIMITER ;
#
# CALL p_insert_marke("New");
# CALL p_insert_marke("Tow");
#
#
# DELIMITER $$
#
# CREATE PROCEDURE IF NOT EXISTS p_select_marke(
#     IN m_marke_name VARCHAR(100)
# )
# BEGIN
#     SELECT * FROM Marke WHERE name = m_marke_name;
# END$$
# DELIMITER ;
#
# CALL p_select_marke("Audi");
#
#
















