-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.10


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO,MYSQL323' */;


--
-- Create schema generalapp_db29179_cie10--

-- CREATE DATABASE IF NOT EXISTS generalapp_db29179_cie10;
USE bienestaruesdb;

--
-- Definition of table `generalapp_db29179_cie10`
--

-- DROP TABLE IF EXISTS `generalapp_db29179_cie10`;
-- CREATE TABLE `generalapp_db29179_cie10` (
--   `id10` varchar(10) NOT NULL,
--   `dec10` varchar(400) DEFAULT NULL,
--   `grp10` varchar(200) DEFAULT NULL,
--   PRIMARY KEY (`id10`)
-- );

--
-- Dumping data for table `generalapp_db29179_cie10`
--

-- data de prueba para las areas de laboratorio clinico
--

-- Disable constraints
--
SET FOREIGN_KEY_CHECKS=0;

-- limpiamos las tablas
--
DELETE FROM `generalapp_examenlab`;
-- DELETE FROM `generalapp_arealab`;

-- usamos TRUNCATE para resetear el contador AUTO_INCREMENT
TRUNCATE TABLE `generalapp_arealab`;

DELETE FROM `generalapp_db29179_cie10`;

DELETE FROM `signosvitalesapp_signosvitales` WHERE `paciente_id`='7777-77';
DELETE FROM `generalapp_consulta` WHERE cod_expediente_id='7777-77';

DELETE FROM `datospersonalesapp_paciente` WHERE codigoPaciente='7777-77';


-- data para expediente clinico de prueba
--
INSERT INTO `datospersonalesapp_paciente` VALUES 
 ('7777-77', 'Ramirez', 'Urquilla', 'Dennis', 'Anderson', 'M', '1987-07-07', 'SOLTERO', '0614-070787-118-9', '03851165-3', NULL, 'EST', 'Urb. Sierra Morena II', '7777-7777', 'anderson@mail.com', 'Santos Ramirez', 'Elena Fuentes', NULL, 'Elena Fuentes', '2222-2222', '2016-10-09 21:14:46', '2016-10-09 21:14:46', 'A', 5, 14, 15, 1);


-- data de prueba para signos vitales
--
INSERT INTO `signosvitalesapp_signosvitales` (`edad`, `presionArterial`, `frecuenciaCardiaca`, `temperatura`, `peso`, `talla`, `frecuenciaRespiratoria`, `fechaIngreso`, `horaIngreso`, `nombreRecibido_id`, `paciente_id`) VALUES 
 (29, '40/300', 150, 40.0, 250, 1.70, 28, '2016-01-25', '11:30:00', 1, '7777-77'),
 (29, '39/280', 140, 37.0, 240, 1.70, 27, '2016-02-25', '11:30:00', 1, '7777-77'),
 (29, '38/260', 130, 34.0, 230, 1.70, 26, '2016-03-25', '11:30:00', 1, '7777-77'),
 (29, '37/240', 120, 31.0, 220, 1.70, 25, '2016-04-25', '11:30:00', 1, '7777-77'),
 (29, '36/220', 110, 28.0, 210, 1.70, 24, '2016-05-25', '11:30:00', 1, '7777-77'),
 
 (29, '34/260', 80, 38.0, 180, 1.70, 20, '2016-08-25', '11:30:00', 1, '7777-77'),
 (29, '33/245', 70, 36.0, 170, 1.70, 19, '2016-09-25', '11:30:00', 1, '7777-77'),
 (29, '32/230', 60, 34.0, 160, 1.70, 18, '2016-10-25', '11:30:00', 1, '7777-77'),
 (29, '31/215', 50, 32.0, 150, 1.70, 17, '2016-11-25', '11:30:00', 1, '7777-77'),
 (29, '30/200', 40, 30.0, 140, 1.70, 16, '2016-12-25', '09:30:00', 1, '7777-77'),
 (29, '40/300', 150, 40.0, 250, 1.70, 28, '2016-12-25', '11:30:00', 1, '7777-77'),
 
 (29, '37/240', 120, 31.0, 220, 1.70, 25, '2016-04-27', '11:50:00', 1, '0009-16'),
 (25, '36/220', 110, 28.0, 210, 1.70, 24, '2016-05-27', '11:50:00', 1, '0008-16'),
 (34, '34/260', 80, 38.0, 180, 1.70, 20, '2016-08-27', '11:50:00', 1, '0007-16'),
 (29, '33/245', 70, 36.0, 170, 1.70, 19, '2016-09-27', '11:50:00', 1, '0003-16'),
 (30, '32/230', 60, 34.0, 160, 1.70, 18, '2016-10-27', '11:50:00', 1, '0001-16');


-- data de prueba para areas de laboratorio clinico
--
INSERT INTO `generalapp_arealab` (`nombreArea`) VALUES 
 ('HEMATOLOGIA'),
 ('QUIMICA_SANGUINEA'),
 ('ORINA'),
 ('HECES'),
 ('INMUNOLOGIA');

-- data de prueba para laboratorio clinico
--
INSERT INTO `generalapp_examenlab` (`nombreExamen`, `codArea_id`) VALUES 
 ('HEMOGRAMA', 1),
 ('LEUCOGRAMA', 1),
 ('HEMOGLOBINA', 1),
 ('HEMATOCRITO', 1),
 ('GOTA_GRUESA', 1),
 ('TIEMPO_DE_SANGRAMIENTO', 1),
 ('TIEMPO_DE_COAGULACION', 1),
 ('T_DE_PROTROMBINA', 1),
 ('T_DE_TROMBOPLASTINA_PARCIAL', 1),
 ('ERITROSEDIMENTACION', 1),
 ('GLUCOSA_EN_AYUNAS', 2),
 ('GLUCOSA_POS_PRANDIAL', 2),
 ('COLESTEROL_TOTAL', 2),
 ('TRIGLICERIDOS', 2),
 ('COLESTEROL_HDL', 2),
 ('COLESTEROL_LDL', 2),
 ('ACIDO_URICO', 2),
 ('UREA', 2),
 ('CREATININA', 2),
 ('BILIRRUBINA', 2),
 ('SGOT', 2),
 ('SGOP', 2),
 ('EXAMEN_GENERAL_DE_ORINA', 3),
 ('PRUEBA_DE_EMBARAZO', 3),
 ('EXAMEN_GENERAL_DE_HECES', 4),
 ('RPR', 5),
 ('PRUEBA_DE_EMBARAZO_EN_SANGRE', 5),
 ('ANTIGENOS_FEBRILES', 5),
 ('GRUPO_SANGUINEO_Y_RH', 5),
 ('HIV', 5);


-- data de prueba para formas farmaceuticas de medicamentos
--
INSERT INTO `generalapp_forma` (`nombre_forma`) VALUES 
 ('Barra'), ('Cápsulas'), ('Champú'), ('Combinación'), ('Comprimidos'),
 ('Crema'), ('Emulsión'), ('Espuma'), ('Gas'), ('Gel'),
 ('Grageas'), ('Granulado'), ('Implante'), ('Jarabe'), ('Líquido'),
 ('Loción'), ('Masticables'), ('Oblea'), ('Óvulos'), ('Pasta'),
 ('Polvo'), ('Pomada'), ('Sistema transdérmico'), ('Sistema de liberación intrauterina'), ('Solución'),
 ('Supositorio'), ('Suspensión'), ('Ungüento');


-- data de prueba para vias de administracion de medicamentos
--
INSERT INTO `generalapp_via` (`nombre_via`) VALUES 
 ('Bucal'), ('Dental'), ('Epidural'), ('Gastroenteral'), ('Intraarterial'),
 ('Intraarticular'), ('Intradiscal'), ('Intramuscular'), ('Intraocular'), ('Intraperitoneal'),
 ('Intrapleural'), ('Intratecal'), ('Intrauterina'), ('Intravenosa'), ('Intravesical'),
 ('Nasal'), ('Oftálmica'), ('Oral'), ('Ötica'), ('Parenteral'),
 ('Rectal'), ('Respiratoria bucal'), ('Respiratoria nasal'), ('Subcutánea'), ('Tópica capilar'),
 ('Tópica dérmica'), ('Tópica mucosa'), ('Transdérmica'), ('Uretral'), ('Vaginal');


-- data de prueba para consulta general
--
INSERT INTO `generalapp_consulta` (`id`,`cod_expediente_id`,`cod_doctor_id`,`nit_paciente`,`fecha`,`tipo_consulta`,`consulta_por`,`presenta_enfermedad`,`antecedentes_personales`,`antecedentes_familiares`,`exploracion_clinica`,`diagnostico_principal`,`otros_diagnosticos`,`tratamiento`,`observaciones`,`created_at`,`updated_at`) VALUES 
 (5550, '7777-77', 1, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sindrome Respiratorio Agudo Severo (SARS)', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (5551, '7777-77', 2, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Dengue', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (5552, '7777-77', 4, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Dengue', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (5553, '7777-77', 5, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Dengue', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 (6660, '0009-16', 12, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Intoxicacion por plaguicidas', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (6661, '0009-16', 13, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Intoxicacion por metales', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (6662, '0009-16', 14, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Varicela', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (6663, '0009-16', 15, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Parotiditis infecciosa', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 (7770, '0008-16', 2, '2456-312464-332-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (7771, '0008-16', 4, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (7772, '0008-16', 5, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (7773, '0008-16', 6, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 (8880, '0007-16', 8, '5464-564654-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infarto Agudo del Miocardio', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (8881, '0007-16', 9, '5464-564654-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (8882, '0007-16', 10, '5464-564654-546-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (8883, '0007-16', 11, '5464-564654-546-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 (9990, '0003-16', 9, '8687-676868-876-8', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (9991, '0003-16', 10, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (9992, '0003-16', 11, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (9993, '0003-16', 12, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 (4440, '0001-16', 13, '1212-121212-121-2', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (4441, '0001-16', 14, '1212-121212-121-2', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (4442, '0001-16', 15, '1212-121212-121-2', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00');

INSERT INTO `generalapp_consulta` (`cod_expediente_id`,`cod_doctor_id`,`nit_paciente`,`fecha`,`tipo_consulta`,`consulta_por`,`presenta_enfermedad`,`antecedentes_personales`,`antecedentes_familiares`,`exploracion_clinica`,`diagnostico_principal`,`otros_diagnosticos`,`tratamiento`,`observaciones`,`created_at`,`updated_at`) VALUES 
 ('7777-77', 6, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Dengue', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 7, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Chikungunya', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 8, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Zika', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 9, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 10, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 11, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 12, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 13, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 14, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 15, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Toxoplasmosis', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 1, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Tuberculosis Extrapulmonar', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 2, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Tuberculosis Pulmonar', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 4, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 5, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 6, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 7, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 8, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 9, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 10, '0614-070787-118-9', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', 11, '0614-070787-118-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis congenita', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0009-16', 1, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 2, '6453-215646-451-3', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 4, '6453-215646-451-3', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 5, '6453-215646-451-3', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 6, '6453-215646-451-3', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 7, '6453-215646-451-3', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 8, '6453-215646-451-3', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 9, '6453-215646-451-3', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 10, '6453-215646-451-3', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 11, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Diarrea y Gastroenteritis', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 12, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Fiebre tifoidea', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 13, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Parasitismo intestinal', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 14, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Conjuntivitis Bacteriana Aguda', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', 15, '6453-215646-451-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion Respiratoria Aguda', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0008-16', 7, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 8, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 9, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 10, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 11, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 12, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 13, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 14, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 15, '2456-312464-332-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 1, '2456-312464-332-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Neumonias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 2, '2456-312464-332-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sintomatico Respiratorio', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 4, '2456-312464-332-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo C', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 5, '2456-312464-332-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Mordedura por Animal Transmisor de Rabia', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 6, '2456-312464-332-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Picadura por Abeja Africanizada', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', 7, '2456-312464-332-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Intoxicacion Alimentaria Aguda', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0007-16', 12, '5464-564654-546-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 13, '5464-564654-546-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 14, '5464-564654-546-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 15, '5464-564654-546-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 1, '5464-564654-546-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 2, '5464-564654-546-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 4, '5464-564654-546-4', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 5, '5464-564654-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Diabetes Mellitus', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 6, '5464-564654-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Desnutricion Proteico Calorica Severa', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 7, '5464-564654-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Obesidad', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', 8, '5464-564654-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Ansiedad', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0003-16', 13, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 14, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 15, '8687-676868-876-8', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Intento suicidio (Conducta Suicida)', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 1, '8687-676868-876-8', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Enfermedad pulmonar obstructiva cronica', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 2, '8687-676868-876-8', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Colon irritable', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 4, '8687-676868-876-8', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 5, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 6, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 7, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 8, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 9, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 10, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 11, '8687-676868-876-8', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', 12, '8687-676868-876-8', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00');


-- nuevo ingreso, expedientes provisionales
-- data de prueba para consulta general
--
INSERT INTO `generalapp_consulta` (`id`,`cod_expediente_id`,`cod_doctor_id`,`nit_paciente`,`fecha`,`tipo_consulta`,`consulta_por`,`presenta_enfermedad`,`antecedentes_personales`,`antecedentes_familiares`,`exploracion_clinica`,`diagnostico_principal`,`otros_diagnosticos`,`tratamiento`,`observaciones`,`created_at`,`updated_at`) VALUES 
 (15000, '3', 1, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sindrome Respiratorio Agudo Severo (SARS)', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (16000, '4', 2, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Dengue', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (17000, '5', 4, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Dengue', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (18000, '6', 5, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Dengue', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (19000, '7', 6, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Dengue', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (14000, '8', 7, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Chikungunya', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 (15001, '3', 11, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (16001, '4', 12, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (17001, '5', 13, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (18001, '6', 14, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (19001, '7', 15, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Toxoplasmosis', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (14001, '8', 1, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Tuberculosis Extrapulmonar', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 (15002, '3', 6, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (16002, '4', 7, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (17002, '5', 8, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (18002, '6', 9, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (19002, '7', 10, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (14002, '8', 11, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis congenita', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 (15003, '3', 15, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Parotiditis infecciosa', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (16003, '4', 1, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (17003, '5', 2, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (18003, '6', 4, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (19003, '7', 5, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 (14003, '8', 6, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00');

INSERT INTO `generalapp_consulta` (`cod_expediente_id`,`cod_doctor_id`,`nit_paciente`,`fecha`,`tipo_consulta`,`consulta_por`,`presenta_enfermedad`,`antecedentes_personales`,`antecedentes_familiares`,`exploracion_clinica`,`diagnostico_principal`,`otros_diagnosticos`,`tratamiento`,`observaciones`,`created_at`,`updated_at`) VALUES 
 ('9', 8, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sospecha de Zika', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 9, '1546-545646-464-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 10, '4567-894654-654-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda de tipo B', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('9', 2, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Tuberculosis Pulmonar', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 4, '1546-545646-464-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 5, '4567-894654-654-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sifilis adquirida', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 
 ('9', 12, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Intoxicacion por plaguicidas', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 13, '1546-545646-464-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Intoxicacion por metales', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 14, '4567-894654-654-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Varicela', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('9', 7, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 8, '1546-545646-464-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 9, '4567-894654-654-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', 10, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo A', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('4', 11, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Diarrea y Gastroenteritis', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', 12, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Fiebre tifoidea', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', 13, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Parasitismo intestinal', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', 14, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Conjuntivitis Bacteriana Aguda', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', 15, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion Respiratoria Aguda', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('9', 2, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 4, '1546-545646-464-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 5, '4567-894654-654-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', 6, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('4', 7, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', 8, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', 9, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', 10, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', 11, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('9', 12, '1231-371783-917-3', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 13, '1546-545646-464-6', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 14, '4567-894654-654-6', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', 15, '8456-432162-136-5', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Influenza', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('4', 1, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Neumonias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', 2, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Sintomatico Respiratorio', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', 4, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hepatitis Aguda tipo C', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', 5, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Mordedura por Animal Transmisor de Rabia', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', 6, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Picadura por Abeja Africanizada', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('9', 7, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Intoxicacion Alimentaria Aguda', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 8, '1546-545646-464-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infarto Agudo del Miocardio', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 9, '4567-894654-654-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', 10, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('4', 11, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', 12, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', 13, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', 14, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', 15, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('9', 1, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 2, '1546-545646-464-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 4, '4567-894654-654-6', '2016-10-24 09:30:00', 'SUB', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Hipertension Arterial', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', 5, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Diabetes Mellitus', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('4', 6, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Desnutricion Proteico Calorica Severa', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', 7, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Obesidad', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', 8, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Ansiedad', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', 9, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', 10, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('9', 11, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 12, '1546-545646-464-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 13, '4567-894654-654-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', 14, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Depresion', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('4', 15, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Intento suicidio (Conducta Suicida)', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', 1, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Enfermedad pulmonar obstructiva cronica', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', 2, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Colon irritable', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', 4, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', 5, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('9', 6, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('1', 7, '1546-545646-464-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('2', 8, '4567-894654-654-6', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', 9, '8456-432162-136-5', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('4', 10, '1546-464486-546-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Infeccion de vias urinarias', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', 11, '2048-092842-084-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', 12, '2938-409238-440-4', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', 13, '1830-912831-083-9', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', 14, '1203-120332-381-0', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('9', 15, '1231-371783-917-3', '2016-10-24 09:30:00', 'PRV', 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 'Diabetes, Hipertension, Obesidad', 'Debilidad, Vista cansada, Temperatura elevada', 'Lumbago', 'Sin diagnosticos secundarios', 'Reposo y medicamentos', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00');


-- data de prueba para referencia interna
-- expediente permanente
-- consulta general
--
INSERT INTO `generalapp_referenciainterna` (`cod_expediente_id`, `cod_doctor_id`, `cod_consulta_id`, `fecha`, `referido_a`, `nombre_paciente`, `tipo_paciente`, `procedencia_paciente`, `motivo_referencia`, `observaciones`, `created_at`, `updated_at`) VALUES 
 ('7777-77', '1', 5550, '2016-10-24 09:30:00', 'Ortopedia', 'Dennis Ramirez', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', '7', 5551, '2016-10-24 09:30:00', 'Medicina Interna', 'Dennis Ramirez', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', '1', 5552, '2016-10-24 09:30:00', 'Nutricionista', 'Dennis Ramirez', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7777-77', '7', 5553, '2016-10-24 09:30:00', 'Dermatologia', 'Dennis Ramirez', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0009-16', '1', 6660, '2016-10-24 09:30:00', 'Ortopedia', 'Luis Linares', 
 'Estudiante', 'Ciencias Agronomicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', '7', 6661, '2016-10-24 09:30:00', 'Medicina Interna', 'Luis Linares', 
 'Estudiante', 'Ciencias Agronomicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', '1', 6662, '2016-10-24 09:30:00', 'Nutricionista', 'Luis Linares', 
 'Estudiante', 'Ciencias Agronomicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0009-16', '7', 6663, '2016-10-24 09:30:00', 'Dermatologia', 'Luis Linares', 
 'Estudiante', 'Ciencias Agronomicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0008-16', '1', 7770, '2016-10-24 09:30:00', 'Ortopedia', 'Ana Hernandez', 
 'Otros', 'Ciencias Economicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', '7', 7771, '2016-10-24 09:30:00', 'Medicina Interna', 'Ana Hernandez', 
 'Otros', 'Ciencias Economicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', '1', 7772, '2016-10-24 09:30:00', 'Nutricionista', 'Ana Hernandez', 
 'Otros', 'Ciencias Economicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0008-16', '7', 7773, '2016-10-24 09:30:00', 'Dermatologia', 'Ana Hernandez', 
 'Otros', 'Ciencias Economicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0007-16', '1', 8880, '2016-10-24 09:30:00', 'Ortopedia', 'Nelson Linares', 
 'Estudiante', 'Ciencias y Humanidades', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', '7', 8881, '2016-10-24 09:30:00', 'Medicina Interna', 'Nelson Linares', 
 'Estudiante', 'Ciencias y Humanidades', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', '1', 8882, '2016-10-24 09:30:00', 'Nutricionista', 'Nelson Linares', 
 'Estudiante', 'Ciencias y Humanidades', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0007-16', '7', 8883, '2016-10-24 09:30:00', 'Dermatologia', 'Nelson Linares', 
 'Estudiante', 'Ciencias y Humanidades', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0003-16', '1', 9990, '2016-10-24 09:30:00', 'Ortopedia', 'Pedro Hernandez', 
 'Administrativo', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', '7', 9991, '2016-10-24 09:30:00', 'Medicina Interna', 'Pedro Hernandez', 
 'Administrativo', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', '1', 9992, '2016-10-24 09:30:00', 'Nutricionista', 'Pedro Hernandez', 
 'Administrativo', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0003-16', '7', 9993, '2016-10-24 09:30:00', 'Dermatologia', 'Pedro Hernandez', 
 'Administrativo', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0001-16', '1', 4440, '2016-10-24 09:30:00', 'Ortopedia', 'Elizabeth Linares', 
 'Estudiante', 'Medicina', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0001-16', '7', 4441, '2016-10-24 09:30:00', 'Medicina Interna', 'Elizabeth Linares', 
 'Estudiante', 'Medicina', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('0001-16', '1', 4442, '2016-10-24 09:30:00', 'Nutricionista', 'Elizabeth Linares', 
 'Estudiante', 'Medicina', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00');


-- data de prueba para referencia externa
-- expediente permanente
-- consulta general
--
INSERT INTO `generalapp_referenciaexterna` (`cod_expediente_id`, `cod_doctor_id`, `cod_consulta_id`, `fecha`, `nombre_paciente`, `edad_paciente`, `sexo_paciente`, `domicilio_paciente`, `telefono_paciente`,
 `presion_arterial`, `frecuencia_cardiaca`, `frecuencia_respiratoria`, `temperatura`, `peso`, `talla`, `consulta_por`, `presenta_enfermedad`, `antecedentes_personales`, `examen_fisico`, `examenes_laboratorio`, `impresion_diagnostica`, `observaciones`, `created_at`, `updated_at`) VALUES 
 ('7777-77', '1', '5551', '2016-10-24 09:30:00', 'Dennis Ramirez', 29, 
 'M', 'Urb. Sierra Morena II', '7777-7777', '40/300', 150, 28, 
 40.0, 250, 1.70, 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 
 'Debilidad, Vista cansada, Temperatura elevada', 'Hemograma, Examen general de orina, Examen general de heces', 'Sospecha de Dengue', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0009-16', '7', '6661', '2016-10-24 09:30:00', 'Luis Linares', 29, 
 'M', 'Colonia los girasoles casa 45', '5456-1321', '37/240', 120, 25, 
 31.0, 220, 1.70, 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 
 'Debilidad, Vista cansada, Temperatura elevada', 'Hemograma, Examen general de orina, Examen general de heces', 'Intoxicacion por metales', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0008-16', '1', '7771', '2016-10-24 09:30:00', 'Ana Hernandez', 25, 
 'F', 'Colonia las golondrinas casa 21', '6453-1546', '36/220', 110, 24, 
 28.0, 210, 1.70, 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 
 'Debilidad, Vista cansada, Temperatura elevada', 'Hemograma, Examen general de orina, Examen general de heces', 'Influenza', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0007-16', '7', '8881', '2016-10-24 09:30:00', 'Nelson Linares', 34, 
 'M', 'Colonia los girasoles casa 12', '5487-6546', '34/260', 80, 20, 
 38.0, 180, 1.70, 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 
 'Debilidad, Vista cansada, Temperatura elevada', 'Hemograma, Examen general de orina, Examen general de heces', 'Hipertension Arterial', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0003-16', '1', '9991', '2016-10-24 09:30:00', 'Pedro Hernandez', 29, 
 'M', 'Residencial los Girasoles, casa 22', '7263-8126', '33/245', 70, 19, 
 36.0, 170, 1.70, 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 
 'Debilidad, Vista cansada, Temperatura elevada', 'Hemograma, Examen general de orina, Examen general de heces', 'Depresion', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('0001-16', '7', '4441', '2016-10-24 09:30:00', 'Elizabeth Linares', 30, 
 'F', 'Carretera Panamericana Km 23 Colonia El Carmen, Pasaje 2 Casa 23', '2122-1312', '32/230', 60, 18, 
 34.0, 160, 1.70, 'Fiebre, Dolor de cabeza y cuerpo, Diarrea', 'Sin padecimientos previos', 'Sin antecedentes personales', 
 'Debilidad, Vista cansada, Temperatura elevada', 'Hemograma, Examen general de orina, Examen general de heces', 'Lumbago', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00');


-- data de prueba para referencia interna
-- expediente provisional
-- consulta general
--
INSERT INTO `generalapp_referenciainterna` (`cod_expediente_id`, `cod_doctor_id`, `cod_consulta_id`, `fecha`, `referido_a`, `nombre_paciente`, `tipo_paciente`, `procedencia_paciente`, `motivo_referencia`, `observaciones`, `created_at`, `updated_at`) VALUES 
 ('3', '1', 15000, '2016-10-24 09:30:00', 'Ortopedia', 'Nelson Gonzalez', 
 'Estudiante', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', '7', 15001, '2016-10-24 09:30:00', 'Medicina Interna', 'Nelson Gonzalez', 
 'Estudiante', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', '1', 15002, '2016-10-24 09:30:00', 'Nutricionista', 'Nelson Gonzalez', 
 'Estudiante', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('3', '7', 15003, '2016-10-24 09:30:00', 'Dermatologia', 'Nelson Gonzalez', 
 'Estudiante', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('4', '1', 16000, '2016-10-24 09:30:00', 'Ortopedia', 'Maria Carcamo', 
 'Estudiante', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('4', '7', 16001, '2016-10-24 09:30:00', 'Medicina Interna', 'Maria Carcamo', 
 'Estudiante', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('4', '1', 16002, '2016-10-24 09:30:00', 'Nutricionista', 'Maria Carcamo', 
 'Estudiante', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('4', '7', 16003, '2016-10-24 09:30:00', 'Dermatologia', 'Maria Carcamo', 
 'Estudiante', 'Jurisprudencia y Ciencias Sociales', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('5', '1', 17000, '2016-10-24 09:30:00', 'Ortopedia', 'Jose Flores', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', '7', 17001, '2016-10-24 09:30:00', 'Medicina Interna', 'Jose Flores', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', '1', 17002, '2016-10-24 09:30:00', 'Nutricionista', 'Jose Flores', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('5', '7', 17003, '2016-10-24 09:30:00', 'Dermatologia', 'Jose Flores', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('6', '1', 18000, '2016-10-24 09:30:00', 'Ortopedia', 'Lorena Linares', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', '7', 18001, '2016-10-24 09:30:00', 'Medicina Interna', 'Lorena Linares', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', '1', 18002, '2016-10-24 09:30:00', 'Nutricionista', 'Lorena Linares', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('6', '7', 18003, '2016-10-24 09:30:00', 'Dermatologia', 'Lorena Linares', 
 'Estudiante', 'Ingenieria y Arquitectura', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('7', '1', 19000, '2016-10-24 09:30:00', 'Ortopedia', 'Daniela Hernandez', 
 'Estudiante', 'Ciencias Economicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', '7', 19001, '2016-10-24 09:30:00', 'Medicina Interna', 'Daniela Hernandez', 
 'Estudiante', 'Ciencias Economicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', '1', 19002, '2016-10-24 09:30:00', 'Nutricionista', 'Daniela Hernandez', 
 'Estudiante', 'Ciencias Economicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('7', '7', 19003, '2016-10-24 09:30:00', 'Dermatologia', 'Daniela Hernandez', 
 'Estudiante', 'Ciencias Economicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 
 ('8', '1', 14000, '2016-10-24 09:30:00', 'Ortopedia', 'Jorge Carcamo', 
 'Estudiante', 'Ciencias Agronomicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', '7', 14001, '2016-10-24 09:30:00', 'Medicina Interna', 'Jorge Carcamo', 
 'Estudiante', 'Ciencias Agronomicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', '1', 14002, '2016-10-24 09:30:00', 'Nutricionista', 'Jorge Carcamo', 
 'Estudiante', 'Ciencias Agronomicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00'),
 ('8', '7', 14003, '2016-10-24 09:30:00', 'Dermatologia', 'Jorge Carcamo', 
 'Estudiante', 'Ciencias Agronomicas', 'Complicaciones en la salud del paciente', 'Sin observaciones', '2016-10-24 09:30:00', '2016-10-24 09:30:00');


-- data de prueba para referencia externa
-- expediente provisional
-- consulta general
--

--
-- pendientes !!!!!
--

-- Enable constraints
--
SET FOREIGN_KEY_CHECKS=1;

-- data de prueba para morbilidades
--
INSERT INTO `generalapp_db29179_cie10` (`id10`,`dec10`,`grp10`) VALUES 
 ('MRB00001','Sindrome Respiratorio Agudo Severo (SARS)',NULL),
 ('MRB00002','Sospecha de Dengue',NULL),
 ('MRB00003','Sospecha de Chikungunya',NULL),
 ('MRB00004','Sospecha de Zika',NULL),
 ('MRB00005','Hepatitis Aguda de tipo B',NULL),
 ('MRB00006','Toxoplasmosis',NULL),
 ('MRB00007','Tuberculosis Extrapulmonar',NULL),
 ('MRB00008','Tuberculosis Pulmonar',NULL),
 ('MRB00009','Sifilis adquirida',NULL),
 ('MRB00010','Sifilis congenita',NULL),
 
 ('MRB00011','Intoxicacion por plaguicidas',NULL),
 ('MRB00012','Intoxicacion por metales',NULL),
 ('MRB00013','Varicela',NULL),
 ('MRB00014','Parotiditis infecciosa',NULL),
 ('MRB00015','Hepatitis Aguda tipo A',NULL),
 ('MRB00016','Diarrea y Gastroenteritis',NULL),
 ('MRB00017','Fiebre tifoidea',NULL),
 ('MRB00018','Parasitismo intestinal',NULL),
 ('MRB00019','Conjuntivitis Bacteriana Aguda',NULL),
 ('MRB00020','Infeccion Respiratoria Aguda',NULL),
 
 ('MRB00021','Influenza',NULL),
 ('MRB00022','Neumonias',NULL),
 ('MRB00023','Sintomatico Respiratorio',NULL),
 ('MRB00024','Hepatitis Aguda tipo C',NULL),
 ('MRB00025','Mordedura por Animal Transmisor de Rabia',NULL),
 ('MRB00026','Picadura por Abeja Africanizada',NULL),
 ('MRB00027','Intoxicacion Alimentaria Aguda',NULL),
 ('MRB00028','Infarto Agudo del Miocardio',NULL),
 ('MRB00029','Hipertension Arterial',NULL),
 ('MRB00030','Diabetes Mellitus',NULL),
 
 ('MRB00031','Desnutricion Proteico Calorica Severa',NULL),
 ('MRB00032','Obesidad',NULL),
 ('MRB00033','Ansiedad',NULL),
 ('MRB00034','Depresion',NULL),
 ('MRB00035','Intento suicidio (Conducta Suicida)',NULL),
 ('MRB00036','Enfermedad pulmonar obstructiva cronica',NULL),
 ('MRB00037','Colon irritable',NULL),
 ('MRB00038','Infeccion de vias urinarias',NULL),
 ('MRB00039','Lumbago',NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
