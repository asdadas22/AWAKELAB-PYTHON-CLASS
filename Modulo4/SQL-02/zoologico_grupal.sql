CREATE TABLE area(
	area_id serial PRIMARY KEY,
	nombre_area char(50)
);

CREATE TABLE trabajador(
	trabajador_id serial PRIMARY KEY,
	area_fk_id int NOT NULL,
	rol char(50) NOT NULL,
	telefono char(50) NOT NULL,
	FOREIGN KEY (area_fk_id)
      REFERENCES area (area_id)
);

CREATE TABLE animales(
	animal_id serial PRIMARY KEY,
	animal_nombre char(50),
	area_fk_id int NOT NULL,
	FOREIGN KEY (area_fk_id)
      REFERENCES area (area_id)
);

CREATE TABLE mamiferos(
	mamifero_id serial PRIMARY KEY,
	animal_fk_id int NOT NULL,
	FOREIGN KEY (animal_fk_id)
      REFERENCES animales (animal_id)
);

CREATE TABLE insectos(
	insectos_id serial PRIMARY KEY,
	animal_fk_id int NOT NULL,
	FOREIGN KEY (animal_fk_id)
      REFERENCES animales (animal_id)
);

CREATE TABLE aves(
	aves_id serial PRIMARY KEY,
	animal_fk_id int NOT NULL,
	FOREIGN KEY (animal_fk_id)
      REFERENCES animales (animal_id)
);

CREATE TABLE reptiles(
	reptiles_id serial PRIMARY KEY,
	animal_fk_id int NOT NULL,
	FOREIGN KEY (animal_fk_id)
      REFERENCES animales (animal_id)
);

CREATE TABLE peces(
	peces_id serial PRIMARY KEY,
	animal_fk_id int NOT NULL,
	FOREIGN KEY (animal_fk_id)
      REFERENCES animales (animal_id)
);

CREATE TABLE novedades(
	novedades_id serial PRIMARY KEY,
	detalle char(100) NOT NULL
);