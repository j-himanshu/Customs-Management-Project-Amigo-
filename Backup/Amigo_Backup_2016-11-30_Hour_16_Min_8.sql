-- MySQL dump 10.14  Distrib 5.5.52-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: customs
-- ------------------------------------------------------
-- Server version	10.1.19-MariaDB

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `pword` varchar(20) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('admin','admin'),('User','PasswordA123a');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_of_landing`
--

DROP TABLE IF EXISTS `bill_of_landing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill_of_landing` (
  `bol_id` int(11) NOT NULL,
  `country_code` int(11) DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL,
  `manifest_id` int(11) DEFAULT NULL,
  `bill_amount` float DEFAULT NULL,
  PRIMARY KEY (`bol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_of_landing`
--

LOCK TABLES `bill_of_landing` WRITE;
/*!40000 ALTER TABLE `bill_of_landing` DISABLE KEYS */;
INSERT INTO `bill_of_landing` VALUES (884,91,'2016-11-13',9116,130.36),(2940,1,'2016-11-27',7060,8488.12),(3004,1,'2016-11-28',6996,8488.12),(3742,1,'2016-11-14',6258,14770.5),(3907,91,'2016-11-25',6093,90.2),(4779,91,'2016-11-28',5221,2713.13),(4977,91,'2016-11-25',5023,90.2),(5188,1,'2016-11-23',4812,8488.12),(5622,91,'2016-11-13',4378,90.2),(5696,91,'2016-11-28',4304,4763.64),(5699,1,'2016-11-27',4301,8488.12),(6075,91,'2016-11-14',3925,130.36),(6127,3,'2016-11-28',3873,3295.27),(7945,91,'2016-11-29',2055,2713.13),(8069,1,'2016-11-28',1931,8488.12),(9142,91,'2016-11-14',858,90.2),(9345,3,'2016-11-28',655,5547.63),(9352,91,'2016-11-14',648,90.2);
/*!40000 ALTER TABLE `bill_of_landing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carrier`
--

DROP TABLE IF EXISTS `carrier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carrier` (
  `carrier_id` int(11) NOT NULL,
  `carrier_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`carrier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrier`
--

LOCK TABLES `carrier` WRITE;
/*!40000 ALTER TABLE `carrier` DISABLE KEYS */;
INSERT INTO `carrier` VALUES (1,'Bluedart'),(2,'DTDC'),(3,'FedEx'),(4,'Amazon Delivery'),(5,'Indian Post'),(8,'ProfessionalCourier');
/*!40000 ALTER TABLE `carrier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'Lufthansa'),(2,'Fly Emirates'),(3,'Go Indigo'),(4,'Jet Airways'),(5,'Air India');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `country` (
  `country_code` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `duty` float DEFAULT NULL,
  `excise` float DEFAULT NULL,
  `charges` float DEFAULT NULL,
  PRIMARY KEY (`country_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (1,'USA',15.88,4000,7803.35),(3,'Sri Lanka',13.8,3476.9,2800),(91,'India',12.5,1200,2550.38);
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location` (
  `company_id` int(11) DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'India'),(1,'UAE'),(1,'USA'),(1,'CHINA'),(2,'India'),(2,'USA'),(2,'Germany'),(2,'UAE'),(3,'India'),(4,'India'),(4,'Russia'),(4,'Japan'),(5,'India');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manifest`
--

DROP TABLE IF EXISTS `manifest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manifest` (
  `manifest_id` int(11) NOT NULL,
  `carrier_id` int(11) DEFAULT NULL,
  `issuer_id` int(11) DEFAULT NULL,
  `mode_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `remarks` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`manifest_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manifest`
--

LOCK TABLES `manifest` WRITE;
/*!40000 ALTER TABLE `manifest` DISABLE KEYS */;
INSERT INTO `manifest` VALUES (648,3,4,4,5,'electronic item'),(655,1,8,2,6,''),(858,5,6,4,5,'electronic item'),(1931,3,2,4,1,''),(3873,4,6,4,5,''),(3925,3,7,1,6,'wheat grain, aged (5 years), for commercial sale'),(4301,3,5,2,4,'Books.'),(4304,2,8,2,8,''),(4378,5,2,1,3,'fragile electronic item. Handle with care'),(4812,5,8,2,4,'computer science programming book. Delivery to pub'),(5023,2,7,5,1,'General grocery'),(5221,4,6,4,5,''),(6093,4,3,2,3,''),(6258,4,4,1,8,'aged basmati rice. continental. sale.'),(6996,4,4,6,3,''),(7060,4,3,4,5,'electrical iterm, comp. delv. rec'),(9116,4,5,3,6,'fresh wheat. south-east asia origin.');
/*!40000 ALTER TABLE `manifest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manifest_issuer`
--

DROP TABLE IF EXISTS `manifest_issuer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manifest_issuer` (
  `issuer_id` int(11) NOT NULL,
  `issuer_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`issuer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manifest_issuer`
--

LOCK TABLES `manifest_issuer` WRITE;
/*!40000 ALTER TABLE `manifest_issuer` DISABLE KEYS */;
INSERT INTO `manifest_issuer` VALUES (1,'Prakash Jha'),(2,'Naman Ojha'),(3,'Shivkumar Sinha'),(4,'Hamid Khureshi'),(5,'Soumya Nigam'),(6,'Arun Pratap'),(7,'Archana Gupta'),(8,'Falak Ul Rehman'),(9,'Srinidhi Ahuja');
/*!40000 ALTER TABLE `manifest_issuer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manifest_port`
--

DROP TABLE IF EXISTS `manifest_port`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manifest_port` (
  `manifest_id` int(11) DEFAULT NULL,
  `from_port_id` int(11) DEFAULT NULL,
  `to_port_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manifest_port`
--

LOCK TABLES `manifest_port` WRITE;
/*!40000 ALTER TABLE `manifest_port` DISABLE KEYS */;
INSERT INTO `manifest_port` VALUES (9116,4,2),(4378,3,1),(3925,5,1),(858,3,2),(6258,7,2),(648,1,2),(4812,4,6),(5023,5,3),(6093,1,2),(4301,3,9),(7060,7,10),(6996,10,7),(1931,4,6),(4304,3,9),(655,3,10),(5221,9,4),(3873,9,4),(2055,7,10);
/*!40000 ALTER TABLE `manifest_port` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mode_of_transport`
--

DROP TABLE IF EXISTS `mode_of_transport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mode_of_transport` (
  `mode_id` int(11) NOT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mode_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mode_of_transport`
--

LOCK TABLES `mode_of_transport` WRITE;
/*!40000 ALTER TABLE `mode_of_transport` DISABLE KEYS */;
INSERT INTO `mode_of_transport` VALUES (1,'Air- Commercial'),(2,'Air-Private'),(3,'Air- Government Dock'),(4,'Water(Cruise ship)'),(5,'RoadWays(Normal)'),(6,'RoadWays(Border)');
/*!40000 ALTER TABLE `mode_of_transport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `port`
--

DROP TABLE IF EXISTS `port`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `port` (
  `port_id` int(11) NOT NULL,
  `port_name` varchar(20) DEFAULT NULL,
  `country_code` int(11) DEFAULT NULL,
  PRIMARY KEY (`port_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `port`
--

LOCK TABLES `port` WRITE;
/*!40000 ALTER TABLE `port` DISABLE KEYS */;
INSERT INTO `port` VALUES (1,'Vishakhapatnum',91),(2,'Chennai',91),(3,'Mumbai',91),(4,'Srirangapatna',91),(5,'Howraw',91),(6,'Florida',1),(7,'Buffalo',1),(9,'Montana',1),(10,'Bahamas',1);
/*!40000 ALTER TABLE `port` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `category` varchar(20) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `weight` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'General','Toothbrush',1),(2,'Explosive','Cigerrate',5),(3,'Electrical','Samsung Plasma LED TV',2),(4,'Books','Programming in Python',8),(5,'Electrical Appliance','Hair Dryer',1),(6,'Eatables','Dry Wheat Grain',7000),(7,'Malicious','Cigerrate',10),(8,'Eatables','Rice',500),(9,'Malicious','Alcohol',1),(10,'Malicious','FireCracker',1075);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_by`
--

DROP TABLE IF EXISTS `service_by`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_by` (
  `carrier_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_by`
--

LOCK TABLES `service_by` WRITE;
/*!40000 ALTER TABLE `service_by` DISABLE KEYS */;
INSERT INTO `service_by` VALUES (1,5),(2,3),(3,1),(4,5),(5,5),(8,3);
/*!40000 ALTER TABLE `service_by` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-30 16:08:48
