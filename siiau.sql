CREATE TABLE materia(
    id INT PRIMARY KEY AUTO_INCREMENT,
    clave VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    creditos INT NOT NULL
);

CREATE TABLE seccion(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE profesor(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE edificio(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE aula(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    id_edificio INT NOT NULL,
    FOREIGN KEY (id_edificio) REFERENCES edificio(id)
);

CREATE TABLE ciclo(
    id INT PRIMARY KEY AUTO_INCREMENT,
    datos VARCHAR(255) NOT NULL
);

CREATE TABLE horario(
    id int PRIMARY KEY AUTO_INCREMENT,
    datos VARCHAR(255) NOT NULL
);

CREATE TABLE dias(
    id INT PRIMARY KEY AUTO_INCREMENT,
    datos VARCHAR(255) NOT NULL
);

CREATE TABLE curso(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nrc INT NOT NULL,
    cupos INT NOT NULL,
    cupos_disponibles INT NOT NULL,
    id_materia INT NOT NULL,
    id_seccion INT NOT NULL,
    id_profesor INT NOT NULL,
    id_ciclo INT NOT NULL,
    FOREIGN KEY (id_materia) REFERENCES materia(id),
    FOREIGN KEY (id_seccion) REFERENCES seccion(id),
    FOREIGN KEY (id_profesor) REFERENCES profesor(id),
    FOREIGN KEY (id_ciclo) REFERENCES ciclo(id)
);

CREATE TABLE agenda_curso(
    id_curso INT NOT NULL,
    id_horario INT NOT NULL,
    id_dias INT NOT NULL,
    id_aula INT NOT NULL,
    FOREIGN KEY (id_curso) REFERENCES curso(id),
    FOREIGN KEY (id_horario) REFERENCES horario(id),
    FOREIGN KEY (id_dias) REFERENCES dias(id),
    FOREIGN KEY (id_aula) REFERENCES aula(id)
);

CREATE TABLE carrera(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE catalogo_carrera(
    id_curso INT NOT NULL,
    id_carrera INT NOT NULL,
    FOREIGN KEY (id_curso) REFERENCES curso(id),
    FOREIGN KEY (id_carrera) REFERENCES carrera(id)
);

ALTER DATABASE oferta_academica CHARACTER SET utf8 COLLATE utf8_general_ci;

ALTER TABLE profesor CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE materia CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;