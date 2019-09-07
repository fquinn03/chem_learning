-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: chemlearning.mysql.pythonanywhere-services.com    Database: chemlearning$ChemLearning
-- ------------------------------------------------------
-- Server version	5.6.40-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add class_id',7,'add_class_id'),(20,'Can change class_id',7,'change_class_id'),(21,'Can delete class_id',7,'delete_class_id'),(22,'Can add school',8,'add_school'),(23,'Can change school',8,'change_school'),(24,'Can delete school',8,'delete_school'),(25,'Can add student profile',9,'add_studentprofile'),(26,'Can change student profile',9,'change_studentprofile'),(27,'Can delete student profile',9,'delete_studentprofile'),(28,'Can add teacher profile',10,'add_teacherprofile'),(29,'Can change teacher profile',10,'change_teacherprofile'),(30,'Can delete teacher profile',10,'delete_teacherprofile'),(31,'Can add lesson',11,'add_lesson'),(32,'Can change lesson',11,'change_lesson'),(33,'Can delete lesson',11,'delete_lesson'),(34,'Can add exam',12,'add_exam'),(35,'Can change exam',12,'change_exam'),(36,'Can delete exam',12,'delete_exam'),(37,'Can add question',13,'add_question'),(38,'Can change question',13,'change_question'),(39,'Can delete question',13,'delete_question'),(40,'Can add Written_Question',14,'add_written_question'),(41,'Can change Written_Question',14,'change_written_question'),(42,'Can delete Written_Question',14,'delete_written_question'),(43,'Can add MCQ_Question',15,'add_mcq_question'),(44,'Can change MCQ_Question',15,'change_mcq_question'),(45,'Can delete MCQ_Question',15,'delete_mcq_question'),(46,'Can add Formula_Question',16,'add_formula_question'),(47,'Can change Formula_Question',16,'change_formula_question'),(48,'Can delete Formula_Question',16,'delete_formula_question'),(49,'Can add answer',17,'add_answer'),(50,'Can change answer',17,'change_answer'),(51,'Can delete answer',17,'delete_answer'),(52,'Can add user answer',18,'add_useranswer'),(53,'Can change user answer',18,'change_useranswer'),(54,'Can delete user answer',18,'delete_useranswer'),(55,'Can add completed exam',19,'add_completedexam'),(56,'Can change completed exam',19,'change_completedexam'),(57,'Can delete completed exam',19,'delete_completedexam'),(58,'Can add incorrect answer',20,'add_incorrectanswer'),(59,'Can change incorrect answer',20,'change_incorrectanswer'),(60,'Can delete incorrect answer',20,'delete_incorrectanswer');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$sZOW4Uyu5Mrc$lcR2rnP8Wphon2sdpaz/unn8X1ueSxg8e44b0UXeamo=','2019-09-06 12:49:04.733122',1,'fquinn03','','','fionaqui@gmail.com',1,1,'2019-08-23 08:18:34.641235'),(2,'pbkdf2_sha256$100000$qaKyI33Wu0Z8$EPzUY/lo6MQPPuO2p7joVoFVksVwvrV4N5r0vh0CbQA=','2019-09-05 20:51:05.910589',0,'Miss_Quinn','','','',0,1,'2019-09-04 12:32:28.155960'),(3,'pbkdf2_sha256$100000$RIscnRGQV5pe$KMR0RMmYC7BA3kWt4+AVLUZGI7ZaQLanZFSbZDxqZ4w=','2019-09-05 12:20:55.981830',0,'Student1','','','',0,1,'2019-09-04 12:37:55.000000'),(4,'pbkdf2_sha256$100000$vUCu3vt2g7x3$ofV8eXahv9r1PUpPtMEg1NHi8ELwGLOHfAJ5syDx9IE=','2019-09-05 12:25:58.397817',0,'student2','','','',0,1,'2019-09-05 12:25:57.812644'),(5,'pbkdf2_sha256$100000$TVZ2LsRknkqy$0VvgAr0V9r8foZo4mUNbE21TCk41kBE88UFX6o013Og=','2019-09-05 12:59:49.733486',0,'student3','','','',0,1,'2019-09-05 12:59:49.270229'),(6,'pbkdf2_sha256$100000$lf2hrSvBtzxS$iIdPUxC57KfNV/DFNcHO3L5KJY8Spmy3Q2Wah05fAMo=','2019-09-05 13:06:28.921167',0,'student4','','','',0,1,'2019-09-05 13:06:28.406719'),(7,'pbkdf2_sha256$100000$XQWYcfo1DuK4$qRjny49dACwD2ElBDeN7nAoi0pPReu7rS6v8/gPgeKo=','2019-09-05 14:21:10.261396',0,'student5','','','',0,1,'2019-09-05 13:08:54.844680'),(8,'pbkdf2_sha256$100000$dSfbxPOUaS96$dwCwRGODDJ4WZsG6ACv9yQI5Mu4euHtATM0vSUq+lWg=','2019-09-05 20:45:54.394396',0,'student6','','','',0,1,'2019-09-05 13:13:37.926210'),(9,'pbkdf2_sha256$100000$qOtWt5iydUK4$hDbtn/wuIev6T3ueWHQClveJBPSAwCzNqWFsLmFAZts=','2019-09-06 06:25:03.744914',0,'student7','','','',0,1,'2019-09-05 17:30:30.897874'),(10,'pbkdf2_sha256$100000$POpqCJIAQzoW$TOIuObhuYsRi7jwXZ/coC3B2vJ1rw0gg2hgKFrVVw6U=','2019-09-06 12:48:14.856511',0,'student12','','','',0,1,'2019-09-05 18:02:44.631332'),(11,'pbkdf2_sha256$100000$cJ2i44qK9RFe$q2+WO4hT4fV/b580oii4YROygvSKqjQSKH0/3YNaYr0=','2019-09-05 20:49:19.653193',0,'student13','','','',0,1,'2019-09-05 20:49:19.348496');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_users_class_id`
--

DROP TABLE IF EXISTS `custom_users_class_id`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_users_class_id` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `custom_users_class_i_teacher_id_04726950_fk_custom_us` (`teacher_id`),
  CONSTRAINT `custom_users_class_i_teacher_id_04726950_fk_custom_us` FOREIGN KEY (`teacher_id`) REFERENCES `custom_users_teacherprofile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_users_class_id`
--

LOCK TABLES `custom_users_class_id` WRITE;
/*!40000 ALTER TABLE `custom_users_class_id` DISABLE KEYS */;
INSERT INTO `custom_users_class_id` VALUES (1,'10Sc2',2),(2,'Year 7s',2);
/*!40000 ALTER TABLE `custom_users_class_id` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_users_school`
--

DROP TABLE IF EXISTS `custom_users_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_users_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `post_code` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_users_school`
--

LOCK TABLES `custom_users_school` WRITE;
/*!40000 ALTER TABLE `custom_users_school` DISABLE KEYS */;
INSERT INTO `custom_users_school` VALUES (1,'La Sainte Union','NW5 1RP');
/*!40000 ALTER TABLE `custom_users_school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_users_studentprofile`
--

DROP TABLE IF EXISTS `custom_users_studentprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_users_studentprofile` (
  `user_id` int(11) NOT NULL,
  `is_student` tinyint(1) NOT NULL,
  `is_teacher` tinyint(1) NOT NULL,
  `level` int(11) NOT NULL,
  `attempt` int(11) NOT NULL,
  `next_lesson_id` int(11) NOT NULL,
  `next_exam_id` int(11) NOT NULL,
  `details_added` tinyint(1) NOT NULL,
  `signup_quiz_completed` tinyint(1) NOT NULL,
  `needs_help` tinyint(1) NOT NULL,
  `progress` int(11) NOT NULL,
  `starting_level` int(11) NOT NULL,
  `class_id_id` int(11) DEFAULT NULL,
  `school_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `custom_users_student_class_id_id_3c67fc7f_fk_custom_us` (`class_id_id`),
  KEY `custom_users_student_school_id_d17e8458_fk_custom_us` (`school_id`),
  KEY `custom_users_student_teacher_id_37d462ad_fk_custom_us` (`teacher_id`),
  CONSTRAINT `custom_users_student_class_id_id_3c67fc7f_fk_custom_us` FOREIGN KEY (`class_id_id`) REFERENCES `custom_users_class_id` (`id`),
  CONSTRAINT `custom_users_student_school_id_d17e8458_fk_custom_us` FOREIGN KEY (`school_id`) REFERENCES `custom_users_school` (`id`),
  CONSTRAINT `custom_users_student_teacher_id_37d462ad_fk_custom_us` FOREIGN KEY (`teacher_id`) REFERENCES `custom_users_teacherprofile` (`user_id`),
  CONSTRAINT `custom_users_studentprofile_user_id_29d4c863_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_users_studentprofile`
--

LOCK TABLES `custom_users_studentprofile` WRITE;
/*!40000 ALTER TABLE `custom_users_studentprofile` DISABLE KEYS */;
INSERT INTO `custom_users_studentprofile` VALUES (3,1,0,1,1,1,1,1,1,0,2,1,1,1,2),(4,1,0,1,1,1,1,1,1,0,2,1,1,1,2),(5,1,0,1,1,1,1,1,1,0,2,1,1,1,2),(6,1,0,1,1,1,1,1,1,0,2,1,1,1,2),(7,1,0,1,1,1,1,1,1,0,2,1,1,1,2),(8,1,0,1,3,2,2,1,1,1,2,1,1,1,2),(9,1,0,1,1,3,3,1,1,0,2,1,1,1,2),(10,1,0,2,2,7,5,1,1,0,2,1,1,1,2),(11,1,0,1,1,1,1,1,0,0,2,1,2,1,2);
/*!40000 ALTER TABLE `custom_users_studentprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_users_studentprofile_completed_lessons`
--

DROP TABLE IF EXISTS `custom_users_studentprofile_completed_lessons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_users_studentprofile_completed_lessons` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentprofile_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `custom_users_studentprof_studentprofile_id_lesson_9a3d54f7_uniq` (`studentprofile_id`,`lesson_id`),
  KEY `custom_users_student_lesson_id_40336c16_fk_lessons_l` (`lesson_id`),
  CONSTRAINT `custom_users_student_lesson_id_40336c16_fk_lessons_l` FOREIGN KEY (`lesson_id`) REFERENCES `lessons_lesson` (`id`),
  CONSTRAINT `custom_users_student_studentprofile_id_eb7062c4_fk_custom_us` FOREIGN KEY (`studentprofile_id`) REFERENCES `custom_users_studentprofile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_users_studentprofile_completed_lessons`
--

LOCK TABLES `custom_users_studentprofile_completed_lessons` WRITE;
/*!40000 ALTER TABLE `custom_users_studentprofile_completed_lessons` DISABLE KEYS */;
INSERT INTO `custom_users_studentprofile_completed_lessons` VALUES (1,3,1),(15,7,1),(27,8,1),(28,8,3),(38,9,1),(51,10,1);
/*!40000 ALTER TABLE `custom_users_studentprofile_completed_lessons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_users_teacherprofile`
--

DROP TABLE IF EXISTS `custom_users_teacherprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `custom_users_teacherprofile` (
  `user_id` int(11) NOT NULL,
  `is_teacher` tinyint(1) NOT NULL,
  `is_student` tinyint(1) NOT NULL,
  `details_added` tinyint(1) NOT NULL,
  `school_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `custom_users_teacher_school_id_0c64d615_fk_custom_us` (`school_id`),
  CONSTRAINT `custom_users_teacher_school_id_0c64d615_fk_custom_us` FOREIGN KEY (`school_id`) REFERENCES `custom_users_school` (`id`),
  CONSTRAINT `custom_users_teacherprofile_user_id_10baba03_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_users_teacherprofile`
--

LOCK TABLES `custom_users_teacherprofile` WRITE;
/*!40000 ALTER TABLE `custom_users_teacherprofile` DISABLE KEYS */;
INSERT INTO `custom_users_teacherprofile` VALUES (2,1,0,1,1);
/*!40000 ALTER TABLE `custom_users_teacherprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=335 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-09-04 12:32:28.300917','2','Miss_Quinn',1,'[{\"added\": {}}]',4,1),(2,'2019-09-04 12:36:09.211783','1','La Sainte Union, NW5 1RP',1,'[{\"added\": {}}]',8,1),(3,'2019-09-04 12:36:34.691355','2','Miss_Quinn',1,'[{\"added\": {}}]',10,1),(4,'2019-09-04 12:36:42.064696','2','Miss_Quinn',2,'[{\"changed\": {\"fields\": [\"details_added\"]}}]',10,1),(5,'2019-09-04 12:36:58.558488','1','Year 10',1,'[{\"added\": {}}]',7,1),(6,'2019-09-04 12:37:09.688682','1','10Sc2',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',7,1),(7,'2019-09-04 12:37:56.041366','3','Student1',1,'[{\"added\": {}}]',4,1),(8,'2019-09-04 12:38:02.755049','3','Student1',2,'[]',4,1),(9,'2019-09-04 12:38:27.727676','3','Student1',1,'[{\"added\": {}}]',9,1),(10,'2019-09-04 12:40:48.610490','1','0 signup_quiz',1,'[{\"added\": {}}]',12,1),(11,'2019-09-04 13:17:14.686582','1','I know which are the physical properties of a liquid.<br/><img style = \"width:40%; height:15%;\" src = \"/static/images\\signupq1.jpg\"/><br/>',1,'[{\"added\": {}}]',15,1),(12,'2019-09-04 13:19:28.121007','1','I know which are the physical properties of a liquid.<br/><img style = \"width:40%; height:15%;\" src = \"/static/images/signup\\signupq1.jpg\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(13,'2019-09-04 13:19:55.408946','1','I know which are the physical properties of a liquid.<br/><img style = \"width:40%; height:15%;\" src = \"/static/images/signup\\signupq1.jpg\"/><br/>',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(14,'2019-09-04 15:17:06.497899','1','I know which are the physical properties of a liquid.<br/><img style = \"width:30%; height:10%;\" src = \"/static/images/signupq1.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(15,'2019-09-04 15:26:34.702283','1','True',1,'[{\"added\": {}}]',17,1),(16,'2019-09-04 15:26:43.315713','2','False',1,'[{\"added\": {}}]',17,1),(17,'2019-09-04 16:07:11.645589','2','I can identify the liquid in the images below. <br/><img src = \"/static/images/signupq2.JPG\"/><br/>',1,'[{\"added\": {}}]',15,1),(18,'2019-09-04 16:08:10.323396','2','I can identify the liquid in the images below. <br/><img style = \"width:40%; height:15%;\"src = \"/static/images/signupq2.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\", \"review\"]}}]',15,1),(19,'2019-09-04 16:10:05.959866','1','I know which are the physical properties of a liquid.<br/><img style = \"width:40%; height:15%;\" src = \"/static/images/signupq1.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(20,'2019-09-04 16:15:09.353878','2','I can identify the liquid in the images below. <br/><img style = \"width:40%; height:15%;\"src = \"/static/images/signupq2.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(21,'2019-09-04 16:15:23.778581','2','I can identify the liquid in the images below. <br/><img style = \"width:35%; height:15%;\"src = \"/static/images/signupq2.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(22,'2019-09-04 16:15:42.040846','1','I know which are the physical properties of a liquid.<br/><img style = \"width:35%; height:15%;\" src = \"/static/images/signupq1.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\", \"review\"]}}]',15,1),(23,'2019-09-04 16:22:58.768819','2','I can identify the liquid in the images below. <br/><img style = \"width:55%; height:15%;\"src = \"/static/images/signupq2.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\", \"review\"]}}]',15,1),(24,'2019-09-04 16:24:15.506665','1','I know which are the physical properties of a liquid.<br/><img style = \"width:55%; height:15%;\" src = \"/static/images/signupq1.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\", \"review\"]}}]',15,1),(25,'2019-09-04 16:25:56.354480','3','True',1,'[{\"added\": {}}]',17,1),(26,'2019-09-04 16:26:11.001544','4','False',1,'[{\"added\": {}}]',17,1),(27,'2019-09-04 17:57:41.388753','3','I can chemical the symbol for the element copper and give two uses of copper.',1,'[{\"added\": {}}]',15,1),(28,'2019-09-04 18:00:47.265652','3','I can write the chemical the symbol for copper and give two use of copper.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(29,'2019-09-04 18:05:33.194520','5','True',1,'[{\"added\": {}}]',17,1),(30,'2019-09-04 18:05:46.133321','6','False',1,'[{\"added\": {}}]',17,1),(31,'2019-09-04 18:06:11.729362','3','I can write the chemical the symbol for copper and give two use of copper.<br/>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(32,'2019-09-04 18:11:07.108858','4','I can identify the liquid in the images below. <br/><img style = \"width:55%; height:15%;\"src = \"/static/images/signupq4.JPG\"/><br/>',1,'[{\"added\": {}}]',15,1),(33,'2019-09-04 18:11:22.301596','7','True',1,'[{\"added\": {}}]',17,1),(34,'2019-09-04 18:11:31.577312','8','False',1,'[{\"added\": {}}]',17,1),(35,'2019-09-04 18:12:17.254189','4','I can identify the element in the images below. <br/><img style = \"width:55%; height:15%;\"src = \"/static/images/signupq4.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(36,'2019-09-04 18:19:46.377935','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-    SO4-      Cl-}</script>',1,'[{\"added\": {}}]',15,1),(37,'2019-09-04 18:21:23.619266','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3- }\\ce{NO3- }</script>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(38,'2019-09-04 18:21:51.404323','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3- }&nbsp\\ce{NO3- }</script>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(39,'2019-09-04 18:23:08.514437','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-&nbspNO3-}</script>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(40,'2019-09-04 18:24:08.388859','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-}</script><script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{SO42-}</script>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(41,'2019-09-04 18:25:18.370697','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-}</script><script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{SO4 2-}</script>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(42,'2019-09-04 18:27:33.785875','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-}</script><script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{SO4^2-}</script>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(43,'2019-09-04 18:29:29.428445','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-},\\ce{SO4^2-}</script>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(44,'2019-09-04 18:30:18.564097','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-}, \\ce{SO4^2-},  \\ce{Cl-}, \\ce{NH4+}</script>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(45,'2019-09-04 18:30:48.928209','9','True',1,'[{\"added\": {}}]',17,1),(46,'2019-09-04 18:30:58.320686','10','False',1,'[{\"added\": {}}]',17,1),(47,'2019-09-04 18:33:13.510627','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-}, \\ce{SO4^2-},  \\ce{Cl-}, \\ce{NH4+}</script>',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(48,'2019-09-04 18:33:40.440501','4','I can identify the element in the images below. <br/><img style = \"width:55%; height:15%;\"src = \"/static/images/signupq4.JPG\"/><br/>',2,'[]',15,1),(49,'2019-09-04 18:34:02.030439','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-}, \\ce{SO4^2-},  \\ce{Cl-}, \\ce{NH4+}</script>',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(50,'2019-09-04 18:34:32.660501','5','I can name the following ions:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-}, \\ce{SO4^2-},  \\ce{Cl-}, \\ce{NH4+}</script><br/>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(51,'2019-09-04 18:50:20.446291','6','I can identify the compound in the image below. <br><im',1,'[{\"added\": {}}]',15,1),(52,'2019-09-04 18:52:56.369033','6','I can identify the compound in the image below. <br/><img style = \"width:55%; height:15%;\"src = \"/static/images/signupq6.JPG\"/><br/>',2,'[{\"changed\": {\"fields\": [\"text\", \"review\"]}}]',15,1),(53,'2019-09-04 18:53:35.864552','11','True',1,'[{\"added\": {}}]',17,1),(54,'2019-09-04 18:53:45.207982','12','False',1,'[{\"added\": {}}]',17,1),(55,'2019-09-04 18:56:57.601684','7','I can name the following compounds:  <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{KNO3}, \\ce{MgSO4},  \\ce{LiCl}, \\ce{(NH4)2CO3}</script><br/>',1,'[{\"added\": {}}]',15,1),(56,'2019-09-04 18:58:54.070166','7','I can name the following compounds:  \\ce{KNO3}, \\ce{MgSO4},  \\ce{LiCl}, \\ce{(NH4)2CO3}<br/>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(57,'2019-09-04 19:01:19.926894','7','I can name the following compounds: <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-2\"> \\ce{KNO3}, \\ce{MgSO4},  \\ce{LiCl}, \\ce{(NH4)2CO3}</script><br/>',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(58,'2019-09-04 19:02:02.582850','13','True',1,'[{\"added\": {}}]',17,1),(59,'2019-09-04 19:02:11.371302','14','False',1,'[{\"added\": {}}]',17,1),(60,'2019-09-04 19:29:19.434233','7','I can name the following compounds: <script type=\"math/tex; mode=inline\" id=\"MathJax-Element-2\"> \\ce{KNO3}, \\ce{MgSO4},  \\ce{LiCl}, \\ce{(NH4)2CO3}</script><br/>',2,'[]',15,1),(61,'2019-09-05 07:35:19.282679','7','I can name the following compounds:',2,'[{\"changed\": {\"fields\": [\"text\", \"review\"]}}]',15,1),(62,'2019-09-05 07:36:35.019259','7','I can name the following compounds:',2,'[{\"changed\": {\"fields\": [\"questionimage\", \"review\"]}}]',15,1),(63,'2019-09-05 07:37:02.567090','6','I can identify the compound in the image below.',2,'[{\"changed\": {\"fields\": [\"text\", \"questionimage\"]}}]',15,1),(64,'2019-09-05 07:37:13.733033','5','I can name the following ions:',2,'[{\"changed\": {\"fields\": [\"text\", \"questionimage\"]}}]',15,1),(65,'2019-09-05 07:37:37.835290','4','I can identify the element in the images below.',2,'[{\"changed\": {\"fields\": [\"text\", \"questionimage\"]}}]',15,1),(66,'2019-09-05 07:37:54.186585','3','I can write the chemical the symbol for copper and give two use of copper.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(67,'2019-09-05 07:41:41.986965','3','I can write the chemical the symbol for copper and give two use of copper.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(68,'2019-09-05 07:43:20.502715','7','I can name the following compounds:',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(69,'2019-09-05 07:43:30.642748','6','I can identify the compound in the image below.',2,'[]',15,1),(70,'2019-09-05 07:43:38.076900','5','I can name the following ions:',2,'[]',15,1),(71,'2019-09-05 07:43:44.286816','4','I can identify the element in the images below.',2,'[]',15,1),(72,'2019-09-05 07:44:42.381264','2','I can identify the liquid in the images below.',2,'[{\"changed\": {\"fields\": [\"text\", \"questionimage\"]}}]',15,1),(73,'2019-09-05 07:45:03.186963','1','I know which are the physical properties of a liquid.',2,'[{\"changed\": {\"fields\": [\"text\", \"questionimage\"]}}]',15,1),(74,'2019-09-05 07:57:24.925214','3','I can write the chemical the symbol for copper and give two use of copper.',2,'[]',15,1),(75,'2019-09-05 08:18:49.543551','8','I can draw a diagram to represent any of the first 20 elements in the periodic table.',1,'[{\"added\": {}}]',15,1),(76,'2019-09-05 08:19:11.877080','6','I can identify the compound in the image below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(77,'2019-09-05 08:19:55.756191','6','I can identify the compound in the image below.',2,'[]',15,1),(78,'2019-09-05 08:20:02.238693','6','I can identify the compound in the image below.',2,'[]',15,1),(79,'2019-09-05 08:20:10.236091','7','I can name the following compounds:',2,'[]',15,1),(80,'2019-09-05 08:20:16.150276','5','I can name the following ions:',2,'[]',15,1),(81,'2019-09-05 08:20:28.085684','5','I can name the following ions:',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(82,'2019-09-05 08:20:42.683213','4','I can identify the element in the images below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(83,'2019-09-05 08:21:12.073650','2','I can identify the liquid in the images below.',2,'[{\"changed\": {\"fields\": [\"questionimage\", \"review\"]}}]',15,1),(84,'2019-09-05 08:21:23.338984','2','I can identify the liquid in the images below.',2,'[]',15,1),(85,'2019-09-05 08:21:47.644527','1','I know which are the physical properties of a liquid.',2,'[{\"changed\": {\"fields\": [\"questionimage\", \"review\"]}}]',15,1),(86,'2019-09-05 08:22:19.862949','8','I can draw a diagram to represent any of the first 20 elements in the periodic table.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(87,'2019-09-05 08:28:34.505856','15','True',1,'[{\"added\": {}}]',17,1),(88,'2019-09-05 08:28:44.055377','16','False',1,'[{\"added\": {}}]',17,1),(89,'2019-09-05 08:32:03.891532','9','I can explain how the chemical bonding in NaCl is different to the chemical bonding in H<sub>2</sub>.',1,'[{\"added\": {}}]',15,1),(90,'2019-09-05 08:32:24.355867','9','I can explain how the chemical bonding in NaCl is different to the chemical bonding in H<sub>2</sub>O.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(91,'2019-09-05 08:33:11.278532','8','I can draw a diagram to represent any of the first 20 elements in the periodic table.',2,'[]',15,1),(92,'2019-09-05 08:33:28.819804','9','I can explain how the chemical bonding in NaCl is different to the chemical bonding in H<sub>2</sub>O.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(93,'2019-09-05 08:34:41.730302','9','I can explain how the chemical bonding in NaCl is different to the chemical bonding in H<sub>2</sub>O.',2,'[]',15,1),(94,'2019-09-05 08:37:56.763985','9','I can explain how the chemical bonding in NaCl is different to the chemical bonding in H<sub>2</sub>O.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(95,'2019-09-05 08:44:29.030890','17','True',1,'[{\"added\": {}}]',17,1),(96,'2019-09-05 08:44:37.942772','18','False',1,'[{\"added\": {}}]',17,1),(97,'2019-09-05 08:55:27.731621','10','I can complete the right hand side of this equation.',1,'[{\"added\": {}}]',15,1),(98,'2019-09-05 08:55:52.485901','10','I can complete the right hand side of this equation.',2,'[{\"changed\": {\"fields\": [\"questionimage\", \"review\"]}}]',15,1),(99,'2019-09-05 08:56:22.406303','10','I can complete the right hand side of this equation.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(100,'2019-09-05 08:57:35.090752','19','True',1,'[{\"added\": {}}]',17,1),(101,'2019-09-05 08:57:44.746614','20','False',1,'[{\"added\": {}}]',17,1),(102,'2019-09-05 08:59:16.262906','10','I can predict which atoms will be on the right hand side of this equation and their mass.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(103,'2019-09-05 09:07:29.670405','11','I can complete the word equations below.',1,'[{\"added\": {}}]',15,1),(104,'2019-09-05 09:07:50.710319','11','I can complete the word equations below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(105,'2019-09-05 09:12:59.053422','21','True',1,'[{\"added\": {}}]',17,1),(106,'2019-09-05 09:13:07.838774','22','False',1,'[{\"added\": {}}]',17,1),(107,'2019-09-05 09:15:04.154586','12','I can write the chemical formula compounds like Calcium Chloride, Potassium Nitrate and Aluminium Sulfate',1,'[{\"added\": {}}]',15,1),(108,'2019-09-05 09:15:24.246927','23','True',1,'[{\"added\": {}}]',17,1),(109,'2019-09-05 09:15:35.506644','24','False',1,'[{\"added\": {}}]',17,1),(110,'2019-09-05 10:56:13.597889','13','I can balance the chemical equations below',1,'[{\"added\": {}}]',15,1),(111,'2019-09-05 10:56:53.870019','25','True',1,'[{\"added\": {}}]',17,1),(112,'2019-09-05 10:57:02.511590','26','False',1,'[{\"added\": {}}]',17,1),(113,'2019-09-05 10:57:24.159084','13','I can balance the chemical equations below.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(114,'2019-09-05 10:57:31.851524','12','I can write the chemical formula compounds like Calcium Chloride, Potassium Nitrate and Aluminium Sulfate.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(115,'2019-09-05 10:59:57.359014','13','I can balance the chemical equations below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(116,'2019-09-05 11:02:21.569757','13','I can balance the chemical equations below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(117,'2019-09-05 11:03:52.248620','13','I can balance the chemical equations below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(118,'2019-09-05 11:05:15.517607','14','I can write balanced symbol equations to represent the chemical reactions below.',1,'[{\"added\": {}}]',15,1),(119,'2019-09-05 11:05:29.513659','27','True',1,'[{\"added\": {}}]',17,1),(120,'2019-09-05 11:05:40.073700','28','False',1,'[{\"added\": {}}]',17,1),(121,'2019-09-05 11:12:11.254243','14','I can write balanced symbol equations to represent the chemical reactions below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(122,'2019-09-05 11:14:26.908178','14','I can write balanced symbol equations to represent the chemical reactions below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(123,'2019-09-05 11:17:08.367420','13','I can balance the chemical equations below.',2,'[]',15,1),(124,'2019-09-05 11:19:51.539564','14','I can write balanced symbol equations to represent the chemical reactions below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(125,'2019-09-05 11:20:29.429824','14','I can write balanced symbol equations to represent the chemical reactions below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(126,'2019-09-05 11:22:13.137434','14','I can write balanced symbol equations to represent the chemical reactions below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(127,'2019-09-05 11:22:52.869920','14','I can write balanced symbol equations to represent the chemical reactions below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(128,'2019-09-05 12:17:36.326563','12','I can write the chemical formula for compounds like Calcium Chloride, Potassium Nitrate and Aluminium Sulfate.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(129,'2019-09-05 12:19:58.792844','1','The properties of solids, liquids and gases',1,'[{\"added\": {}}]',11,1),(130,'2019-09-05 12:20:25.396353','3','Student1',2,'[]',9,1),(131,'2019-09-05 12:37:20.807348','2','1 Properties of solids, liquids and gases Test 1',1,'[{\"added\": {}}]',12,1),(132,'2019-09-05 12:43:15.373474','15','Solids have a fixed shape.',1,'[{\"added\": {}}]',15,1),(133,'2019-09-05 12:43:47.413492','29','True',1,'[{\"added\": {}}]',17,1),(134,'2019-09-05 12:43:58.487210','30','False',1,'[{\"added\": {}}]',17,1),(135,'2019-09-05 12:45:16.797235','16','Liquids can be compressed.',1,'[{\"added\": {}}]',15,1),(136,'2019-09-05 12:45:32.018164','31','True',1,'[{\"added\": {}}]',17,1),(137,'2019-09-05 12:45:44.011221','32','False',1,'[{\"added\": {}}]',17,1),(138,'2019-09-05 12:47:48.718707','17','Gases have a fixed volume but do not have a fixed shape.',1,'[{\"added\": {}}]',15,1),(139,'2019-09-05 12:48:04.438708','33','True',1,'[{\"added\": {}}]',17,1),(140,'2019-09-05 12:48:13.669241','34','False',1,'[{\"added\": {}}]',17,1),(141,'2019-09-05 12:50:37.812393','1','The properties of solids, liquids and gases Lesson 1',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(142,'2019-09-05 12:51:15.113365','2','The properties of solids, liquids and gases Lesson 2',1,'[{\"added\": {}}]',11,1),(143,'2019-09-05 12:57:50.766634','3','The properties of solids, liquids and gases. Lesson 3',1,'[{\"added\": {}}]',11,1),(144,'2019-09-05 12:58:31.110562','2','The properties of solids, liquids and gases: Lesson 2',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(145,'2019-09-05 12:58:38.429703','3','The properties of solids, liquids and gases: Lesson 3',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(146,'2019-09-05 12:58:47.003797','1','The properties of solids, liquids and gases: Lesson 1',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(147,'2019-09-05 12:59:32.126754','2','1 Properties of solids, liquids and gases Quiz 1',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',12,1),(148,'2019-09-05 13:19:04.146217','34','False',2,'[{\"changed\": {\"fields\": [\"correct\", \"correct_answer_to_display\"]}}]',17,1),(149,'2019-09-05 13:21:48.793013','29','True',2,'[]',17,1),(150,'2019-09-05 13:44:10.438967','3','student6 Properties of solids, liquids and gases Quiz 1',3,'',19,1),(151,'2019-09-05 13:44:10.452207','2','student6 Properties of solids, liquids and gases Quiz 1',3,'',19,1),(152,'2019-09-05 13:57:48.416475','3','The properties of solids, liquids and gases: Lesson 3',2,'[]',11,1),(153,'2019-09-05 16:28:17.520533','15','True',3,'',18,1),(154,'2019-09-05 16:28:17.538565','14','True',3,'',18,1),(155,'2019-09-05 16:28:17.555573','13','True',3,'',18,1),(156,'2019-09-05 16:28:17.570115','12','True',3,'',18,1),(157,'2019-09-05 16:28:17.593259','11','True',3,'',18,1),(158,'2019-09-05 16:28:17.611523','10','True',3,'',18,1),(159,'2019-09-05 16:28:17.634172','9','True',3,'',18,1),(160,'2019-09-05 16:28:17.651553','8','True',3,'',18,1),(161,'2019-09-05 16:28:17.667477','7','True',3,'',18,1),(162,'2019-09-05 16:35:45.203752','8','student6',2,'[{\"changed\": {\"fields\": [\"needs_help\"]}}]',9,1),(163,'2019-09-05 16:54:24.256715','8','student6',2,'[{\"changed\": {\"fields\": [\"next_lesson_id\"]}}]',9,1),(164,'2019-09-05 17:04:53.552487','10','student6 Properties of solids, liquids and gases Quiz 1',3,'',19,1),(165,'2019-09-05 17:12:18.387878','11','student6 Properties of solids, liquids and gases Quiz 1',3,'',19,1),(166,'2019-09-05 17:16:28.681827','8','student6',2,'[{\"changed\": {\"fields\": [\"level\"]}}]',9,1),(167,'2019-09-05 17:17:17.221795','3','1 Solids, Liquids and',1,'[{\"added\": {}}]',12,1),(168,'2019-09-05 17:17:24.525138','2','1 Properties of solids, liquids and gases Quiz 1',2,'[]',12,1),(169,'2019-09-05 17:17:33.262782','3','1 Properties of solids, liquids and gases Quiz 2',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',12,1),(170,'2019-09-05 17:18:19.077941','18','Liquids have fixed shape.',1,'[{\"added\": {}}]',15,1),(171,'2019-09-05 17:18:37.876283','35','True',1,'[{\"added\": {}}]',17,1),(172,'2019-09-05 17:18:50.091147','36','False',1,'[{\"added\": {}}]',17,1),(173,'2019-09-05 17:23:41.052862','8','student6',2,'[{\"changed\": {\"fields\": [\"level\", \"next_lesson_id\", \"next_exam_id\"]}}]',9,1),(174,'2019-09-05 17:25:07.050004','8','student6',2,'[{\"changed\": {\"fields\": [\"next_exam_id\"]}}]',9,1),(175,'2019-09-05 20:06:02.436123','14','I can write balanced symbol equations to represent the chemical reactions below.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(176,'2019-09-05 20:19:33.890397','14','I can write balanced symbol equations to represent the chemical reactions below.',3,'',15,1),(177,'2019-09-05 20:19:33.928314','13','I can balance the chemical equations below.',3,'',15,1),(178,'2019-09-05 20:19:33.940270','12','I can write the chemical formula for compounds like Calcium Chloride, Potassium Nitrate and Aluminium Sulfate.',3,'',15,1),(179,'2019-09-05 20:19:33.954588','11','I can complete the word equations below.',3,'',15,1),(180,'2019-09-05 20:19:33.963026','10','I can predict which atoms will be on the right hand side of this equation and their mass.',3,'',15,1),(181,'2019-09-05 20:21:51.235266','19','I can name the reactants in this chemical reaction.',1,'[{\"added\": {}}]',15,1),(182,'2019-09-05 20:22:30.147298','37','True',1,'[{\"added\": {}}]',17,1),(183,'2019-09-05 20:22:39.807305','38','False',1,'[{\"added\": {}}]',17,1),(184,'2019-09-05 20:23:54.319115','20','I can predict which atoms will be on the right hand side of this equation and their mass.',1,'[{\"added\": {}}]',15,1),(185,'2019-09-05 20:24:10.063021','39','True',1,'[{\"added\": {}}]',17,1),(186,'2019-09-05 20:24:19.231538','40','False',1,'[{\"added\": {}}]',17,1),(187,'2019-09-05 20:25:07.907023','21','I can complete the word equations below.',1,'[{\"added\": {}}]',15,1),(188,'2019-09-05 20:25:28.167053','41','True',1,'[{\"added\": {}}]',17,1),(189,'2019-09-05 20:25:37.019085','42','False',1,'[{\"added\": {}}]',17,1),(190,'2019-09-05 20:28:46.770892','22','I can work out the chemical formula for the substance below.',1,'[{\"added\": {}}]',15,1),(191,'2019-09-05 20:29:11.952352','43','True',1,'[{\"added\": {}}]',17,1),(192,'2019-09-05 20:29:21.139421','44','False',1,'[{\"added\": {}}]',17,1),(193,'2019-09-05 20:30:23.859343','23','I can write the chemical formula for compounds like Calcium Chloride, Potassium Nitrate and Aluminium Sulfate.',1,'[{\"added\": {}}]',15,1),(194,'2019-09-05 20:30:36.560876','45','True',1,'[{\"added\": {}}]',17,1),(195,'2019-09-05 20:30:45.654246','46','False',1,'[{\"added\": {}}]',17,1),(196,'2019-09-05 20:31:47.297358','24','I can balance the chemical equations below.',1,'[{\"added\": {}}]',15,1),(197,'2019-09-05 20:32:00.189133','47','True',1,'[{\"added\": {}}]',17,1),(198,'2019-09-05 20:32:09.166369','48','False',1,'[{\"added\": {}}]',17,1),(199,'2019-09-05 20:32:49.955231','25','I can write balanced symbol equations to represent the chemical reactions below.',1,'[{\"added\": {}}]',15,1),(200,'2019-09-05 20:35:28.931064','19','I can name the reactants in this chemical reaction.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(201,'2019-09-05 20:39:27.147684','49','True',1,'[{\"added\": {}}]',17,1),(202,'2019-09-05 20:39:39.022906','50','False',1,'[{\"added\": {}}]',17,1),(203,'2019-09-06 06:06:02.155421','1','I know which box below describes the properties of a liquid.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(204,'2019-09-06 06:06:33.137888','6','I can identify the compound in the images below.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(205,'2019-09-06 06:07:35.290490','8','I can draw a diagram to show the atomic structure of an element.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(206,'2019-09-06 06:08:28.505172','9','I can explain how the chemical bonding in Sodium Chloride (NaCl) is different to the chemical bonding in Water (H<sub>2</sub>O).',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(207,'2019-09-06 06:09:05.257770','17','Gases have a fixed volume.',2,'[{\"changed\": {\"fields\": [\"text\", \"review\"]}}]',15,1),(208,'2019-09-06 06:27:47.064025','2','The properties of solids, liquids and gases: Lesson 2',2,'[{\"changed\": {\"fields\": [\"link\"]}}]',11,1),(209,'2019-09-06 06:29:20.965351','4','The Particle Theory: Lesson 1',1,'[{\"added\": {}}]',11,1),(210,'2019-09-06 06:29:40.447962','4','The Particle Theory: Lesson 1',2,'[]',11,1),(211,'2019-09-06 06:32:31.929106','5','The Particle Theory: Lesson 2',1,'[{\"added\": {}}]',11,1),(212,'2019-09-06 06:32:40.877846','5','The Particle Theory: Lesson 2',2,'[]',11,1),(213,'2019-09-06 06:33:37.416991','6','The Particle Theory: Lesson 3',1,'[{\"added\": {}}]',11,1),(214,'2019-09-06 06:35:03.574342','6','The Particle Theory: Lesson 3',2,'[]',11,1),(215,'2019-09-06 06:35:18.848357','7','The Particle Theory: Lesson 4',1,'[{\"added\": {}}]',11,1),(216,'2019-09-06 06:42:13.216444','1','The properties of solids, liquids and gases: Lesson 1',2,'[{\"changed\": {\"fields\": [\"link\"]}}]',11,1),(217,'2019-09-06 06:43:16.288654','3','The properties of solids, liquids and gases: Lesson 3',2,'[]',11,1),(218,'2019-09-06 06:44:44.160423','8','The properties of solids, liquids and gases: Lesson 4',1,'[{\"added\": {}}]',11,1),(219,'2019-09-06 06:46:51.183102','26','What is the physical state of HCl(g)',1,'[{\"added\": {}}]',15,1),(220,'2019-09-06 06:47:08.324447','51','Solid',1,'[{\"added\": {}}]',17,1),(221,'2019-09-06 06:47:19.372269','52','Liquid',1,'[{\"added\": {}}]',17,1),(222,'2019-09-06 06:47:32.612530','53','Gas',1,'[{\"added\": {}}]',17,1),(223,'2019-09-06 06:52:23.568502','18','Liquids have fixed shape.',2,'[]',15,1),(224,'2019-09-06 06:53:09.147284','27','Solids have a fixed volume.',1,'[{\"added\": {}}]',15,1),(225,'2019-09-06 06:53:27.369324','54','True',1,'[{\"added\": {}}]',17,1),(226,'2019-09-06 06:53:39.646370','55','False',1,'[{\"added\": {}}]',17,1),(227,'2019-09-06 06:55:23.915758','28','Gases take the shape of the bottom of their container.',1,'[{\"added\": {}}]',15,1),(228,'2019-09-06 06:56:18.635699','29','What physical state is C(s) in?',1,'[{\"added\": {}}]',15,1),(229,'2019-09-06 06:56:37.921832','56','Solid',1,'[{\"added\": {}}]',17,1),(230,'2019-09-06 06:56:52.588374','57','Liquid',1,'[{\"added\": {}}]',17,1),(231,'2019-09-06 06:57:03.643586','58','Gas',1,'[{\"added\": {}}]',17,1),(232,'2019-09-06 06:57:22.512498','3','1 Properties of solids, liquids and gases Quiz 2',2,'[]',12,1),(233,'2019-09-06 06:57:30.804244','4','1 Properties of solids, liquids and gases Quiz 3',1,'[{\"added\": {}}]',12,1),(234,'2019-09-06 06:59:58.754917','30','Solids can be compressed.',1,'[{\"added\": {}}]',15,1),(235,'2019-09-06 07:00:36.851326','31','Liquids have a fixed volume.',1,'[{\"added\": {}}]',15,1),(236,'2019-09-06 07:01:12.351105','32','Gases have fixed shape.',1,'[{\"added\": {}}]',15,1),(237,'2019-09-06 07:01:43.435660','33','What state is Br(l) in?',1,'[{\"added\": {}}]',15,1),(238,'2019-09-06 07:02:04.331456','59','True',1,'[{\"added\": {}}]',17,1),(239,'2019-09-06 07:02:17.249691','60','False',1,'[{\"added\": {}}]',17,1),(240,'2019-09-06 07:02:29.341329','61','True',1,'[{\"added\": {}}]',17,1),(241,'2019-09-06 07:02:39.688629','62','False',1,'[{\"added\": {}}]',17,1),(242,'2019-09-06 07:02:51.959317','63','True',1,'[{\"added\": {}}]',17,1),(243,'2019-09-06 07:03:05.683755','64','False',1,'[{\"added\": {}}]',17,1),(244,'2019-09-06 07:03:15.816510','65','Solid',1,'[{\"added\": {}}]',17,1),(245,'2019-09-06 07:03:27.054935','66','Liquid',1,'[{\"added\": {}}]',17,1),(246,'2019-09-06 07:03:37.639568','67','Gas',1,'[{\"added\": {}}]',17,1),(247,'2019-09-06 07:06:17.084888','68','True',1,'[{\"added\": {}}]',17,1),(248,'2019-09-06 07:06:31.760596','69','False',1,'[{\"added\": {}}]',17,1),(249,'2019-09-06 07:17:18.693824','5','2 The Particle Theory: Quiz 1',1,'[{\"added\": {}}]',12,1),(250,'2019-09-06 07:22:09.289882','34','The particles in a liquid vibrate about fixed positions.',1,'[{\"added\": {}}]',15,1),(251,'2019-09-06 07:22:24.005202','70','True',1,'[{\"added\": {}}]',17,1),(252,'2019-09-06 07:22:36.995199','71','False',1,'[{\"added\": {}}]',17,1),(253,'2019-09-06 07:33:51.676455','35','The diagram below shows the arrangement of particles in a solid.',1,'[{\"added\": {}}]',15,1),(254,'2019-09-06 07:34:10.299129','72','True',1,'[{\"added\": {}}]',17,1),(255,'2019-09-06 07:34:23.676481','73','False',1,'[{\"added\": {}}]',17,1),(256,'2019-09-06 07:35:48.470907','36','The particles in a liquid are not touching.',1,'[{\"added\": {}}]',15,1),(257,'2019-09-06 07:36:06.077392','74','True',1,'[{\"added\": {}}]',17,1),(258,'2019-09-06 07:36:21.735186','75','False',1,'[{\"added\": {}}]',17,1),(259,'2019-09-06 07:39:18.370666','37','The particles in a gas move rapidly and randomly in all directions.',1,'[{\"added\": {}}]',15,1),(260,'2019-09-06 07:42:11.654739','76','True',1,'[{\"added\": {}}]',17,1),(261,'2019-09-06 07:42:21.925572','77','False',1,'[{\"added\": {}}]',17,1),(262,'2019-09-06 07:57:56.372839','5','2 The Particle Theory: Quiz 1',2,'[]',12,1),(263,'2019-09-06 07:58:05.623172','6','2 The Particle Theory: Quiz 2',1,'[{\"added\": {}}]',12,1),(264,'2019-09-06 08:03:57.516555','38','The diagram below shows how the particles are arranged in a solid.',1,'[{\"added\": {}}]',15,1),(265,'2019-09-06 08:04:29.764755','38','The diagram below shows how the particles are arranged in a solid.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(266,'2019-09-06 08:04:45.702261','78','True',1,'[{\"added\": {}}]',17,1),(267,'2019-09-06 08:04:57.370709','79','False',1,'[{\"added\": {}}]',17,1),(268,'2019-09-06 08:21:09.668552','39','Which diagram below shows Helium gas  He(g)',1,'[{\"added\": {}}]',15,1),(269,'2019-09-06 08:21:17.616121','38','The diagram below shows how the particles are arranged in a solid.',2,'[]',15,1),(270,'2019-09-06 08:21:27.244291','39','Which diagram below shows Helium gas  He(g)',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(271,'2019-09-06 08:21:49.502264','39','Which diagram below shows Helium gas  He(g)',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(272,'2019-09-06 08:22:07.899011','80','A',1,'[{\"added\": {}}]',17,1),(273,'2019-09-06 08:22:23.464267','81','B',1,'[{\"added\": {}}]',17,1),(274,'2019-09-06 08:22:33.876292','82','C',1,'[{\"added\": {}}]',17,1),(275,'2019-09-06 08:22:42.988239','83','D',1,'[{\"added\": {}}]',17,1),(276,'2019-09-06 08:23:33.770388','39','Which diagram below shows helium gas  He(g)',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(277,'2019-09-06 08:26:01.347365','40','The particles in a solid vibrate around fixed positions.',1,'[{\"added\": {}}]',15,1),(278,'2019-09-06 08:26:18.637083','84','True',1,'[{\"added\": {}}]',17,1),(279,'2019-09-06 08:26:29.167321','85','False',1,'[{\"added\": {}}]',17,1),(280,'2019-09-06 08:26:42.738333','40','The particles in a solid vibrate about fixed positions.',2,'[{\"changed\": {\"fields\": [\"text\"]}}]',15,1),(281,'2019-09-06 08:27:41.128487','41','The particles in a liquid can slip and slide over each other.',1,'[{\"added\": {}}]',15,1),(282,'2019-09-06 08:27:58.073833','86','True',1,'[{\"added\": {}}]',17,1),(283,'2019-09-06 08:28:08.022247','87','False',1,'[{\"added\": {}}]',17,1),(284,'2019-09-06 10:54:10.913143','39','Which diagram below shows helium gas  He(g)',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(285,'2019-09-06 10:54:20.724311','38','The diagram below shows how the particles are arranged in a solid.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(286,'2019-09-06 10:54:27.618892','37','The particles in a gas move rapidly and randomly in all directions.',2,'[]',15,1),(287,'2019-09-06 10:54:38.296504','35','The diagram below shows the arrangement of particles in a solid.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(288,'2019-09-06 11:55:26.696868','6','2 The Particle Theory: Quiz 2',2,'[]',12,1),(289,'2019-09-06 11:55:39.309221','7','2 The Particle Theory: Quiz 3',1,'[{\"added\": {}}]',12,1),(290,'2019-09-06 11:56:53.023936','42','What type of bonding is between the atoms in methane. CH<sub>4</sub>',1,'[{\"added\": {}}]',14,1),(291,'2019-09-06 11:57:16.671314','88','Covalent',1,'[{\"added\": {}}]',17,1),(292,'2019-09-06 11:57:39.939934','89','covelent',1,'[{\"added\": {}}]',17,1),(293,'2019-09-06 11:59:37.383615','92','covelent',3,'',18,1),(294,'2019-09-06 12:00:01.585670','10','student12',2,'[{\"changed\": {\"fields\": [\"level\"]}}]',9,1),(295,'2019-09-06 12:01:09.536286','43','What is the chemical formula for water',1,'[{\"added\": {}}]',16,1),(296,'2019-09-06 12:01:45.588860','90','H2O',1,'[{\"added\": {}}]',17,1),(297,'2019-09-06 12:14:03.843667','94','CH4',3,'',18,1),(298,'2019-09-06 12:14:03.864857','93','covelent',3,'',18,1),(299,'2019-09-06 12:14:17.352092','49','student12 The Particle Theory: Quiz 3',3,'',19,1),(300,'2019-09-06 12:14:57.538868','10','student12',2,'[{\"changed\": {\"fields\": [\"next_exam_id\"]}}]',9,1),(301,'2019-09-06 13:13:32.412448','43','What is the chemical formula for water',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',16,1),(302,'2019-09-06 13:15:16.649818','42','What type of bonding is between the atoms in methane. CH<sub>4</sub>',3,'',14,1),(303,'2019-09-06 13:15:54.848966','43','What is the chemical formula for water',3,'',16,1),(304,'2019-09-06 13:20:59.440327','44','Which box below shows a substance in the liquid state.',1,'[{\"added\": {}}]',15,1),(305,'2019-09-06 13:21:38.890289','44','Which box below shows a substance in the liquid state.',2,'[{\"changed\": {\"fields\": [\"questionimage\"]}}]',15,1),(306,'2019-09-06 13:21:59.250338','38','The diagram below shows how the particles are arranged in a solid.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(307,'2019-09-06 13:22:15.978656','41','The particles in a liquid can slip and slide over each other.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(308,'2019-09-06 13:22:24.867022','40','The particles in a solid vibrate about fixed positions.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(309,'2019-09-06 13:22:43.114459','44','Which box below shows a substance in the liquid state.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(310,'2019-09-06 13:22:51.316875','41','The particles in a liquid can slip and slide over each other.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(311,'2019-09-06 13:23:15.035569','40','The particles in a solid vibrate about fixed positions.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(312,'2019-09-06 13:23:23.091003','38','The diagram below shows how the particles are arranged in a solid.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(313,'2019-09-06 13:23:28.938393','37','The particles in a gas move rapidly and randomly in all directions.',2,'[]',15,1),(314,'2019-09-06 13:23:38.034930','37','The particles in a gas move rapidly and randomly in all directions.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(315,'2019-09-06 13:23:44.359321','37','The particles in a gas move rapidly and randomly in all directions.',2,'[]',15,1),(316,'2019-09-06 13:23:55.859971','36','The particles in a liquid are not touching.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(317,'2019-09-06 13:24:05.554013','35','The diagram below shows the arrangement of particles in a solid.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(318,'2019-09-06 13:24:17.514886','34','The particles in a liquid vibrate about fixed positions.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(319,'2019-09-06 13:24:34.961703','33','What state is Br(l) in?',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(320,'2019-09-06 13:24:47.310762','31','Liquids have a fixed volume.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(321,'2019-09-06 13:25:35.684306','30','Solids can be compressed.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(322,'2019-09-06 13:25:47.778431','29','What physical state is C(s) in?',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(323,'2019-09-06 13:26:09.626573','18','Liquids have fixed shape.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(324,'2019-09-06 13:27:02.310630','17','Gases have a fixed volume.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(325,'2019-09-06 13:27:45.307672','16','Liquids can be compressed.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(326,'2019-09-06 13:28:45.328253','15','Solids have a fixed shape.',2,'[{\"changed\": {\"fields\": [\"review\"]}}]',15,1),(327,'2019-09-06 13:28:55.350164','44','Which box below shows a substance in the liquid state.',2,'[]',15,1),(328,'2019-09-06 13:29:50.976759','45','Liquids have a fixed shape.',1,'[{\"added\": {}}]',15,1),(329,'2019-09-06 13:30:20.402835','91','A',1,'[{\"added\": {}}]',17,1),(330,'2019-09-06 13:30:31.922333','92','B',1,'[{\"added\": {}}]',17,1),(331,'2019-09-06 13:30:42.299396','93','C',1,'[{\"added\": {}}]',17,1),(332,'2019-09-06 13:30:52.858154','94','D',1,'[{\"added\": {}}]',17,1),(333,'2019-09-06 13:31:05.016842','95','True',1,'[{\"added\": {}}]',17,1),(334,'2019-09-06 13:31:18.601633','96','False',1,'[{\"added\": {}}]',17,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'custom_users','class_id'),(8,'custom_users','school'),(9,'custom_users','studentprofile'),(10,'custom_users','teacherprofile'),(17,'exams','answer'),(19,'exams','completedexam'),(12,'exams','exam'),(16,'exams','formula_question'),(20,'exams','incorrectanswer'),(15,'exams','mcq_question'),(13,'exams','question'),(18,'exams','useranswer'),(14,'exams','written_question'),(11,'lessons','lesson'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-08-23 07:27:07.447885'),(2,'auth','0001_initial','2019-08-23 07:35:50.080345'),(3,'admin','0001_initial','2019-08-23 07:38:05.386709'),(4,'admin','0002_logentry_remove_auto_add','2019-08-23 07:38:05.436051'),(5,'contenttypes','0002_remove_content_type_name','2019-08-23 07:38:05.721757'),(6,'auth','0002_alter_permission_name_max_length','2019-08-23 07:38:05.901517'),(7,'auth','0003_alter_user_email_max_length','2019-08-23 07:38:06.598622'),(8,'auth','0004_alter_user_username_opts','2019-08-23 07:38:06.634666'),(9,'auth','0005_alter_user_last_login_null','2019-08-23 07:38:06.785514'),(10,'auth','0006_require_contenttypes_0002','2019-08-23 07:38:06.838969'),(11,'auth','0007_alter_validators_add_error_messages','2019-08-23 07:38:06.894633'),(12,'auth','0008_alter_user_username_max_length','2019-08-23 07:38:07.226787'),(13,'auth','0009_alter_user_last_name_max_length','2019-08-23 07:38:07.494683'),(14,'lessons','0001_initial','2019-08-23 07:39:34.991166'),(15,'custom_users','0001_initial','2019-08-23 07:47:25.565506'),(16,'sessions','0001_initial','2019-08-23 07:48:05.323516'),(17,'exams','0001_initial','2019-08-23 07:59:32.760352'),(18,'lessons','0002_remove_lesson_image_link','2019-08-30 15:49:12.701845'),(19,'exams','0002_question_questionimage','2019-09-05 07:33:12.810809'),(20,'exams','0003_auto_20190905_0840','2019-09-05 07:40:51.523957');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('56ws1io6hit25vqs2nlk8zvn8gjwzdmp','NzNlNmU1ODhmMmQ5MTMxMDkwMDE2MTNmZDgxZWUwOGQ1ZjAyYmYyODp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNGE5OWI3NGMzMTdhYTE0N2I1ZmE1Njg3ODBmMGY1YjUzN2EzNjZkIn0=','2019-09-19 11:00:14.827270'),('k57y790ojeu7mk4szrurlpxumeihplxq','YmVhOGFlNDk1ODRhMzY4MTBiMzM4MzZhNzA0NzE1YmNlYmViMjIzNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYWM4NzEwZTM3MzM3YjhlZjQ5ZWRkOTdmMTM3ZjYyYTgxZWIyNzg0In0=','2019-09-20 12:49:04.741227'),('kazaltgpun71h3ihym6es26j8dr3s31c','YjlhNDA0ZDhhMmY0YzUyYzdmYjdiNWQ2MmNjYTBjZmEzNDg1YmQ1NDp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODhmMjU0MTg3OWYyZjkyNzc4NWIyMjlmODQ2ZTMxNDMzYzQ3MjUxOCJ9','2019-09-20 12:02:20.492483'),('o9nfo0bol0pa5a2u3yfcsif5dz6zvnh2','NzNlNmU1ODhmMmQ5MTMxMDkwMDE2MTNmZDgxZWUwOGQ1ZjAyYmYyODp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNGE5OWI3NGMzMTdhYTE0N2I1ZmE1Njg3ODBmMGY1YjUzN2EzNjZkIn0=','2019-09-18 17:36:50.957525');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams_answer`
--

DROP TABLE IF EXISTS `exams_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exams_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(1000) NOT NULL,
  `correct` tinyint(1) NOT NULL,
  `correct_spelling` tinyint(1) NOT NULL,
  `correct_answer_to_display` tinyint(1) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exams_answer_question_id_7327e287_fk_exams_question_id` (`question_id`),
  CONSTRAINT `exams_answer_question_id_7327e287_fk_exams_question_id` FOREIGN KEY (`question_id`) REFERENCES `exams_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams_answer`
--

LOCK TABLES `exams_answer` WRITE;
/*!40000 ALTER TABLE `exams_answer` DISABLE KEYS */;
INSERT INTO `exams_answer` VALUES (1,'True',0,1,0,1),(2,'False',0,1,0,1),(3,'True',0,1,0,2),(4,'False',0,1,0,2),(5,'True',0,1,0,3),(6,'False',0,1,0,3),(7,'True',0,1,0,4),(8,'False',0,1,0,4),(9,'True',0,1,0,5),(10,'False',0,1,0,5),(11,'True',0,1,0,6),(12,'False',0,1,0,6),(13,'True',0,1,0,7),(14,'False',0,1,0,7),(15,'True',0,1,0,8),(16,'False',0,1,0,8),(17,'True',0,1,0,9),(18,'False',0,1,0,9),(29,'True',1,1,1,15),(30,'False',0,1,0,15),(31,'True',0,1,0,16),(32,'False',1,1,1,16),(33,'True',0,1,0,17),(34,'False',1,1,1,17),(35,'True',0,1,0,18),(36,'False',1,1,1,18),(37,'True',0,1,0,19),(38,'False',0,1,0,19),(39,'True',0,1,0,20),(40,'False',0,1,0,20),(41,'True',0,1,0,21),(42,'False',0,1,0,21),(43,'True',0,1,0,22),(44,'False',0,1,0,22),(45,'True',0,1,0,23),(46,'False',0,1,0,23),(47,'True',0,1,0,24),(48,'False',0,1,0,24),(49,'True',0,1,0,25),(50,'False',0,1,0,25),(51,'Solid',0,1,0,26),(52,'Liquid',0,1,0,26),(53,'Gas',1,1,1,26),(54,'True',1,1,1,27),(55,'False',0,1,0,27),(56,'Solid',1,1,1,29),(57,'Liquid',0,1,0,29),(58,'Gas',0,1,0,29),(59,'True',0,1,0,30),(60,'False',1,1,1,30),(61,'True',1,1,1,31),(62,'False',0,1,0,31),(63,'True',0,1,0,32),(64,'False',1,1,1,32),(65,'Solid',0,1,0,33),(66,'Liquid',1,1,1,33),(67,'Gas',0,1,0,33),(68,'True',0,1,0,28),(69,'False',1,1,1,28),(70,'True',0,1,0,34),(71,'False',1,1,1,34),(72,'True',1,1,1,35),(73,'False',0,1,0,35),(74,'True',0,1,0,36),(75,'False',1,1,1,36),(76,'True',1,1,1,37),(77,'False',0,1,0,37),(78,'True',0,1,0,38),(79,'False',1,1,1,38),(80,'A',0,1,0,39),(81,'B',1,1,1,39),(82,'C',0,1,0,39),(83,'D',0,1,0,39),(84,'True',1,1,1,40),(85,'False',0,1,0,40),(86,'True',1,1,1,41),(87,'False',0,1,0,41),(91,'A',1,1,1,44),(92,'B',0,1,0,44),(93,'C',0,1,0,44),(94,'D',0,1,0,44),(95,'True',0,1,0,45),(96,'False',1,1,1,45);
/*!40000 ALTER TABLE `exams_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams_completedexam`
--

DROP TABLE IF EXISTS `exams_completedexam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exams_completedexam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` int(11) NOT NULL,
  `percentage` int(11) NOT NULL,
  `attempt` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exams_completedexam_exam_id_ef4c9f40_fk_exams_exam_id` (`exam_id`),
  KEY `exams_completedexam_user_id_bcacebf8_fk_custom_us` (`user_id`),
  CONSTRAINT `exams_completedexam_exam_id_ef4c9f40_fk_exams_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `exams_exam` (`id`),
  CONSTRAINT `exams_completedexam_user_id_bcacebf8_fk_custom_us` FOREIGN KEY (`user_id`) REFERENCES `custom_users_studentprofile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams_completedexam`
--

LOCK TABLES `exams_completedexam` WRITE;
/*!40000 ALTER TABLE `exams_completedexam` DISABLE KEYS */;
INSERT INTO `exams_completedexam` VALUES (16,1,0,1,2,8),(17,1,0,1,3,8),(21,1,67,1,2,9),(39,1,0,1,4,10),(40,1,0,1,3,10),(41,2,0,1,6,10),(43,1,100,1,2,10),(54,2,0,1,7,10);
/*!40000 ALTER TABLE `exams_completedexam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams_exam`
--

DROP TABLE IF EXISTS `exams_exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exams_exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `level` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams_exam`
--

LOCK TABLES `exams_exam` WRITE;
/*!40000 ALTER TABLE `exams_exam` DISABLE KEYS */;
INSERT INTO `exams_exam` VALUES (1,'signup_quiz',0),(2,'Properties of solids, liquids and gases Quiz 1',1),(3,'Properties of solids, liquids and gases Quiz 2',1),(4,'Properties of solids, liquids and gases Quiz 3',1),(5,'The Particle Theory: Quiz 1',2),(6,'The Particle Theory: Quiz 2',2),(7,'The Particle Theory: Quiz 3',2);
/*!40000 ALTER TABLE `exams_exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams_formula_question`
--

DROP TABLE IF EXISTS `exams_formula_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exams_formula_question` (
  `question_ptr_id` int(11) NOT NULL,
  `is_formula` tinyint(1) NOT NULL,
  PRIMARY KEY (`question_ptr_id`),
  CONSTRAINT `exams_formula_questi_question_ptr_id_6f3ed44c_fk_exams_que` FOREIGN KEY (`question_ptr_id`) REFERENCES `exams_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams_formula_question`
--

LOCK TABLES `exams_formula_question` WRITE;
/*!40000 ALTER TABLE `exams_formula_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `exams_formula_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams_incorrectanswer`
--

DROP TABLE IF EXISTS `exams_incorrectanswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exams_incorrectanswer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exams_incorrectanswer_question_id_4ef9b80f_fk_exams_question_id` (`question_id`),
  KEY `exams_incorrectanswe_user_id_2845d647_fk_custom_us` (`user_id`),
  CONSTRAINT `exams_incorrectanswe_user_id_2845d647_fk_custom_us` FOREIGN KEY (`user_id`) REFERENCES `custom_users_studentprofile` (`user_id`),
  CONSTRAINT `exams_incorrectanswer_question_id_4ef9b80f_fk_exams_question_id` FOREIGN KEY (`question_id`) REFERENCES `exams_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams_incorrectanswer`
--

LOCK TABLES `exams_incorrectanswer` WRITE;
/*!40000 ALTER TABLE `exams_incorrectanswer` DISABLE KEYS */;
INSERT INTO `exams_incorrectanswer` VALUES (1,16,8),(2,15,8),(3,17,8),(4,18,8),(5,17,9),(6,15,10),(7,16,10),(8,18,10),(9,27,10),(10,28,10),(11,29,10),(12,30,10),(13,31,10),(14,32,10),(15,33,10),(16,17,10),(17,26,10),(18,34,10),(19,35,10),(20,37,10),(21,36,10),(22,38,10),(23,39,10),(24,40,10),(25,41,10);
/*!40000 ALTER TABLE `exams_incorrectanswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams_mcq_question`
--

DROP TABLE IF EXISTS `exams_mcq_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exams_mcq_question` (
  `question_ptr_id` int(11) NOT NULL,
  `is_MCQ` tinyint(1) NOT NULL,
  PRIMARY KEY (`question_ptr_id`),
  CONSTRAINT `exams_mcq_question_question_ptr_id_cb42e7dd_fk_exams_question_id` FOREIGN KEY (`question_ptr_id`) REFERENCES `exams_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams_mcq_question`
--

LOCK TABLES `exams_mcq_question` WRITE;
/*!40000 ALTER TABLE `exams_mcq_question` DISABLE KEYS */;
INSERT INTO `exams_mcq_question` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(15,1),(16,1),(17,1),(18,1),(19,1),(20,1),(21,1),(22,1),(23,1),(24,1),(25,1),(26,1),(27,1),(28,1),(29,1),(30,1),(31,1),(32,1),(33,1),(34,1),(35,1),(36,1),(37,1),(38,1),(39,1),(40,1),(41,1),(44,1),(45,1);
/*!40000 ALTER TABLE `exams_mcq_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams_question`
--

DROP TABLE IF EXISTS `exams_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exams_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(250) NOT NULL,
  `review` varchar(1000) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `questionimage` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `text` (`text`),
  KEY `exams_question_exam_id_85081c44_fk_exams_exam_id` (`exam_id`),
  CONSTRAINT `exams_question_exam_id_85081c44_fk_exams_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `exams_exam` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams_question`
--

LOCK TABLES `exams_question` WRITE;
/*!40000 ALTER TABLE `exams_question` DISABLE KEYS */;
INSERT INTO `exams_question` VALUES (1,'I know which box below describes the properties of a liquid.','<img style = \"width:55%; height:15%;\" src = \"/static/images/signup/reviewq1.jpg\"/>',1,'<img style = \"width:55%; height:15%;\" src = \"/static/images/signup/signupq1.JPG\"/>'),(2,'I can identify the liquid in the images below.','<br/><img style = \"width:55%; height:15%;\"src = \"/static/images/signup/review2.JPG\"/><br/>',1,'<img style = \"width:55%; height:15%;\"src = \"/static/images/signup/signupq2.JPG\"/>'),(3,'I can write the chemical the symbol for copper and give two use of copper.','The chemical symbol is Cu. It is used for electrical wiring because it is a good conductor of electricity and water pipes because it is very unreactive.',1,NULL),(4,'I can identify the element in the images below.','B is the element because all the atoms are the same.',1,'<img style = \"width:55%; height:15%;\"src = \"/static/images/signup/signupq4.JPG\"/>'),(5,'I can name the following ions:','<br/><img style = \"width:55%; height:15%;\"src = \"/static/images/signup/review5.JPG\"/><br/>',1,'<script type=\"math/tex; mode=inline\" id=\"MathJax-Element-1\">\\ce{NO3-}, \\ce{SO4^2-},  \\ce{Cl-}, \\ce{NH4+}</script><br/>'),(6,'I can identify the compound in the images below.','A is the compound it\'s made up of two different elements chemically bonded together.',1,'<img style = \"width:55%; height:15%;\"src = \"/static/images/signup/signupq6.JPG\"/>'),(7,'I can name the following compounds:','review',1,'<script type=\"math/tex; mode=inline\" id=\"MathJax-Element-2\"> \\ce{KNO3}, \\ce{MgSO4},  \\ce{LiCl}, \\ce{(NH4)2CO3}</script><br/>'),(8,'I can draw a diagram to show the atomic structure of an element.','<img style = \"width:55%; height:15%;\" src = \"/static/images/signup/reviewq6.jpg\"/>',1,NULL),(9,'I can explain how the chemical bonding in Sodium Chloride (NaCl) is different to the chemical bonding in Water (H<sub>2</sub>O).','sss',1,'<img style = \"width:55%; height:15%;\" src = \"/static/images/signup/signupq9.JPG\"/>'),(15,'Solids have a fixed shape.','True - solids have a fixed shape and cannot flow.',2,NULL),(16,'Liquids can be compressed.','False - the particles are already touching. Liquids can not be compressed.',2,NULL),(17,'Gases have a fixed volume.','False - There is space between the particles. Gases can be compressed into a smaller volume.',2,NULL),(18,'Liquids have fixed shape.','False - liquids take the shape of the bottom of their container.',3,NULL),(19,'I can name the reactants in this chemical reaction.','The reactants are on the left hand side of the arrow. The products are on the right hand side.',1,'<script type=\"math/tex; mode=inline\" id=\"MathJax-Element-3\">\\ce{Sodium Hydroxide + Hydrochloric Acid -> Sodium Chloride + Water}</script>'),(20,'I can predict which atoms will be on the right hand side of this equation and their mass.','<img style = \"width:55%; height:15%;\" src = \"/static/images/signup/review11.JPG\"/>',1,'<img style = \"width:55%; height:15%;\" src = \"/static/images/signup/signup11.JPG\"/>'),(21,'I can complete the word equations below.','Review',1,'<img style = \"width:55%; height:15%;\" src = \"/static/images/signup/signupq12.JPG\"/>'),(22,'I can work out the chemical formula for the substance below.','Review',1,'<script type=\"math/tex; mode=inline\" id=\"MathJax-Element-4\">\\ce{Hydrochloric Acid}, \\ce{Sulfuric Acid}, \\ce{ Calcium Hydroxide }</script>'),(23,'I can write the chemical formula for compounds like Calcium Chloride, Potassium Nitrate and Aluminium Sulfate.','Review',1,NULL),(24,'I can balance the chemical equations below.','Review',1,'<script type=\"math/tex; mode=inline\" id=\"MathJax-Element-5\">\\ce{__HCl + CaCO3 -> CaCl2 + CO2 + H2O}</script><br/><script type=\"math/tex; mode=inline\" id=\"MathJax-Element-6\">\\ce{HNO3 + Al2O3 -> Al(NO3)3 + H2O}</script>'),(25,'I can write balanced symbol equations to represent the chemical reactions below.','Review',1,'<img style = \"width:55%; height:15%;\" src = \"static/images/signup/signupq12.JPG\"/>'),(26,'What is the physical state of HCl(g)','(g) indicates this substance is in the gas phase.',2,NULL),(27,'Solids have a fixed volume.','True, solids can not be compressed they have a fixed volume.',3,NULL),(28,'Gases take the shape of the bottom of their container.','False, gases take the shape of their whole container. They spread out to fill all the available space.',3,NULL),(29,'What physical state is C(s) in?','Solid - (s) indicates that carbon is in the solid state.',3,NULL),(30,'Solids can be compressed.','False - solids have a fixed volume. The particles are touching, they can not be compressed.',4,NULL),(31,'Liquids have a fixed volume.','True - liquids can not be compressed. They have a fixed volume.',4,NULL),(32,'Gases have fixed shape.','False, gases take the shape of their container.',4,NULL),(33,'What state is Br(l) in?','Liquid - (l) indicates the liquid state.',4,NULL),(34,'The particles in a liquid vibrate about fixed positions.','False - the particles in a solid vibrate about fixed positions.',5,NULL),(35,'The diagram below shows the arrangement of particles in a solid.','True - the particles in a solid are in a regular arrangement.',5,'<img style = \"width:55%; height:15%;\" src = \"/static/images/level2quiz1/q2.JPG\"/>'),(36,'The particles in a liquid are not touching.','False - the particles in a liquid are touching. This is why liquids can not be compressed.',5,NULL),(37,'The particles in a gas move rapidly and randomly in all directions.','True - the particles in a gas are weakly attracted to each other so move rapidly and randomly in all directions.',5,NULL),(38,'The diagram below shows how the particles are arranged in a solid.','False - the particles in a liquid can slip and slide over each other.',6,'<img style = \"width:55%; height:15%;\" src = \"/static/images/level2quiz2/q1.JPG\"/>'),(39,'Which diagram below shows helium gas  He(g)','B - shows atoms of Helium. D shows a mixture of substances. It is not pure helium.',6,'<img style = \"width:55%; height:15%;\" src = \"/static/images/level2quiz2/q2.JPG\"/>'),(40,'The particles in a solid vibrate about fixed positions.','True - the particles in a solid are not free to move around but they do vibrate.',6,NULL),(41,'The particles in a liquid can slip and slide over each other.','True - the particles in a liquid can slide over each other. This is why liquids flow.',6,NULL),(44,'Which box below shows a substance in the liquid state.','A - in a liquid the particles are touching but free to slip and slide over each other.',7,'<img style = \"width:55%; height:15%;\" src = \"/static/images/level2quiz2/q2.JPG\"/>'),(45,'Liquids have a fixed shape.','False - Liquids take the shape of the bottom of their container and they can flow.',7,NULL);
/*!40000 ALTER TABLE `exams_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams_useranswer`
--

DROP TABLE IF EXISTS `exams_useranswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exams_useranswer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_answer` varchar(1000) NOT NULL,
  `question_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exams_useranswer_question_id_2942c9ad_fk_exams_question_id` (`question_id`),
  KEY `exams_useranswer_user_id_e0508323_fk_custom_us` (`user_id`),
  CONSTRAINT `exams_useranswer_question_id_2942c9ad_fk_exams_question_id` FOREIGN KEY (`question_id`) REFERENCES `exams_question` (`id`),
  CONSTRAINT `exams_useranswer_user_id_e0508323_fk_custom_us` FOREIGN KEY (`user_id`) REFERENCES `custom_users_studentprofile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams_useranswer`
--

LOCK TABLES `exams_useranswer` WRITE;
/*!40000 ALTER TABLE `exams_useranswer` DISABLE KEYS */;
INSERT INTO `exams_useranswer` VALUES (25,'False',15,8),(26,'True',16,8),(27,'True',17,8),(28,'True',18,8),(29,'True',15,9),(30,'False',16,9),(31,'True',17,9),(36,'True',18,10),(37,'False',27,10),(38,'True',28,10),(39,'Gas',29,10),(40,'True',30,10),(41,'False',31,10),(42,'True',32,10),(43,'Solid',33,10),(72,'True',38,10),(73,'A',39,10),(74,'False',40,10),(75,'False',41,10),(80,'True',15,10),(81,'False',16,10),(82,'False',17,10),(83,'Gas',26,10);
/*!40000 ALTER TABLE `exams_useranswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exams_written_question`
--

DROP TABLE IF EXISTS `exams_written_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exams_written_question` (
  `question_ptr_id` int(11) NOT NULL,
  `is_written` tinyint(1) NOT NULL,
  PRIMARY KEY (`question_ptr_id`),
  CONSTRAINT `exams_written_questi_question_ptr_id_8127bc00_fk_exams_que` FOREIGN KEY (`question_ptr_id`) REFERENCES `exams_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exams_written_question`
--

LOCK TABLES `exams_written_question` WRITE;
/*!40000 ALTER TABLE `exams_written_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `exams_written_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lessons_lesson`
--

DROP TABLE IF EXISTS `lessons_lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lessons_lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `level` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `link` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessons_lesson`
--

LOCK TABLES `lessons_lesson` WRITE;
/*!40000 ALTER TABLE `lessons_lesson` DISABLE KEYS */;
INSERT INTO `lessons_lesson` VALUES (1,1,'The properties of solids, liquids and gases: Lesson 1','<iframe src=\"https://onedrive.live.com/embed?resid=3D33CEBA6673D86C%21225588&amp;authkey=%21AFy44iyx8HKAUYE&amp;em=2&amp;wdAr=1.7777777777777777\" width=\"962px\" height=\"565px\" frameborder=\"0\">This is an embedded <a target=\"_blank\" href=\"https://office.com\">Microsoft Office</a> presentation, powered by <a target=\"_blank\" href=\"https://office.com/webapps\">Office</a>.</iframe>'),(2,1,'The properties of solids, liquids and gases: Lesson 2','<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/wclY8F-UoTE\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>'),(3,1,'The properties of solids, liquids and gases: Lesson 3','<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/Asx1D31gRxA\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>'),(4,2,'The Particle Theory: Lesson 1','<iframe src=\"https://onedrive.live.com/embed?resid=3D33CEBA6673D86C%21225596&amp;authkey=%21ABjm7hhcZv8PoWQ&amp;em=2&amp;wdAr=1.7777777777777777\" width=\"962px\" height=\"565px\" frameborder=\"0\">This is an embedded <a target=\"_blank\" href=\"https://office.com\">Microsoft Office</a> presentation, powered by <a target=\"_blank\" href=\"https://office.com/webapps\">Office</a>.</iframe>'),(5,2,'The Particle Theory: Lesson 2','<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/OG9aBq3V24Y\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>'),(6,2,'The Particle Theory: Lesson 3','<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/Wn48reA1vBs\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>'),(7,2,'The Particle Theory: Lesson 4','<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/P6onnI6G3DI\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>'),(8,1,'The properties of solids, liquids and gases: Lesson 4','<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/h7ErVAZbeu0\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>');
/*!40000 ALTER TABLE `lessons_lesson` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-06 13:43:10
