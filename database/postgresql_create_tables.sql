DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public IS 'standard public schema';


CREATE TABLE "student" (
	"student_id" serial NOT NULL,
	"first_name" varchar(50) NOT NULL,
	"last_name" varchar(50) NOT NULL,
	"email" varchar(50) NOT NULL,
	"active" BOOLEAN NOT NULL,
	"health_group_id" integer NOT NULL,
	CONSTRAINT "student_pk" PRIMARY KEY ("student_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "trainer" (
	"trainer_id" serial NOT NULL,
	"first_name" varchar(50) NOT NULL,
	"last_name" varchar(50) NOT NULL,
	"email" varchar(50) NOT NULL,
	"active" BOOLEAN NOT NULL,
	CONSTRAINT "trainer_pk" PRIMARY KEY ("trainer_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "admin" (
	"admin_id" integer NOT NULL,
	"first_name" varchar(50) NOT NULL,
	"last_name" varchar(50) NOT NULL,
	"email" varchar(50) NOT NULL,
	"active" BOOLEAN NOT NULL,
	CONSTRAINT "admin_pk" PRIMARY KEY ("admin_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "group" (
	"group_id" serial NOT NULL,
	"name" varchar(10) NOT NULL,
	"max_students_number" integer,
	"health_group_id" integer,
	CONSTRAINT "group_pk" PRIMARY KEY ("group_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "class" (
	"class_id" integer NOT NULL,
	"group_id" integer NOT NULL,
	"date_time" timestamp NOT NULL,
	"duration" interval NOT NULL,
	CONSTRAINT "class_pk" PRIMARY KEY ("class_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "trainer_enrollment" (
	"trainer_id" integer NOT NULL,
	"group_id" integer NOT NULL,
	CONSTRAINT "trainer_enrollment_pk" PRIMARY KEY ("trainer_id","group_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "student_enrollment" (
	"student_id" integer NOT NULL,
	"group_id" integer NOT NULL,
	CONSTRAINT "student_enrollment_pk" PRIMARY KEY ("group_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "attendance" (
	"student_id" integer NOT NULL,
	"class_id" integer NOT NULL,
	"presence" BOOLEAN NOT NULL,
	CONSTRAINT "attendance_pk" PRIMARY KEY ("student_id","class_id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "health_group" (
	"health_group_id" serial NOT NULL,
	"name" varchar(20) NOT NULL,
	CONSTRAINT "health_group_pk" PRIMARY KEY ("health_group_id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE "student" ADD CONSTRAINT "student_fk0" FOREIGN KEY ("health_group_id") REFERENCES "health_group"("health_group_id");

ALTER TABLE "group" ADD CONSTRAINT "group_fk0" FOREIGN KEY ("health_group_id") REFERENCES "health_group"("health_group_id");

ALTER TABLE "class" ADD CONSTRAINT "class_fk0" FOREIGN KEY ("group_id") REFERENCES "group"("group_id");

ALTER TABLE "trainer_enrollment" ADD CONSTRAINT "trainer_enrollment_fk0" FOREIGN KEY ("trainer_id") REFERENCES "trainer"("trainer_id");
ALTER TABLE "trainer_enrollment" ADD CONSTRAINT "trainer_enrollment_fk1" FOREIGN KEY ("group_id") REFERENCES "group"("group_id");

ALTER TABLE "student_enrollment" ADD CONSTRAINT "student_enrollment_fk0" FOREIGN KEY ("student_id") REFERENCES "student"("student_id");
ALTER TABLE "student_enrollment" ADD CONSTRAINT "student_enrollment_fk1" FOREIGN KEY ("group_id") REFERENCES "group"("group_id");

ALTER TABLE "attendance" ADD CONSTRAINT "attendance_fk0" FOREIGN KEY ("student_id") REFERENCES "student"("student_id");
ALTER TABLE "attendance" ADD CONSTRAINT "attendance_fk1" FOREIGN KEY ("class_id") REFERENCES "student"("student_id");


