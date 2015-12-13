-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 05 Lis 2015, 22:15
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `xml6`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `article`
--

CREATE TABLE IF NOT EXISTS `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `title` text NOT NULL,
  `featured` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Zrzut danych tabeli `article`
--

INSERT INTO `article` (`id`, `content`, `title`, `featured`) VALUES
(1, 'zawartosc artykulu nr 1 ...', 'Artykul 1', 1),
(2, 'zawartosc artykulu nr 2 ...', 'Artykul 2 ', 0),
(3, 'zawartosc artykulu nr 3 ...', 'Artykul 3', 1),
(4, 'zawartosc artykulu nr 4 ...', 'Artykul 4 ', 0),
(5, 'zawartosc artykulu nr 5 ...', 'Artykul 5', 1),
(6, 'zawartosc artykulu nr 6 ...', 'Artykul 6 ', 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `footer`
--

CREATE TABLE IF NOT EXISTS `footer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `type` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Zrzut danych tabeli `footer`
--

INSERT INTO `footer` (`id`, `title`, `type`) VALUES
(1, 'Autor', 'main'),
(2, 'Prawa', 'main');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `menu`
--

CREATE TABLE IF NOT EXISTS `menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link` text NOT NULL,
  `label` text NOT NULL,
  `type` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Zrzut danych tabeli `menu`
--

INSERT INTO `menu` (`id`, `link`, `label`, `type`) VALUES
(1, 'http://wp.pl', 'Wirtualna Polska', 'mainmenu'),
(2, 'http://onet.pl', 'Onet', 'mainmenu'),
(3, 'http://interia.pl', 'Interia', 'mainmenu'),
(4, 'http://facebook.pl', 'Facebook', 'othermenu');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `title`
--

CREATE TABLE IF NOT EXISTS `title` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page` text NOT NULL,
  `title` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Zrzut danych tabeli `title`
--

INSERT INTO `title` (`id`, `page`, `title`) VALUES
(1, 'main', 'Strona Glowna');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
