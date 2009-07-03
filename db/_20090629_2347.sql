-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.0.51a-3ubuntu5.4


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema sissan
--

CREATE DATABASE IF NOT EXISTS sissan;
USE sissan;

--
-- Definition of table `sissan`.`auth_group`
--

DROP TABLE IF EXISTS `sissan`.`auth_group`;
CREATE TABLE  `sissan`.`auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`auth_group`
--

/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
LOCK TABLES `auth_group` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;


--
-- Definition of table `sissan`.`auth_group_permissions`
--

DROP TABLE IF EXISTS `sissan`.`auth_group_permissions`;
CREATE TABLE  `sissan`.`auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_5886d21f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`auth_group_permissions`
--

/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
LOCK TABLES `auth_group_permissions` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;


--
-- Definition of table `sissan`.`auth_message`
--

DROP TABLE IF EXISTS `sissan`.`auth_message`;
CREATE TABLE  `sissan`.`auth_message` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `auth_message_user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`auth_message`
--

/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
LOCK TABLES `auth_message` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;


--
-- Definition of table `sissan`.`auth_permission`
--

DROP TABLE IF EXISTS `sissan`.`auth_permission`;
CREATE TABLE  `sissan`.`auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`auth_permission`
--

/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
LOCK TABLES `auth_permission` WRITE;
INSERT INTO `sissan`.`auth_permission` VALUES  (1,'Can add permission',1,'add_permission'),
 (2,'Can change permission',1,'change_permission'),
 (3,'Can delete permission',1,'delete_permission'),
 (4,'Can add group',2,'add_group'),
 (5,'Can change group',2,'change_group'),
 (6,'Can delete group',2,'delete_group'),
 (7,'Can add user',3,'add_user'),
 (8,'Can change user',3,'change_user'),
 (9,'Can delete user',3,'delete_user'),
 (10,'Can add message',4,'add_message'),
 (11,'Can change message',4,'change_message'),
 (12,'Can delete message',4,'delete_message'),
 (13,'Can add content type',5,'add_contenttype'),
 (14,'Can change content type',5,'change_contenttype'),
 (15,'Can delete content type',5,'delete_contenttype'),
 (16,'Can add session',6,'add_session'),
 (17,'Can change session',6,'change_session'),
 (18,'Can delete session',6,'delete_session'),
 (19,'Can add site',7,'add_site'),
 (20,'Can change site',7,'change_site'),
 (21,'Can delete site',7,'delete_site');
UNLOCK TABLES;
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;


--
-- Definition of table `sissan`.`auth_user`
--

DROP TABLE IF EXISTS `sissan`.`auth_user`;
CREATE TABLE  `sissan`.`auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`auth_user`
--

/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
LOCK TABLES `auth_user` WRITE;
INSERT INTO `sissan`.`auth_user` VALUES  (1,'django','','','byroncorrales@gmail.com','sha1$281b5$7d6e89ff0548323ce7116ec41ba1c3b58de43853',1,1,1,'2009-06-30 00:46:00','2009-06-30 00:46:00');
UNLOCK TABLES;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;


--
-- Definition of table `sissan`.`auth_user_groups`
--

DROP TABLE IF EXISTS `sissan`.`auth_user_groups`;
CREATE TABLE  `sissan`.`auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f116770` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`auth_user_groups`
--

/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
LOCK TABLES `auth_user_groups` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;


--
-- Definition of table `sissan`.`auth_user_user_permissions`
--

DROP TABLE IF EXISTS `sissan`.`auth_user_user_permissions`;
CREATE TABLE  `sissan`.`auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`auth_user_user_permissions`
--

/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
LOCK TABLES `auth_user_user_permissions` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


--
-- Definition of table `sissan`.`django_content_type`
--

DROP TABLE IF EXISTS `sissan`.`django_content_type`;
CREATE TABLE  `sissan`.`django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`django_content_type`
--

/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
LOCK TABLES `django_content_type` WRITE;
INSERT INTO `sissan`.`django_content_type` VALUES  (1,'permission','auth','permission'),
 (2,'group','auth','group'),
 (3,'user','auth','user'),
 (4,'message','auth','message'),
 (5,'content type','contenttypes','contenttype'),
 (6,'session','sessions','session'),
 (7,'site','sites','site');
UNLOCK TABLES;
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;


--
-- Definition of table `sissan`.`django_session`
--

DROP TABLE IF EXISTS `sissan`.`django_session`;
CREATE TABLE  `sissan`.`django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`django_session`
--

/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
LOCK TABLES `django_session` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;


--
-- Definition of table `sissan`.`django_site`
--

DROP TABLE IF EXISTS `sissan`.`django_site`;
CREATE TABLE  `sissan`.`django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sissan`.`django_site`
--

/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
LOCK TABLES `django_site` WRITE;
INSERT INTO `sissan`.`django_site` VALUES  (1,'example.com','example.com');
UNLOCK TABLES;
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
