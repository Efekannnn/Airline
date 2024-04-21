-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: ucakyolcu
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `biletler`
--

DROP TABLE IF EXISTS `biletler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `biletler` (
  `bilet_id` int NOT NULL AUTO_INCREMENT,
  `yolcu_id` int DEFAULT NULL,
  `ucus_id` int DEFAULT NULL,
  `fiyat` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`bilet_id`),
  KEY `yolcu_id` (`yolcu_id`),
  KEY `ucus_id` (`ucus_id`),
  CONSTRAINT `biletler_ibfk_1` FOREIGN KEY (`yolcu_id`) REFERENCES `yolcu` (`yolcu_id`),
  CONSTRAINT `biletler_ibfk_2` FOREIGN KEY (`ucus_id`) REFERENCES `ucuslar` (`ucus_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `havaalanlari`
--

DROP TABLE IF EXISTS `havaalanlari`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `havaalanlari` (
  `havaalani_id` int NOT NULL,
  `havaalani_kodu` varchar(10) DEFAULT NULL,
  `havaalani_adi` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`havaalani_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ucaklar`
--

DROP TABLE IF EXISTS `ucaklar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ucaklar` (
  `ucak_id` int NOT NULL,
  `ucak_modeli` varchar(100) DEFAULT NULL,
  `koltuk_sayisi` int DEFAULT NULL,
  PRIMARY KEY (`ucak_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ucuslar`
--

DROP TABLE IF EXISTS `ucuslar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ucuslar` (
  `ucus_id` int NOT NULL,
  `kalkis_havaalani_id` int DEFAULT NULL,
  `varis_havaalani_id` int DEFAULT NULL,
  `kalkis_zamani` datetime DEFAULT NULL,
  `varis_zamani` datetime DEFAULT NULL,
  `ucak_id` int DEFAULT NULL,
  PRIMARY KEY (`ucus_id`),
  KEY `kalkis_havaalani_id` (`kalkis_havaalani_id`),
  KEY `varis_havaalani_id` (`varis_havaalani_id`),
  KEY `ucak_id` (`ucak_id`),
  CONSTRAINT `ucuslar_ibfk_1` FOREIGN KEY (`kalkis_havaalani_id`) REFERENCES `havaalanlari` (`havaalani_id`),
  CONSTRAINT `ucuslar_ibfk_2` FOREIGN KEY (`varis_havaalani_id`) REFERENCES `havaalanlari` (`havaalani_id`),
  CONSTRAINT `ucuslar_ibfk_3` FOREIGN KEY (`ucak_id`) REFERENCES `ucaklar` (`ucak_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `yolcu`
--

DROP TABLE IF EXISTS `yolcu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `yolcu` (
  `yolcu_id` int NOT NULL,
  `ad` varchar(50) DEFAULT NULL,
  `soyad` varchar(50) DEFAULT NULL,
  `cinsiyet` varchar(10) DEFAULT NULL,
  `dogum_tarihi` date DEFAULT NULL,
  PRIMARY KEY (`yolcu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `yolcubilgi`
--

DROP TABLE IF EXISTS `yolcubilgi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `yolcubilgi` (
  `bilgi_id` int NOT NULL,
  `yolcu_id` int DEFAULT NULL,
  `telefon` varchar(20) DEFAULT NULL,
  `e_posta` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bilgi_id`),
  KEY `yolcu_id` (`yolcu_id`),
  CONSTRAINT `yolcubilgi_ibfk_1` FOREIGN KEY (`yolcu_id`) REFERENCES `yolcu` (`yolcu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-19 20:34:15
