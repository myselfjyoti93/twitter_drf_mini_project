-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2021 at 06:49 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `twitter`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add tweet', 8, 'add_tweet'),
(30, 'Can change tweet', 8, 'change_tweet'),
(31, 'Can delete tweet', 8, 'delete_tweet'),
(32, 'Can view tweet', 8, 'view_tweet'),
(33, 'Can add twitter follower', 9, 'add_twitterfollower'),
(34, 'Can change twitter follower', 9, 'change_twitterfollower'),
(35, 'Can delete twitter follower', 9, 'delete_twitterfollower'),
(36, 'Can view twitter follower', 9, 'view_twitterfollower');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(8, 'tweet_api', 'tweet'),
(9, 'tweet_api', 'twitterfollower'),
(7, 'tweet_api', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-04-13 19:35:30.000000'),
(2, 'auth', '0001_initial', '2021-04-13 19:35:30.000000'),
(3, 'admin', '0001_initial', '2021-04-13 19:35:31.000000'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-04-13 19:35:31.000000'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-04-13 19:35:31.000000'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-04-13 19:35:31.000000'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-04-13 19:35:31.000000'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-04-13 19:35:31.000000'),
(9, 'auth', '0004_alter_user_username_opts', '2021-04-13 19:35:31.000000'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-04-13 19:35:31.000000'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-04-13 19:35:31.000000'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-04-13 19:35:31.000000'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-04-13 19:35:31.000000'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-04-13 19:35:31.000000'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-04-13 19:35:31.000000'),
(16, 'auth', '0011_update_proxy_permissions', '2021-04-13 19:35:31.000000'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-04-13 19:35:31.000000'),
(18, 'sessions', '0001_initial', '2021-04-13 19:35:31.000000'),
(19, 'tweet_api', '0001_initial', '2021-04-13 19:39:48.000000'),
(20, 'tweet_api', '0002_auto_20210414_0120', '2021-04-13 19:50:12.000000'),
(21, 'tweet_api', '0003_tweet', '2021-04-13 19:56:11.000000'),
(22, 'tweet_api', '0004_tweet_active_status', '2021-04-13 19:58:25.000000'),
(23, 'tweet_api', '0005_auto_20210414_0132', '2021-04-13 20:02:30.000000'),
(24, 'tweet_api', '0006_twitterfollower', '2021-04-13 20:04:33.000000'),
(25, 'tweet_api', '0007_auto_20210414_0141', '2021-04-13 20:11:21.000000'),
(26, 'tweet_api', '0008_auto_20210414_0143', '2021-04-13 20:13:15.000000');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tweets`
--

CREATE TABLE `tweets` (
  `id` int(11) NOT NULL,
  `tweet_hashtag` varchar(255) DEFAULT NULL,
  `tweet_content` varchar(255) DEFAULT NULL,
  `tweeted_at` datetime(6) DEFAULT NULL,
  `tweeted_by` int(11) NOT NULL,
  `active_status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tweets`
--

INSERT INTO `tweets` (`id`, `tweet_hashtag`, `tweet_content`, `tweeted_at`, `tweeted_by`, `active_status`) VALUES
(1, '#xyz', 'xyz', '2021-04-16 16:38:10.000000', 4, 1),
(2, '#xyz', 'xyzz', '2021-04-16 16:38:20.000000', 4, 1),
(3, '#xyz', 'xyzzz', '2021-04-16 16:38:22.000000', 4, 1),
(4, '#xyz', 'xyzzzz', '2021-04-16 16:39:05.000000', 4, 1),
(5, '#xyz', 'xyzzzzz', '2021-04-16 16:39:07.000000', 4, 1),
(6, '#xyz', 'xyzzzzzz', '2021-04-16 16:39:14.000000', 4, 1),
(7, '#ABC', 'ABC', '2021-04-16 16:39:34.000000', 3, 1),
(8, '#ABC', 'ABC', '2021-04-16 16:39:36.000000', 3, 1),
(9, '#ABCC', 'ABC', '2021-04-16 16:39:41.000000', 3, 1),
(10, '#ABCC', 'ABC', '2021-04-16 16:39:42.000000', 3, 1),
(11, '#ABCC', 'ABC', '2021-04-16 16:39:43.000000', 3, 1),
(12, '#ABCC', 'ABC', '2021-04-16 16:39:43.000000', 3, 1),
(13, '#ABCCCC', 'ABC', '2021-04-16 16:39:47.000000', 3, 1),
(14, '#ABCCCC', 'ABC', '2021-04-16 16:39:47.000000', 3, 1),
(15, '#ABCCCC', 'ABC', '2021-04-16 16:39:48.000000', 3, 1),
(16, '#ABCCC', 'ABC', '2021-04-16 16:39:51.000000', 3, 1),
(17, '#ABCCC', 'ABC', '2021-04-16 16:39:52.000000', 3, 1),
(18, '#CHECK', 'ABC', '2021-04-16 16:47:27.000000', 1, 1),
(19, '#CHECK', 'ABCD', '2021-04-16 16:47:33.000000', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `twitter_follwers`
--

CREATE TABLE `twitter_follwers` (
  `id` int(11) NOT NULL,
  `active_status` int(11) NOT NULL,
  `follower_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `twitter_user`
--

CREATE TABLE `twitter_user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `active_status` int(11) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `created_at` datetime(6),
  `details` varchar(255) DEFAULT NULL,
  `email_id` varchar(255) DEFAULT NULL,
  `updated_date` datetime(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `twitter_user`
--

INSERT INTO `twitter_user` (`id`, `username`, `active_status`, `address`, `age`, `created_at`, `details`, `email_id`, `updated_date`) VALUES
(1, 'user1', 1, NULL, NULL, '2021-04-16 16:33:42.000000', NULL, 'user1@gmail.com', '2021-04-16 16:33:42.000000'),
(2, 'user2', 1, NULL, 19, '2021-04-16 16:36:37.000000', NULL, 'user2@gmail.com', '2021-04-16 16:36:37.000000'),
(3, 'user3', 1, NULL, 19, '2021-04-16 16:36:50.000000', NULL, 'user3@gmail.com', '2021-04-16 16:36:50.000000'),
(4, 'user4', 1, NULL, 19, '2021-04-16 16:36:58.000000', NULL, 'user4@gmail.com', '2021-04-16 16:36:58.000000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tweets`
--
ALTER TABLE `tweets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tweets_tweeted_by_6b916c71_fk_twitter_user_id` (`tweeted_by`);

--
-- Indexes for table `twitter_follwers`
--
ALTER TABLE `twitter_follwers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `twitter_follwers_follower_id_6d154638_fk_twitter_user_id` (`follower_id`),
  ADD KEY `twitter_follwers_user_id_a6263c19_fk_twitter_user_id` (`user_id`);

--
-- Indexes for table `twitter_user`
--
ALTER TABLE `twitter_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `tweets`
--
ALTER TABLE `tweets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `twitter_follwers`
--
ALTER TABLE `twitter_follwers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `twitter_user`
--
ALTER TABLE `twitter_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tweets`
--
ALTER TABLE `tweets`
  ADD CONSTRAINT `tweets_tweeted_by_6b916c71_fk_twitter_user_id` FOREIGN KEY (`tweeted_by`) REFERENCES `twitter_user` (`id`);

--
-- Constraints for table `twitter_follwers`
--
ALTER TABLE `twitter_follwers`
  ADD CONSTRAINT `twitter_follwers_follower_id_6d154638_fk_twitter_user_id` FOREIGN KEY (`follower_id`) REFERENCES `twitter_user` (`id`),
  ADD CONSTRAINT `twitter_follwers_user_id_a6263c19_fk_twitter_user_id` FOREIGN KEY (`user_id`) REFERENCES `twitter_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
