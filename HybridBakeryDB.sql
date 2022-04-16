CREATE DATABASE  IF NOT EXISTS `hybrid_bakery` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hybrid_bakery`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hybrid_bakery
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `allergen`
--

DROP TABLE IF EXISTS `allergen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allergen` (
  `id` int NOT NULL AUTO_INCREMENT,
  `allergen_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `allergen`
--

LOCK TABLES `allergen` WRITE;
/*!40000 ALTER TABLE `allergen` DISABLE KEYS */;
INSERT INTO `allergen` VALUES (1,'Tree Nuts'),(2,'Gluten'),(3,'Milk'),(4,'Eggs'),(5,'Peanuts');
/*!40000 ALTER TABLE `allergen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `product_description` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Brookie',5.00,'Brookies are bars made from marbled layers of fudgy brownie batter and cakey chocolate chip cookie dough. These are also gluten free!'),(2,'Cronut',6.00,'The Cronut is a croissant-doughnut pastry. It resembles a doughnut and is made from croissant-like dough which is filled with flavored cream and fried in grapeseed oil. The Cronut in its current form was invented in 2013 by French-American pastry chef Dominique Ansel.'),(3,'Cruffin',8.00,'A Cruffin is made from a buttery croissant pastry that has been moulded into a muffin shape and packed with a tasty filling. Once baked, the Cruffin has the crispy, flaky exterior of a croissant, but the doughy centre of a muffin.'),(4,'Duffin',3.70,'Muffin meets doughnut with a raspberry filling'),(5,'Cragel',3.25,'Bagel shaped, croissant-style pastry'),(6,'Townie',4.50,'A Tart-Brownie hybrid'),(7,'Cretzel',3.99,'A croissant - pretzel mix'),(8,'Wonut',2.75,'We\'ve combined two breakfast favourites to create these decadent waffle donuts! Fluffy, deep-fried and covered in a powdered sugar glaze.'),(9,'Crookie',2.50,'A croissant filled with crushed cookie pieces and topped with a melted, chocolate cream cookie. The crunchy cookie and pillow-soft croissant dough are a winning combination.'),(10,'Biskie',3.00,'The sandwiched dessert of your dreams is a cross between a cake and a cookie. Two chewy dark chocolate cookies are filled with cream and handmade salted caramel sauce.');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_allergen`
--

DROP TABLE IF EXISTS `product_allergen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_allergen` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `allergen_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `allergen_id` (`allergen_id`),
  CONSTRAINT `product_allergen_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  CONSTRAINT `product_allergen_ibfk_2` FOREIGN KEY (`allergen_id`) REFERENCES `allergen` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_allergen`
--

LOCK TABLES `product_allergen` WRITE;
/*!40000 ALTER TABLE `product_allergen` DISABLE KEYS */;
INSERT INTO `product_allergen` VALUES (1,1,3),(2,1,4),(3,2,2),(4,2,3),(5,2,4),(6,3,2),(7,3,3),(8,3,4),(9,4,2),(10,4,3),(11,4,4),(12,5,2),(13,5,3),(14,5,4),(15,6,1),(16,6,2),(17,6,3),(18,6,4),(19,7,2),(20,7,3),(21,7,4),(22,8,2),(23,8,3),(24,8,4),(25,9,2),(26,9,3),(27,9,4),(28,9,5),(29,10,2),(30,10,3),(31,10,4);
/*!40000 ALTER TABLE `product_allergen` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-16 14:37:50
