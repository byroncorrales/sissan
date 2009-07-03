-- MySQL dump 10.11
--
-- Host: localhost    Database: sissan
-- ------------------------------------------------------
-- Server version	5.0.51a-3ubuntu5.4

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_5886d21f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `auth_message_user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add poblacion',8,'add_poblacion'),(23,'Can change poblacion',8,'change_poblacion'),(24,'Can delete poblacion',8,'delete_poblacion'),(25,'Can add departamento',9,'add_departamento'),(26,'Can change departamento',9,'change_departamento'),(27,'Can delete departamento',9,'delete_departamento'),(28,'Can add municipio',10,'add_municipio'),(29,'Can change municipio',10,'change_municipio'),(30,'Can delete municipio',10,'delete_municipio'),(31,'Can add version',11,'add_version'),(32,'Can change version',11,'change_version'),(33,'Can delete version',11,'delete_version'),(34,'Can add evolution',12,'add_evolution'),(35,'Can change evolution',12,'change_evolution'),(36,'Can delete evolution',12,'delete_evolution'),(37,'Can add log entry',13,'add_logentry'),(38,'Can change log entry',13,'change_logentry'),(39,'Can delete log entry',13,'delete_logentry');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user` (
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
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'django','','','byroncorrales@gmail.com','sha1$281b5$7d6e89ff0548323ce7116ec41ba1c3b58de43853',1,1,1,'2009-07-02 16:31:48','2009-06-30 00:46:00');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f116770` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

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
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `demografico_poblacion`
--

DROP TABLE IF EXISTS `demografico_poblacion`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `demografico_poblacion` (
  `id` int(11) NOT NULL auto_increment,
  `ano` int(11) NOT NULL,
  `total_ambos_sexos` int(11) NOT NULL,
  `total_hombre` int(11) NOT NULL,
  `total_mujer` int(11) NOT NULL,
  `urbano_ambos_sexos` int(11) NOT NULL,
  `urbano_hombre` int(11) NOT NULL,
  `urbano_mujer` int(11) NOT NULL,
  `rural_ambos_sexos` int(11) NOT NULL,
  `rural_hombre` int(11) NOT NULL,
  `rural_mujer` int(11) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `demografico_poblacion`
--

LOCK TABLES `demografico_poblacion` WRITE;
/*!40000 ALTER TABLE `demografico_poblacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `demografico_poblacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL auto_increment,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) default NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_admin_log_user_id` (`user_id`),
  KEY `django_admin_log_content_type_id` (`content_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'poblacion','demografico','poblacion'),(9,'departamento','lugar','departamento'),(10,'municipio','lugar','municipio'),(11,'version','django_evolution','version'),(12,'evolution','django_evolution','evolution'),(13,'log entry','admin','logentry');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_evolution`
--

DROP TABLE IF EXISTS `django_evolution`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_evolution` (
  `id` int(11) NOT NULL auto_increment,
  `version_id` int(11) NOT NULL,
  `app_label` varchar(200) NOT NULL,
  `label` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_evolution_version_id` (`version_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_evolution`
--

LOCK TABLES `django_evolution` WRITE;
/*!40000 ALTER TABLE `django_evolution` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_evolution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_project_version`
--

DROP TABLE IF EXISTS `django_project_version`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_project_version` (
  `id` int(11) NOT NULL auto_increment,
  `signature` longtext NOT NULL,
  `when` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_project_version`
--

LOCK TABLES `django_project_version` WRITE;
/*!40000 ALTER TABLE `django_project_version` DISABLE KEYS */;
INSERT INTO `django_project_version` VALUES (1,'(dp1\nS\'lugar\'\np2\n(dp3\nS\'Municipio\'\np4\n(dp5\nS\'fields\'\np6\n(dp7\nS\'nombre\'\np8\n(dp9\nS\'field_type\'\np10\ncdjango.db.models.fields\nCharField\np11\nsS\'max_length\'\np12\nI30\nssS\'id\'\np13\n(dp14\ng10\ncdjango.db.models.fields\nAutoField\np15\nsS\'primary_key\'\np16\nI01\nssS\'departamento\'\np17\n(dp18\ng10\ncdjango.db.models.fields.related\nForeignKey\np19\nsS\'related_model\'\np20\nS\'lugar.Departamento\'\np21\nsssS\'meta\'\np22\n(dp23\nS\'unique_together\'\np24\n(lp25\nsS\'db_table\'\np26\nS\'lugar_municipio\'\np27\nsS\'db_tablespace\'\np28\nS\'\'\nsS\'pk_column\'\np29\ng13\nsssS\'Departamento\'\np30\n(dp31\ng6\n(dp32\ng8\n(dp33\ng10\ng11\nsg12\nI30\nssS\'numero\'\np34\n(dp35\ng10\ncdjango.db.models.fields\nDecimalField\np36\nsg16\nI01\nsS\'decimal_places\'\np37\nI0\nsS\'max_digits\'\np38\nI2\nsssg22\n(dp39\ng24\n(lp40\nsg26\nS\'lugar_departamento\'\np41\nsg28\nS\'\'\nsg29\ng34\nssssS\'sessions\'\np42\n(dp43\nS\'Session\'\np44\n(dp45\ng6\n(dp46\nS\'session_key\'\np47\n(dp48\ng10\ng11\nsg12\nI40\nsg16\nI01\nssS\'expire_date\'\np49\n(dp50\ng10\ncdjango.db.models.fields\nDateTimeField\np51\nssS\'session_data\'\np52\n(dp53\ng10\ncdjango.db.models.fields\nTextField\np54\nsssg22\n(dp55\ng24\n(lp56\nsg26\nS\'django_session\'\np57\nsg28\nS\'\'\nsg29\ng47\nssssS\'sites\'\np58\n(dp59\nS\'Site\'\np60\n(dp61\ng6\n(dp62\nS\'domain\'\np63\n(dp64\ng10\ng11\nsg12\nI100\nssg13\n(dp65\ng10\ng15\nsg16\nI01\nssS\'name\'\np66\n(dp67\ng10\ng11\nsg12\nI50\nsssg22\n(dp68\ng24\n(lp69\nsg26\nS\'django_site\'\np70\nsg28\nS\'\'\nsg29\ng13\nssssS\'auth\'\np71\n(dp72\nS\'Message\'\np73\n(dp74\ng6\n(dp75\nS\'message\'\np76\n(dp77\ng10\ng54\nssg13\n(dp78\ng10\ng15\nsg16\nI01\nssS\'user\'\np79\n(dp80\ng10\ng19\nsg20\nS\'auth.User\'\np81\nsssg22\n(dp82\ng24\n(lp83\nsg26\nS\'auth_message\'\np84\nsg28\nS\'\'\nsg29\ng13\nsssS\'Group\'\np85\n(dp86\ng6\n(dp87\nS\'permissions\'\np88\n(dp89\ng10\ncdjango.db.models.fields.related\nManyToManyField\np90\nsg20\nS\'auth.Permission\'\np91\nssg13\n(dp92\ng10\ng15\nsg16\nI01\nssg66\n(dp93\ng10\ng11\nsS\'unique\'\np94\nI01\nsg12\nI80\nsssg22\n(dp95\ng24\n(lp96\nsg26\nS\'auth_group\'\np97\nsg28\nS\'\'\nsg29\ng13\nsssS\'User\'\np98\n(dp99\ng6\n(dp100\nS\'username\'\np101\n(dp102\ng10\ng11\nsg94\nI01\nsg12\nI30\nssS\'first_name\'\np103\n(dp104\ng10\ng11\nsg12\nI30\nssS\'last_name\'\np105\n(dp106\ng10\ng11\nsg12\nI30\nssS\'is_active\'\np107\n(dp108\ng10\ncdjango.db.models.fields\nBooleanField\np109\nssS\'email\'\np110\n(dp111\ng10\ncdjango.db.models.fields\nEmailField\np112\nsg12\nI75\nssS\'is_superuser\'\np113\n(dp114\ng10\ng109\nssS\'is_staff\'\np115\n(dp116\ng10\ng109\nssS\'last_login\'\np117\n(dp118\ng10\ng51\nssS\'groups\'\np119\n(dp120\ng10\ng90\nsg20\nS\'auth.Group\'\np121\nssS\'user_permissions\'\np122\n(dp123\ng10\ng90\nsg20\nS\'auth.Permission\'\np124\nssS\'password\'\np125\n(dp126\ng10\ng11\nsg12\nI128\nssg13\n(dp127\ng10\ng15\nsg16\nI01\nssS\'date_joined\'\np128\n(dp129\ng10\ng51\nsssg22\n(dp130\ng24\n(lp131\nsg26\nS\'auth_user\'\np132\nsg28\nS\'\'\nsg29\ng13\nsssS\'Permission\'\np133\n(dp134\ng6\n(dp135\nS\'codename\'\np136\n(dp137\ng10\ng11\nsg12\nI100\nssg13\n(dp138\ng10\ng15\nsg16\nI01\nssS\'content_type\'\np139\n(dp140\ng10\ng19\nsg20\nS\'contenttypes.ContentType\'\np141\nssg66\n(dp142\ng10\ng11\nsg12\nI50\nsssg22\n(dp143\ng24\n((S\'content_type\'\nS\'codename\'\nttp144\nsg26\nS\'auth_permission\'\np145\nsg28\nS\'\'\nsg29\ng13\nssssS\'demografico\'\np146\n(dp147\nS\'Poblacion\'\np148\n(dp149\ng6\n(dp150\nS\'ano\'\np151\n(dp152\ng10\ncdjango.db.models.fields\nIntegerField\np153\nsg12\nI5\nssS\'urbano_ambos_sexos\'\np154\n(dp155\ng10\ng153\nsg12\nI10\nssS\'urbano_hombre\'\np156\n(dp157\ng10\ng153\nsg12\nI10\nssS\'rural_hombre\'\np158\n(dp159\ng10\ng153\nsg12\nI10\nssS\'total_ambos_sexos\'\np160\n(dp161\ng10\ng153\nsg12\nI10\nssS\'total_mujer\'\np162\n(dp163\ng10\ng153\nsg12\nI10\nssS\'total_hombre\'\np164\n(dp165\ng10\ng153\nsg12\nI10\nssS\'rural_ambos_sexos\'\np166\n(dp167\ng10\ng153\nsg12\nI10\nssS\'rural_mujer\'\np168\n(dp169\ng10\ng153\nsg12\nI10\nssS\'urbano_mujer\'\np170\n(dp171\ng10\ng153\nsg12\nI10\nssg13\n(dp172\ng10\ng15\nsg16\nI01\nsssg22\n(dp173\ng24\n(lp174\nsg26\nS\'demografico_poblacion\'\np175\nsg28\nS\'\'\nsg29\ng13\nssssS\'contenttypes\'\np176\n(dp177\nS\'ContentType\'\np178\n(dp179\ng6\n(dp180\nS\'model\'\np181\n(dp182\ng10\ng11\nsg12\nI100\nssS\'app_label\'\np183\n(dp184\ng10\ng11\nsg12\nI100\nssg13\n(dp185\ng10\ng15\nsg16\nI01\nssg66\n(dp186\ng10\ng11\nsg12\nI100\nsssg22\n(dp187\ng24\n((S\'app_label\'\nS\'model\'\nttp188\nsg26\nS\'django_content_type\'\np189\nsg28\nS\'\'\nsg29\ng13\nssssS\'django_evolution\'\np190\n(dp191\nS\'Evolution\'\np192\n(dp193\ng6\n(dp194\nS\'label\'\np195\n(dp196\ng10\ng11\nsg12\nI100\nssS\'version\'\np197\n(dp198\ng10\ng19\nsg20\nS\'django_evolution.Version\'\np199\nssg13\n(dp200\ng10\ng15\nsg16\nI01\nssg183\n(dp201\ng10\ng11\nsg12\nI200\nsssg22\n(dp202\ng24\n(lp203\nsg26\nS\'django_evolution\'\np204\nsg28\nS\'\'\nsg29\ng13\nsssS\'Version\'\np205\n(dp206\ng6\n(dp207\nS\'when\'\np208\n(dp209\ng10\ng51\nssg13\n(dp210\ng10\ng15\nsg16\nI01\nssS\'signature\'\np211\n(dp212\ng10\ng54\nsssg22\n(dp213\ng24\n(lp214\nsg26\nS\'django_project_version\'\np215\nsg28\nS\'\'\nsg29\ng13\nssssS\'__version__\'\np216\nI1\ns.','2009-07-02 16:28:06'),(2,'(dp1\nS\'lugar\'\np2\n(dp3\nS\'Departamento\'\np4\n(dp5\nS\'fields\'\np6\n(dp7\nS\'nombre\'\np8\n(dp9\nS\'field_type\'\np10\ncdjango.db.models.fields\nCharField\np11\nsS\'max_length\'\np12\nI30\nssS\'numero\'\np13\n(dp14\ng10\ncdjango.db.models.fields\nDecimalField\np15\nsS\'primary_key\'\np16\nI01\nsS\'decimal_places\'\np17\nI0\nsS\'max_digits\'\np18\nI2\nsssS\'meta\'\np19\n(dp20\nS\'unique_together\'\np21\n(lp22\nsS\'db_table\'\np23\nS\'lugar_departamento\'\np24\nsS\'db_tablespace\'\np25\nS\'\'\nsS\'pk_column\'\np26\ng13\nsssS\'Municipio\'\np27\n(dp28\ng6\n(dp29\ng8\n(dp30\ng10\ng11\nsg12\nI30\nssS\'id\'\np31\n(dp32\ng10\ncdjango.db.models.fields\nAutoField\np33\nsg16\nI01\nssS\'departamento\'\np34\n(dp35\ng10\ncdjango.db.models.fields.related\nForeignKey\np36\nsS\'related_model\'\np37\nS\'lugar.Departamento\'\np38\nsssg19\n(dp39\ng21\n(lp40\nsg23\nS\'lugar_municipio\'\np41\nsg25\nS\'\'\nsg26\ng31\nssssS\'sessions\'\np42\n(dp43\nS\'Session\'\np44\n(dp45\ng6\n(dp46\nS\'session_key\'\np47\n(dp48\ng10\ng11\nsg12\nI40\nsg16\nI01\nssS\'session_data\'\np49\n(dp50\ng10\ncdjango.db.models.fields\nTextField\np51\nssS\'expire_date\'\np52\n(dp53\ng10\ncdjango.db.models.fields\nDateTimeField\np54\nsssg19\n(dp55\ng21\n(lp56\nsg23\nS\'django_session\'\np57\nsg25\nS\'\'\nsg26\ng47\nssssS\'admin\'\np58\n(dp59\nS\'LogEntry\'\np60\n(dp61\nS\'fields\'\np62\n(dp63\nS\'action_flag\'\np64\n(dp65\nS\'field_type\'\np66\ncdjango.db.models.fields\nPositiveSmallIntegerField\np67\nssS\'action_time\'\np68\n(dp69\ng66\ng54\nssS\'object_repr\'\np70\n(dp71\ng66\ng11\nsS\'max_length\'\np72\nI200\nssS\'object_id\'\np73\n(dp74\ng66\ng51\nsS\'null\'\np75\nI01\nssS\'change_message\'\np76\n(dp77\ng66\ng51\nssS\'user\'\np78\n(dp79\ng66\ng36\nsS\'related_model\'\np80\nS\'auth.User\'\np81\nssS\'content_type\'\np82\n(dp83\ng66\ng36\nsg75\nI01\nsg80\nS\'contenttypes.ContentType\'\np84\nssS\'id\'\np85\n(dp86\ng66\ng33\nsS\'primary_key\'\np87\nI01\nsssS\'meta\'\np88\n(dp89\nS\'unique_together\'\np90\n(lp91\nsS\'db_table\'\np92\nS\'django_admin_log\'\np93\nsS\'db_tablespace\'\np94\nS\'\'\nsS\'pk_column\'\np95\ng85\nssssS\'demografico\'\np96\n(dp97\nS\'Poblacion\'\np98\n(dp99\ng6\n(dp100\nS\'ano\'\np101\n(dp102\ng10\ncdjango.db.models.fields\nIntegerField\np103\nsg12\nI5\nssS\'urbano_ambos_sexos\'\np104\n(dp105\ng10\ng103\nsg12\nI10\nssS\'urbano_hombre\'\np106\n(dp107\ng10\ng103\nsg12\nI10\nssS\'rural_hombre\'\np108\n(dp109\ng10\ng103\nsg12\nI10\nssS\'total_ambos_sexos\'\np110\n(dp111\ng10\ng103\nsg12\nI10\nssS\'total_mujer\'\np112\n(dp113\ng10\ng103\nsg12\nI10\nssS\'total_hombre\'\np114\n(dp115\ng10\ng103\nsg12\nI10\nssS\'rural_ambos_sexos\'\np116\n(dp117\ng10\ng103\nsg12\nI10\nssS\'rural_mujer\'\np118\n(dp119\ng10\ng103\nsg12\nI10\nssS\'urbano_mujer\'\np120\n(dp121\ng10\ng103\nsg12\nI10\nssg31\n(dp122\ng10\ng33\nsg16\nI01\nsssg19\n(dp123\ng21\n(lp124\nsg23\nS\'demografico_poblacion\'\np125\nsg25\nS\'\'\nsg26\ng31\nssssS\'auth\'\np126\n(dp127\nS\'Message\'\np128\n(dp129\ng6\n(dp130\nS\'message\'\np131\n(dp132\ng10\ng51\nssg31\n(dp133\ng10\ng33\nsg16\nI01\nssS\'user\'\np134\n(dp135\ng10\ng36\nsg37\nS\'auth.User\'\np136\nsssg19\n(dp137\ng21\n(lp138\nsg23\nS\'auth_message\'\np139\nsg25\nS\'\'\nsg26\ng31\nsssS\'Group\'\np140\n(dp141\ng6\n(dp142\ng31\n(dp143\ng10\ng33\nsg16\nI01\nssS\'name\'\np144\n(dp145\ng12\nI80\nsg10\ng11\nsS\'unique\'\np146\nI01\nssS\'permissions\'\np147\n(dp148\ng10\ncdjango.db.models.fields.related\nManyToManyField\np149\nsg37\nS\'auth.Permission\'\np150\nsssg19\n(dp151\ng21\n(lp152\nsg23\nS\'auth_group\'\np153\nsg25\nS\'\'\nsg26\ng31\nsssS\'User\'\np154\n(dp155\ng6\n(dp156\nS\'username\'\np157\n(dp158\ng12\nI30\nsg10\ng11\nsg146\nI01\nssS\'first_name\'\np159\n(dp160\ng10\ng11\nsg12\nI30\nssS\'last_name\'\np161\n(dp162\ng10\ng11\nsg12\nI30\nssS\'is_active\'\np163\n(dp164\ng10\ncdjango.db.models.fields\nBooleanField\np165\nssg31\n(dp166\ng10\ng33\nsg16\nI01\nssS\'is_superuser\'\np167\n(dp168\ng10\ng165\nssS\'is_staff\'\np169\n(dp170\ng10\ng165\nssS\'last_login\'\np171\n(dp172\ng10\ng54\nssS\'groups\'\np173\n(dp174\ng10\ng149\nsg37\nS\'auth.Group\'\np175\nssS\'user_permissions\'\np176\n(dp177\ng10\ng149\nsg37\nS\'auth.Permission\'\np178\nssS\'password\'\np179\n(dp180\ng10\ng11\nsg12\nI128\nssS\'email\'\np181\n(dp182\ng10\ncdjango.db.models.fields\nEmailField\np183\nsg12\nI75\nssS\'date_joined\'\np184\n(dp185\ng10\ng54\nsssg19\n(dp186\ng21\n(lp187\nsg23\nS\'auth_user\'\np188\nsg25\nS\'\'\nsg26\ng31\nsssS\'Permission\'\np189\n(dp190\ng6\n(dp191\nS\'codename\'\np192\n(dp193\ng10\ng11\nsg12\nI100\nssg31\n(dp194\ng10\ng33\nsg16\nI01\nssS\'content_type\'\np195\n(dp196\ng10\ng36\nsg37\nS\'contenttypes.ContentType\'\np197\nssg144\n(dp198\ng10\ng11\nsg12\nI50\nsssg19\n(dp199\ng21\n((S\'content_type\'\nS\'codename\'\nttp200\nsg23\nS\'auth_permission\'\np201\nsg25\nS\'\'\nsg26\ng31\nssssS\'sites\'\np202\n(dp203\nS\'Site\'\np204\n(dp205\ng6\n(dp206\nS\'domain\'\np207\n(dp208\ng10\ng11\nsg12\nI100\nssg31\n(dp209\ng10\ng33\nsg16\nI01\nssg144\n(dp210\ng10\ng11\nsg12\nI50\nsssg19\n(dp211\ng21\n(lp212\nsg23\nS\'django_site\'\np213\nsg25\nS\'\'\nsg26\ng31\nssssS\'contenttypes\'\np214\n(dp215\nS\'ContentType\'\np216\n(dp217\ng6\n(dp218\nS\'model\'\np219\n(dp220\ng10\ng11\nsg12\nI100\nssg31\n(dp221\ng10\ng33\nsg16\nI01\nssg144\n(dp222\ng10\ng11\nsg12\nI100\nssS\'app_label\'\np223\n(dp224\ng10\ng11\nsg12\nI100\nsssg19\n(dp225\ng21\n((S\'app_label\'\nS\'model\'\nttp226\nsg23\nS\'django_content_type\'\np227\nsg25\nS\'\'\nsg26\ng31\nssssS\'django_evolution\'\np228\n(dp229\nS\'Evolution\'\np230\n(dp231\ng6\n(dp232\ng223\n(dp233\ng10\ng11\nsg12\nI200\nssS\'version\'\np234\n(dp235\ng10\ng36\nsg37\nS\'django_evolution.Version\'\np236\nssg31\n(dp237\ng10\ng33\nsg16\nI01\nssS\'label\'\np238\n(dp239\ng10\ng11\nsg12\nI100\nsssg19\n(dp240\ng21\n(lp241\nsg23\nS\'django_evolution\'\np242\nsg25\nS\'\'\nsg26\ng31\nsssS\'Version\'\np243\n(dp244\ng6\n(dp245\nS\'when\'\np246\n(dp247\ng10\ng54\nssg31\n(dp248\ng10\ng33\nsg16\nI01\nssS\'signature\'\np249\n(dp250\ng10\ng51\nsssg19\n(dp251\ng21\n(lp252\nsg23\nS\'django_project_version\'\np253\nsg25\nS\'\'\nsg26\ng31\nssssS\'__version__\'\np254\nI1\ns.','2009-07-02 16:32:14');
/*!40000 ALTER TABLE `django_project_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('53d1f2ca1d28358d74939bd942798c6f','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS45NjRmNGViMWE2ZWQxNDczODgz\nMTI4YmY2MjVkZTBjMA==\n','2009-07-16 16:31:48');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_departamento`
--

DROP TABLE IF EXISTS `lugar_departamento`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `lugar_departamento` (
  `nombre` varchar(30) NOT NULL,
  `numero` decimal(2,0) NOT NULL,
  PRIMARY KEY  (`numero`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `lugar_departamento`
--

LOCK TABLES `lugar_departamento` WRITE;
/*!40000 ALTER TABLE `lugar_departamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `lugar_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_municipio`
--

DROP TABLE IF EXISTS `lugar_municipio`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `lugar_municipio` (
  `id` int(11) NOT NULL auto_increment,
  `nombre` varchar(30) NOT NULL,
  `departamento_id` decimal(2,0) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `lugar_municipio_departamento_id` (`departamento_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `lugar_municipio`
--

LOCK TABLES `lugar_municipio` WRITE;
/*!40000 ALTER TABLE `lugar_municipio` DISABLE KEYS */;
/*!40000 ALTER TABLE `lugar_municipio` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2009-07-03  3:33:05
