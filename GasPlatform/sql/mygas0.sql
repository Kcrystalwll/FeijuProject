/*
Navicat MySQL Data Transfer

Source Server         : mm
Source Server Version : 50625
Source Host           : localhost:3306
Source Database       : mygas0

Target Server Type    : MYSQL
Target Server Version : 50625
File Encoding         : 65001

Date: 2019-06-17 14:33:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 生产厂商', '7', 'add_manufacture');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 生产厂商', '7', 'change_manufacture');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 生产厂商', '7', 'delete_manufacture');
INSERT INTO `auth_permission` VALUES ('22', 'Can add g s_ meter type info', '8', 'add_gs_metertypeinfo');
INSERT INTO `auth_permission` VALUES ('23', 'Can change g s_ meter type info', '8', 'change_gs_metertypeinfo');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete g s_ meter type info', '8', 'delete_gs_metertypeinfo');
INSERT INTO `auth_permission` VALUES ('25', 'Can add g s_ meter info_ic', '9', 'add_gs_meterinfo_ic');
INSERT INTO `auth_permission` VALUES ('26', 'Can change g s_ meter info_ic', '9', 'change_gs_meterinfo_ic');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete g s_ meter info_ic', '9', 'delete_gs_meterinfo_ic');
INSERT INTO `auth_permission` VALUES ('28', 'Can add g s_ meter info_msb', '10', 'add_gs_meterinfo_msb');
INSERT INTO `auth_permission` VALUES ('29', 'Can change g s_ meter info_msb', '10', 'change_gs_meterinfo_msb');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete g s_ meter info_msb', '10', 'delete_gs_meterinfo_msb');
INSERT INTO `auth_permission` VALUES ('31', 'Can add g s_ meter info_xzy', '11', 'add_gs_meterinfo_xzy');
INSERT INTO `auth_permission` VALUES ('32', 'Can change g s_ meter info_xzy', '11', 'change_gs_meterinfo_xzy');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete g s_ meter info_xzy', '11', 'delete_gs_meterinfo_xzy');
INSERT INTO `auth_permission` VALUES ('34', 'Can add g s_ meter info_csb', '12', 'add_gs_meterinfo_csb');
INSERT INTO `auth_permission` VALUES ('35', 'Can change g s_ meter info_csb', '12', 'change_gs_meterinfo_csb');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete g s_ meter info_csb', '12', 'delete_gs_meterinfo_csb');
INSERT INTO `auth_permission` VALUES ('37', 'Can add meter_ test', '13', 'add_meter_test');
INSERT INTO `auth_permission` VALUES ('38', 'Can change meter_ test', '13', 'change_meter_test');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete meter_ test', '13', 'delete_meter_test');
INSERT INTO `auth_permission` VALUES ('40', 'Can add meter_ result', '14', 'add_meter_result');
INSERT INTO `auth_permission` VALUES ('41', 'Can change meter_ result', '14', 'change_meter_result');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete meter_ result', '14', 'delete_meter_result');
INSERT INTO `auth_permission` VALUES ('43', 'Can add meter_ result_ record', '15', 'add_meter_result_record');
INSERT INTO `auth_permission` VALUES ('44', 'Can change meter_ result_ record', '15', 'change_meter_result_record');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete meter_ result_ record', '15', 'delete_meter_result_record');
INSERT INTO `auth_permission` VALUES ('46', 'Can add plan info', '16', 'add_planinfo');
INSERT INTO `auth_permission` VALUES ('47', 'Can change plan info', '16', 'change_planinfo');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete plan info', '16', 'delete_planinfo');
INSERT INTO `auth_permission` VALUES ('49', 'Can add meter plat', '17', 'add_meterplat');
INSERT INTO `auth_permission` VALUES ('50', 'Can change meter plat', '17', 'change_meterplat');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete meter plat', '17', 'delete_meterplat');
INSERT INTO `auth_permission` VALUES ('52', 'Can add 菜单表', '18', 'add_menu');
INSERT INTO `auth_permission` VALUES ('53', 'Can change 菜单表', '18', 'change_menu');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete 菜单表', '18', 'delete_menu');
INSERT INTO `auth_permission` VALUES ('55', 'Can add 权限表', '19', 'add_permission_info');
INSERT INTO `auth_permission` VALUES ('56', 'Can change 权限表', '19', 'change_permission_info');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete 权限表', '19', 'delete_permission_info');
INSERT INTO `auth_permission` VALUES ('58', 'Can add 分组表', '20', 'add_group_info');
INSERT INTO `auth_permission` VALUES ('59', 'Can change 分组表', '20', 'change_group_info');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete 分组表', '20', 'delete_group_info');
INSERT INTO `auth_permission` VALUES ('61', 'Can add 用户表', '21', 'add_user_info');
INSERT INTO `auth_permission` VALUES ('62', 'Can change 用户表', '21', 'change_user_info');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete 用户表', '21', 'delete_user_info');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$24000$upqywXTEQVfw$GzRcjBvn3cRSfBAXMe6lcZ+8O3JHb6T6INMxtbeEBNM=', '2019-06-08 14:09:38.175804', '1', 'shu', '', '', 'shu@123.com', '1', '1', '2019-05-29 21:53:50.408834');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
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
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-05-29 21:55:16.373363', '1', '生产厂商', '2', '已修改 permission 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-05-29 21:55:30.737991', '2', '测试人员-管理员', '2', '已修改 permission 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2019-05-29 21:55:41.285667', '3', '测试人员-操作员', '2', '已修改 permission 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2019-05-29 21:55:46.894150', '4', '超级管理员', '2', '没有字段被修改。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2019-06-08 14:10:17.748883', '57', '导出excel', '1', '已添加。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2019-06-08 14:43:09.509642', '4', '超级管理员', '2', '已修改 permission 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2019-06-10 08:26:27.132324', '58', '重置密码', '1', '已添加。', '19', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2019-06-10 08:26:36.871217', '4', '超级管理员', '2', '已修改 permission 。', '20', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2019-06-10 08:26:52.141402', '2', '测试人员-管理员', '2', '已修改 permission 。', '20', '1');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('12', 'mygas', 'gs_meterinfo_csb');
INSERT INTO `django_content_type` VALUES ('9', 'mygas', 'gs_meterinfo_ic');
INSERT INTO `django_content_type` VALUES ('10', 'mygas', 'gs_meterinfo_msb');
INSERT INTO `django_content_type` VALUES ('11', 'mygas', 'gs_meterinfo_xzy');
INSERT INTO `django_content_type` VALUES ('8', 'mygas', 'gs_metertypeinfo');
INSERT INTO `django_content_type` VALUES ('7', 'mygas', 'manufacture');
INSERT INTO `django_content_type` VALUES ('17', 'mygas', 'meterplat');
INSERT INTO `django_content_type` VALUES ('14', 'mygas', 'meter_result');
INSERT INTO `django_content_type` VALUES ('15', 'mygas', 'meter_result_record');
INSERT INTO `django_content_type` VALUES ('13', 'mygas', 'meter_test');
INSERT INTO `django_content_type` VALUES ('16', 'mygas', 'planinfo');
INSERT INTO `django_content_type` VALUES ('20', 'rbac', 'group_info');
INSERT INTO `django_content_type` VALUES ('18', 'rbac', 'menu');
INSERT INTO `django_content_type` VALUES ('19', 'rbac', 'permission_info');
INSERT INTO `django_content_type` VALUES ('21', 'rbac', 'user_info');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-05-29 18:03:37.376029');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-05-29 18:03:43.752631');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-05-29 18:03:45.641625');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-05-29 18:03:45.721604');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2019-05-29 18:03:46.591277');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2019-05-29 18:03:47.090896');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2019-05-29 18:03:47.730504');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2019-05-29 18:03:47.750530');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2019-05-29 18:03:48.100348');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2019-05-29 18:03:48.120346');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2019-05-29 18:03:48.160276');
INSERT INTO `django_migrations` VALUES ('12', 'rbac', '0001_initial', '2019-05-29 18:03:52.757063');
INSERT INTO `django_migrations` VALUES ('13', 'mygas', '0001_initial', '2019-05-29 18:04:02.162054');
INSERT INTO `django_migrations` VALUES ('14', 'mygas', '0002_auto_20190529_1803', '2019-05-29 18:04:05.840038');
INSERT INTO `django_migrations` VALUES ('15', 'rbac', '0002_auto_20190529_1803', '2019-05-29 18:04:07.629136');
INSERT INTO `django_migrations` VALUES ('16', 'sessions', '0001_initial', '2019-05-29 18:04:08.248816');
INSERT INTO `django_migrations` VALUES ('17', 'rbac', '0003_auto_20190529_1804', '2019-05-29 18:04:36.765646');
INSERT INTO `django_migrations` VALUES ('18', 'mygas', '0003_auto_20190529_1804', '2019-05-29 18:04:45.580982');
INSERT INTO `django_migrations` VALUES ('19', 'mygas', '0004_gs_metertypeinfo_check_user', '2019-06-09 18:51:51.137841');
INSERT INTO `django_migrations` VALUES ('20', 'mygas', '0005_gs_metertypeinfo_allo_user', '2019-06-09 19:12:45.447200');
INSERT INTO `django_migrations` VALUES ('21', 'mygas', '0006_auto_20190615_1421', '2019-06-15 14:21:17.314749');
INSERT INTO `django_migrations` VALUES ('22', 'mygas', '0007_gs_metertypeinfo_meterprivilege', '2019-06-17 12:37:43.058405');
INSERT INTO `django_migrations` VALUES ('23', 'mygas', '0008_auto_20190616_2014', '2019-06-17 12:37:52.289233');
INSERT INTO `django_migrations` VALUES ('24', 'mygas', '0009_gs_metertypeinfo_istest', '2019-06-17 12:37:52.898727');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('7ts68r7cs968hnaau25mc0ccibwkzmnq', 'ODkwNjQyZTFhYTdiYmQwYjJjMWVhY2NkYTJjNTVmNTA3ZGJkN2QwYzp7InBlcm1pc3Npb24iOlt7InVybCI6Ii9kYXRhLyJ9LHsidXJsIjoiL2RhdGFyZXN1bHQvIn0seyJ1cmwiOiIvbWlkZGxlX3Jlc3VsdC8ifSx7InVybCI6Ii9yZXN1bHQvIn0seyJ1cmwiOiIvc3VibWl0LyJ9LHsidXJsIjoiL2RhdGFpbnB1dC8ifSx7InVybCI6Ii9kYXRhaW5wdXRfaWNfbXNiLyJ9LHsidXJsIjoiL2RhdGFpbnB1dF9pY194enkvIn0seyJ1cmwiOiIvZGF0YWlucHV0X2ljX2NzYi8ifSx7InVybCI6Ii9kYXRhaW5wdXRfbXNiLyJ9LHsidXJsIjoiL2RhdGFpbnB1dF94enkvIn0seyJ1cmwiOiIvZGF0YWlucHV0X2NzYi8ifSx7InVybCI6Ii9kZWxfZGF0YS8ifSx7InVybCI6Ii9lZGl0X2RhdGEvIn0seyJ1cmwiOiIvZWRpdF9pY19tc2IvIn0seyJ1cmwiOiIvZWRpdF9pY194enkvIn0seyJ1cmwiOiIvZWRpdF9pY19jc2IvIn0seyJ1cmwiOiIvZWRpdF9tc2IvIn0seyJ1cmwiOiIvZWRpdF94enkvIn0seyJ1cmwiOiIvZWRpdF9jc2IvIn0seyJ1cmwiOiIvY2hlY2tfZGF0YS8ifSx7InVybCI6Ii9jaGVja19pY19tc2IvIn0seyJ1cmwiOiIvY2hlY2tfaWNfeHp5LyJ9LHsidXJsIjoiL2NoZWNrX2ljX2NzYi8ifSx7InVybCI6Ii9jaGVja19tc2IvIn0seyJ1cmwiOiIvY2hlY2tfeHp5LyJ9LHsidXJsIjoiL2NoZWNrX2NzYi8ifSx7InVybCI6Ii91c2VyLyJ9LHsidXJsIjoiL2luZGV4LyJ9XSwibWVudSI6eyIxIjp7Im1lbnVfbmFtZSI6Ilx1NjU3MFx1NjM2ZVx1NWY1NVx1NTE2NSIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QtYWx0Iiwid2VpZ2h0Ijo1LCJjaGlsZHJlbiI6W3sibWVudV9uYW1lIjoiXHU3ZjE2XHU4ZjkxXHU2NTcwXHU2MzZlIiwidXJsIjoiL2RhdGEvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tcGVuY2lsIn0seyJtZW51X25hbWUiOiJcdTViYTFcdTY4MzhcdTYwYzVcdTUxYjUiLCJ1cmwiOiIvZGF0YXJlc3VsdC8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1saXN0In1dfSwiNCI6eyJtZW51X25hbWUiOiJcdTdlZDNcdTY3OWNcdTY3ZTVcdThiZTIiLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1mb2xkZXItb3BlbiIsIndlaWdodCI6MiwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NmQ0Ylx1OGJkNVx1OGZkYlx1NWVhNiIsInVybCI6Ii9taWRkbGVfcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXRhc2tzIn0seyJtZW51X25hbWUiOiJcdTZkNGJcdThiZDVcdTdlZDNcdTY3OWMiLCJ1cmwiOiIvcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QifV19fSwidXNlciI6Im1hbnUwMSIsIk1ldGVySWQiOiIyMDE5MDQxMDAxMTEiLCJNZXRlclR5cGUiOiJcdTgxOWNcdTVmMGZcdTg4NjgiLCJNYW51ZmFjdHVyZU5hbWVfaWQiOjEsIlRpbWVPZlByb2R1Y2UiOiIyMDE5LTAyLTA0In0=', '2019-06-22 16:24:33.171181');
INSERT INTO `django_session` VALUES ('8ltczq2t72rofaduinzjwbsvt5fklqpz', 'MWEzZTJmZTVhZGRkMThhNzM0NDQ3ZTBjMGRkZWZkYTAxMjEyMDk5NDp7InBlcm1pc3Npb24iOlt7InVybCI6Ii9kYXRhLyJ9LHsidXJsIjoiL2RhdGFyZXN1bHQvIn0seyJ1cmwiOiIvbWlkZGxlX3Jlc3VsdC8ifSx7InVybCI6Ii9yZXN1bHQvIn0seyJ1cmwiOiIvc3VibWl0LyJ9LHsidXJsIjoiL2RhdGFpbnB1dC8ifSx7InVybCI6Ii9kYXRhaW5wdXRfaWNfbXNiLyJ9LHsidXJsIjoiL2RhdGFpbnB1dF9pY194enkvIn0seyJ1cmwiOiIvZGF0YWlucHV0X2ljX2NzYi8ifSx7InVybCI6Ii9kYXRhaW5wdXRfbXNiLyJ9LHsidXJsIjoiL2RhdGFpbnB1dF94enkvIn0seyJ1cmwiOiIvZGF0YWlucHV0X2NzYi8ifSx7InVybCI6Ii9kZWxfZGF0YS8ifSx7InVybCI6Ii9lZGl0X2RhdGEvIn0seyJ1cmwiOiIvZWRpdF9pY19tc2IvIn0seyJ1cmwiOiIvZWRpdF9pY194enkvIn0seyJ1cmwiOiIvZWRpdF9pY19jc2IvIn0seyJ1cmwiOiIvZWRpdF9tc2IvIn0seyJ1cmwiOiIvZWRpdF94enkvIn0seyJ1cmwiOiIvZWRpdF9jc2IvIn0seyJ1cmwiOiIvY2hlY2tfZGF0YS8ifSx7InVybCI6Ii9jaGVja19pY19tc2IvIn0seyJ1cmwiOiIvY2hlY2tfaWNfeHp5LyJ9LHsidXJsIjoiL2NoZWNrX2ljX2NzYi8ifSx7InVybCI6Ii9jaGVja19tc2IvIn0seyJ1cmwiOiIvY2hlY2tfeHp5LyJ9LHsidXJsIjoiL2NoZWNrX2NzYi8ifSx7InVybCI6Ii91c2VyLyJ9LHsidXJsIjoiL2luZGV4LyJ9XSwibWVudSI6eyIxIjp7Im1lbnVfbmFtZSI6Ilx1NjU3MFx1NjM2ZVx1NWY1NVx1NTE2NSIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QtYWx0Iiwid2VpZ2h0Ijo1LCJjaGlsZHJlbiI6W3sibWVudV9uYW1lIjoiXHU3ZjE2XHU4ZjkxXHU2NTcwXHU2MzZlIiwidXJsIjoiL2RhdGEvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tcGVuY2lsIn0seyJtZW51X25hbWUiOiJcdTViYTFcdTY4MzhcdTYwYzVcdTUxYjUiLCJ1cmwiOiIvZGF0YXJlc3VsdC8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1saXN0In1dfSwiNCI6eyJtZW51X25hbWUiOiJcdTdlZDNcdTY3OWNcdTY3ZTVcdThiZTIiLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1mb2xkZXItb3BlbiIsIndlaWdodCI6MiwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NmQ0Ylx1OGJkNVx1OGZkYlx1NWVhNiIsInVybCI6Ii9taWRkbGVfcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXRhc2tzIn0seyJtZW51X25hbWUiOiJcdTZkNGJcdThiZDVcdTdlZDNcdTY3OWMiLCJ1cmwiOiIvcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QifV19fSwidXNlciI6Im1hbnUwMSJ9', '2019-07-01 13:30:48.256364');
INSERT INTO `django_session` VALUES ('ck6tyk9bayxxmeoljt8zh7k0hl40odi5', 'MzgwZjNmN2QwY2M2YWIxNTEzNGQxNzJjNTJjYWI2ZGQ2NmJiM2I1Zjp7InBlcm1pc3Npb24iOlt7InVybCI6Ii9kYXRhLyJ9LHsidXJsIjoiL2RhdGFyZXN1bHQvIn0seyJ1cmwiOiIvZGF0YWNoZWNrLyJ9LHsidXJsIjoiL2NoZWNrcmVzdWx0LyJ9LHsidXJsIjoiL2FsbG9jYXRpb24vIn0seyJ1cmwiOiIvYWxsb19yZXN1bHQvIn0seyJ1cmwiOiIvbWlkZGxlX3Jlc3VsdC8ifSx7InVybCI6Ii9yZXN1bHQvIn0seyJ1cmwiOiIvZ3JvdXAvIn0seyJ1cmwiOiIvbWFudWxpc3QvIn0seyJ1cmwiOiIvc3VibWl0LyJ9LHsidXJsIjoiL2RhdGFpbnB1dC8ifSx7InVybCI6Ii9kYXRhaW5wdXRfaWNfbXNiLyJ9LHsidXJsIjoiL2RhdGFpbnB1dF9pY194enkvIn0seyJ1cmwiOiIvZGF0YWlucHV0X2ljX2NzYi8ifSx7InVybCI6Ii9kYXRhaW5wdXRfbXNiLyJ9LHsidXJsIjoiL2RhdGFpbnB1dF94enkvIn0seyJ1cmwiOiIvZGF0YWlucHV0X2NzYi8ifSx7InVybCI6Ii9kZWxfZGF0YS8ifSx7InVybCI6Ii9lZGl0X2RhdGEvIn0seyJ1cmwiOiIvZWRpdF9pY19tc2IvIn0seyJ1cmwiOiIvZWRpdF9pY194enkvIn0seyJ1cmwiOiIvZWRpdF9pY19jc2IvIn0seyJ1cmwiOiIvZWRpdF9tc2IvIn0seyJ1cmwiOiIvZWRpdF94enkvIn0seyJ1cmwiOiIvZWRpdF9jc2IvIn0seyJ1cmwiOiIvY2hlY2tfZGF0YS8ifSx7InVybCI6Ii9jaGVja19pY19tc2IvIn0seyJ1cmwiOiIvY2hlY2tfaWNfeHp5LyJ9LHsidXJsIjoiL2NoZWNrX2ljX2NzYi8ifSx7InVybCI6Ii9jaGVja19tc2IvIn0seyJ1cmwiOiIvY2hlY2tfeHp5LyJ9LHsidXJsIjoiL2NoZWNrX2NzYi8ifSx7InVybCI6Ii9jaGVjay8ifSx7InVybCI6Ii9zdWJfYWxsb2NhdGlvbi8ifSx7InVybCI6Ii9ncm91cF9hZGQvIn0seyJ1cmwiOiIvZ3JvdXBfZWRpdC8ifSx7InVybCI6Ii9ncm91cF9kZWwvIn0seyJ1cmwiOiIvbWFudWxpc3RfYWRkLyJ9LHsidXJsIjoiL21hbnVsaXN0X2VkaXQvIn0seyJ1cmwiOiIvbWFudWxpc3RfZGVsLyJ9LHsidXJsIjoiL3Blcm1pc3Npb25saXN0X2FkZC8ifSx7InVybCI6Ii9wZXJtaXNzaW9ubGlzdF9kZWwvIn0seyJ1cmwiOiIvcGVybWlzc2lvbmxpc3RfZWRpdC8ifSx7InVybCI6Ii91c2VyLyJ9LHsidXJsIjoiL2luZGV4LyJ9LHsidXJsIjoiL2xvZ2ludXNlcl9hZGQvIn0seyJ1cmwiOiIvbG9naW51c2VyX2VkaXQvIn0seyJ1cmwiOiIvbG9naW51c2VyX2RlbC8ifSx7InVybCI6Ii9zdG9yYWdlLyJ9LHsidXJsIjoiL2RlbF90ZXN0LyJ9LHsidXJsIjoiL2JhY2svIn0seyJ1cmwiOiIvYWdhaW5fdGVzdC8ifV0sIm1lbnUiOnsiMSI6eyJtZW51X25hbWUiOiJcdTY1NzBcdTYzNmVcdTVmNTVcdTUxNjUiLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1saXN0LWFsdCIsIndlaWdodCI6NSwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1N2YxNlx1OGY5MVx1NjU3MFx1NjM2ZSIsInVybCI6Ii9kYXRhLyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXBlbmNpbCJ9LHsibWVudV9uYW1lIjoiXHU1YmExXHU2ODM4XHU2MGM1XHU1MWI1IiwidXJsIjoiL2RhdGFyZXN1bHQvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tbGlzdCJ9XX0sIjIiOnsibWVudV9uYW1lIjoiXHU2NTcwXHU2MzZlXHU1YmExXHU2ODM4IiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tc2VhcmNoIiwid2VpZ2h0Ijo0LCJjaGlsZHJlbiI6W3sibWVudV9uYW1lIjoiXHU1YmExXHU2ODM4XHU2NTcwXHU2MzZlIiwidXJsIjoiL2RhdGFjaGVjay8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1zZWFyY2gifSx7Im1lbnVfbmFtZSI6Ilx1NWJhMVx1NjgzOFx1N2VkM1x1Njc5YyIsInVybCI6Ii9jaGVja3Jlc3VsdC8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1saXN0In1dfSwiMyI6eyJtZW51X25hbWUiOiJcdTZkNGJcdThiZDVcdTUyMDZcdTkxNGQiLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1yZXR3ZWV0Iiwid2VpZ2h0IjozLCJjaGlsZHJlbiI6W3sibWVudV9uYW1lIjoiXHU1MjA2XHU5MTRkXHU2ZDRiXHU4YmQ1IiwidXJsIjoiL2FsbG9jYXRpb24vIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tcmV0d2VldCJ9LHsibWVudV9uYW1lIjoiXHU1MjA2XHU5MTRkXHU3ZWQzXHU2NzljIiwidXJsIjoiL2FsbG9fcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QifV19LCI0Ijp7Im1lbnVfbmFtZSI6Ilx1N2VkM1x1Njc5Y1x1NjdlNVx1OGJlMiIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWZvbGRlci1vcGVuIiwid2VpZ2h0IjoyLCJjaGlsZHJlbiI6W3sibWVudV9uYW1lIjoiXHU2ZDRiXHU4YmQ1XHU4ZmRiXHU1ZWE2IiwidXJsIjoiL21pZGRsZV9yZXN1bHQvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tdGFza3MifSx7Im1lbnVfbmFtZSI6Ilx1NmQ0Ylx1OGJkNVx1N2VkM1x1Njc5YyIsInVybCI6Ii9yZXN1bHQvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tbGlzdCJ9XX0sIjUiOnsibWVudV9uYW1lIjoiXHU3NTI4XHU2MjM3XHU3YmExXHU3NDA2IiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tdXNlciIsIndlaWdodCI6MSwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NTIwNlx1N2VjNFx1N2JhMVx1NzQwNiIsInVybCI6Ii9ncm91cC8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1jb2cifSx7Im1lbnVfbmFtZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiIsInVybCI6Ii9tYW51bGlzdC8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1jb2cifV19fSwidXNlciI6IndsbCJ9', '2019-06-22 14:09:19.679417');
INSERT INTO `django_session` VALUES ('l3fzyu90bn5o05vohwg9rqnom0eqv496', 'Mzk5MWYxYzYwYzA1M2NjZTFmYzkzODJjOWUyZWU2MDMwNDg0NWI3YTp7InBlcm1pc3Npb24iOlt7InVybCI6Ii9kYXRhY2hlY2svIn0seyJ1cmwiOiIvY2hlY2tyZXN1bHQvIn0seyJ1cmwiOiIvYWxsb2NhdGlvbi8ifSx7InVybCI6Ii9hbGxvX3Jlc3VsdC8ifSx7InVybCI6Ii9taWRkbGVfcmVzdWx0LyJ9LHsidXJsIjoiL3Jlc3VsdC8ifSx7InVybCI6Ii9ncm91cC8ifSx7InVybCI6Ii9tYW51bGlzdC8ifSx7InVybCI6Ii9jaGVja19kYXRhLyJ9LHsidXJsIjoiL2NoZWNrX2ljX21zYi8ifSx7InVybCI6Ii9jaGVja19pY194enkvIn0seyJ1cmwiOiIvY2hlY2tfaWNfY3NiLyJ9LHsidXJsIjoiL2NoZWNrX21zYi8ifSx7InVybCI6Ii9jaGVja194enkvIn0seyJ1cmwiOiIvY2hlY2tfY3NiLyJ9LHsidXJsIjoiL2NoZWNrLyJ9LHsidXJsIjoiL3N1Yl9hbGxvY2F0aW9uLyJ9LHsidXJsIjoiL2dyb3VwX2FkZC8ifSx7InVybCI6Ii9ncm91cF9lZGl0LyJ9LHsidXJsIjoiL2dyb3VwX2RlbC8ifSx7InVybCI6Ii9tYW51bGlzdF9hZGQvIn0seyJ1cmwiOiIvbWFudWxpc3RfZWRpdC8ifSx7InVybCI6Ii9tYW51bGlzdF9kZWwvIn0seyJ1cmwiOiIvcGVybWlzc2lvbmxpc3RfYWRkLyJ9LHsidXJsIjoiL3Blcm1pc3Npb25saXN0X2RlbC8ifSx7InVybCI6Ii9wZXJtaXNzaW9ubGlzdF9lZGl0LyJ9LHsidXJsIjoiL3VzZXIvIn0seyJ1cmwiOiIvaW5kZXgvIn0seyJ1cmwiOiIvbG9naW51c2VyX2FkZC8ifSx7InVybCI6Ii9sb2dpbnVzZXJfZWRpdC8ifSx7InVybCI6Ii9sb2dpbnVzZXJfZGVsLyJ9LHsidXJsIjoiL3N0b3JhZ2UvIn0seyJ1cmwiOiIvZGVsX3Rlc3QvIn0seyJ1cmwiOiIvYmFjay8ifSx7InVybCI6Ii9leHBvcnRfZXhjZWwvIn0seyJ1cmwiOiIvcHdkX3Jlc2V0LyJ9XSwibWVudSI6eyIyIjp7Im1lbnVfbmFtZSI6Ilx1NjU3MFx1NjM2ZVx1NWJhMVx1NjgzOCIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXNlYXJjaCIsIndlaWdodCI6NCwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NWJhMVx1NjgzOFx1NjU3MFx1NjM2ZSIsInVybCI6Ii9kYXRhY2hlY2svIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tc2VhcmNoIn0seyJtZW51X25hbWUiOiJcdTViYTFcdTY4MzhcdTdlZDNcdTY3OWMiLCJ1cmwiOiIvY2hlY2tyZXN1bHQvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tbGlzdCJ9XX0sIjMiOnsibWVudV9uYW1lIjoiXHU2ZDRiXHU4YmQ1XHU1MjA2XHU5MTRkIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tcmV0d2VldCIsIndlaWdodCI6MywiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NTIwNlx1OTE0ZFx1NmQ0Ylx1OGJkNSIsInVybCI6Ii9hbGxvY2F0aW9uLyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXJldHdlZXQifSx7Im1lbnVfbmFtZSI6Ilx1NTIwNlx1OTE0ZFx1N2VkM1x1Njc5YyIsInVybCI6Ii9hbGxvX3Jlc3VsdC8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1saXN0In1dfSwiNCI6eyJtZW51X25hbWUiOiJcdTdlZDNcdTY3OWNcdTY3ZTVcdThiZTIiLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1mb2xkZXItb3BlbiIsIndlaWdodCI6MiwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NmQ0Ylx1OGJkNVx1OGZkYlx1NWVhNiIsInVybCI6Ii9taWRkbGVfcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXRhc2tzIn0seyJtZW51X25hbWUiOiJcdTZkNGJcdThiZDVcdTdlZDNcdTY3OWMiLCJ1cmwiOiIvcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QifV19LCI1Ijp7Im1lbnVfbmFtZSI6Ilx1NzUyOFx1NjIzN1x1N2JhMVx1NzQwNiIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXVzZXIiLCJ3ZWlnaHQiOjEsImNoaWxkcmVuIjpbeyJtZW51X25hbWUiOiJcdTUyMDZcdTdlYzRcdTdiYTFcdTc0MDYiLCJ1cmwiOiIvZ3JvdXAvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tY29nIn0seyJtZW51X25hbWUiOiJcdTY3NDNcdTk2NTBcdTdiYTFcdTc0MDYiLCJ1cmwiOiIvbWFudWxpc3QvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tY29nIn1dfX0sInVzZXIiOiJ0ZXN0bWFuYWdlciIsIk1ldGVySWQiOiIwMDIwMTkwNjE2MDIiLCJNZXRlclR5cGUiOiJcdTgxOWNcdTVmMGZcdTg4NjgiLCJNYW51ZmFjdHVyZU5hbWVfaWQiOjEsIlRpbWVPZlByb2R1Y2UiOiIyMDE5LTA2LTE2IiwibG9vazEiOm51bGwsImxvb2syIjoibG9vayJ9', '2019-07-01 13:17:03.693327');
INSERT INTO `django_session` VALUES ('s9dahrox6nfuww1zzzp4116ypai3iup3', 'NGU4MWVmMWM5YzllNTlmNmQwMDcwMTFmMDFjMWE4M2Y0YWIzZjVjODp7InBlcm1pc3Npb24iOlt7InVybCI6Ii9kYXRhY2hlY2svIn0seyJ1cmwiOiIvY2hlY2tyZXN1bHQvIn0seyJ1cmwiOiIvYWxsb2NhdGlvbi8ifSx7InVybCI6Ii9hbGxvX3Jlc3VsdC8ifSx7InVybCI6Ii9taWRkbGVfcmVzdWx0LyJ9LHsidXJsIjoiL3Jlc3VsdC8ifSx7InVybCI6Ii9ncm91cC8ifSx7InVybCI6Ii9tYW51bGlzdC8ifSx7InVybCI6Ii9jaGVja19kYXRhLyJ9LHsidXJsIjoiL2NoZWNrX2ljX21zYi8ifSx7InVybCI6Ii9jaGVja19pY194enkvIn0seyJ1cmwiOiIvY2hlY2tfaWNfY3NiLyJ9LHsidXJsIjoiL2NoZWNrX21zYi8ifSx7InVybCI6Ii9jaGVja194enkvIn0seyJ1cmwiOiIvY2hlY2tfY3NiLyJ9LHsidXJsIjoiL2NoZWNrLyJ9LHsidXJsIjoiL3N1Yl9hbGxvY2F0aW9uLyJ9LHsidXJsIjoiL2dyb3VwX2FkZC8ifSx7InVybCI6Ii9ncm91cF9lZGl0LyJ9LHsidXJsIjoiL2dyb3VwX2RlbC8ifSx7InVybCI6Ii9tYW51bGlzdF9hZGQvIn0seyJ1cmwiOiIvbWFudWxpc3RfZWRpdC8ifSx7InVybCI6Ii9tYW51bGlzdF9kZWwvIn0seyJ1cmwiOiIvcGVybWlzc2lvbmxpc3RfYWRkLyJ9LHsidXJsIjoiL3Blcm1pc3Npb25saXN0X2RlbC8ifSx7InVybCI6Ii9wZXJtaXNzaW9ubGlzdF9lZGl0LyJ9LHsidXJsIjoiL3VzZXIvIn0seyJ1cmwiOiIvaW5kZXgvIn0seyJ1cmwiOiIvbG9naW51c2VyX2FkZC8ifSx7InVybCI6Ii9sb2dpbnVzZXJfZWRpdC8ifSx7InVybCI6Ii9sb2dpbnVzZXJfZGVsLyJ9LHsidXJsIjoiL3N0b3JhZ2UvIn0seyJ1cmwiOiIvZGVsX3Rlc3QvIn0seyJ1cmwiOiIvYmFjay8ifSx7InVybCI6Ii9leHBvcnRfZXhjZWwvIn0seyJ1cmwiOiIvcHdkX3Jlc2V0LyJ9XSwibWVudSI6eyIyIjp7Im1lbnVfbmFtZSI6Ilx1NjU3MFx1NjM2ZVx1NWJhMVx1NjgzOCIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXNlYXJjaCIsIndlaWdodCI6NCwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NWJhMVx1NjgzOFx1NjU3MFx1NjM2ZSIsInVybCI6Ii9kYXRhY2hlY2svIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tc2VhcmNoIn0seyJtZW51X25hbWUiOiJcdTViYTFcdTY4MzhcdTdlZDNcdTY3OWMiLCJ1cmwiOiIvY2hlY2tyZXN1bHQvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tbGlzdCJ9XX0sIjMiOnsibWVudV9uYW1lIjoiXHU2ZDRiXHU4YmQ1XHU1MjA2XHU5MTRkIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tcmV0d2VldCIsIndlaWdodCI6MywiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NTIwNlx1OTE0ZFx1NmQ0Ylx1OGJkNSIsInVybCI6Ii9hbGxvY2F0aW9uLyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXJldHdlZXQifSx7Im1lbnVfbmFtZSI6Ilx1NTIwNlx1OTE0ZFx1N2VkM1x1Njc5YyIsInVybCI6Ii9hbGxvX3Jlc3VsdC8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1saXN0In1dfSwiNCI6eyJtZW51X25hbWUiOiJcdTdlZDNcdTY3OWNcdTY3ZTVcdThiZTIiLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1mb2xkZXItb3BlbiIsIndlaWdodCI6MiwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NmQ0Ylx1OGJkNVx1OGZkYlx1NWVhNiIsInVybCI6Ii9taWRkbGVfcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXRhc2tzIn0seyJtZW51X25hbWUiOiJcdTZkNGJcdThiZDVcdTdlZDNcdTY3OWMiLCJ1cmwiOiIvcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QifV19LCI1Ijp7Im1lbnVfbmFtZSI6Ilx1NzUyOFx1NjIzN1x1N2JhMVx1NzQwNiIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXVzZXIiLCJ3ZWlnaHQiOjEsImNoaWxkcmVuIjpbeyJtZW51X25hbWUiOiJcdTUyMDZcdTdlYzRcdTdiYTFcdTc0MDYiLCJ1cmwiOiIvZ3JvdXAvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tY29nIn0seyJtZW51X25hbWUiOiJcdTY3NDNcdTk2NTBcdTdiYTFcdTc0MDYiLCJ1cmwiOiIvbWFudWxpc3QvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tY29nIn1dfX0sInVzZXIiOiJ0ZXN0bWFuYWdlciJ9', '2019-07-01 13:18:47.603273');
INSERT INTO `django_session` VALUES ('thn6rmwto4thdw4x24x5ucvw4i7x5szg', 'ZjllMWJlOTRlNmVhNmQ0ZTg4OGE4YTVkMjQyZjQxZmQxN2QyZWIzMTp7InBlcm1pc3Npb24iOlt7InVybCI6Ii9kYXRhLyJ9LHsidXJsIjoiL2RhdGFyZXN1bHQvIn0seyJ1cmwiOiIvbWlkZGxlX3Jlc3VsdC8ifSx7InVybCI6Ii9yZXN1bHQvIn0seyJ1cmwiOiIvc3VibWl0LyJ9LHsidXJsIjoiL2RhdGFpbnB1dC8ifSx7InVybCI6Ii9kYXRhaW5wdXRfaWNfbXNiLyJ9LHsidXJsIjoiL2RhdGFpbnB1dF9pY194enkvIn0seyJ1cmwiOiIvZGF0YWlucHV0X2ljX2NzYi8ifSx7InVybCI6Ii9kYXRhaW5wdXRfbXNiLyJ9LHsidXJsIjoiL2RhdGFpbnB1dF94enkvIn0seyJ1cmwiOiIvZGF0YWlucHV0X2NzYi8ifSx7InVybCI6Ii9kZWxfZGF0YS8ifSx7InVybCI6Ii9lZGl0X2RhdGEvIn0seyJ1cmwiOiIvZWRpdF9pY19tc2IvIn0seyJ1cmwiOiIvZWRpdF9pY194enkvIn0seyJ1cmwiOiIvZWRpdF9pY19jc2IvIn0seyJ1cmwiOiIvZWRpdF9tc2IvIn0seyJ1cmwiOiIvZWRpdF94enkvIn0seyJ1cmwiOiIvZWRpdF9jc2IvIn0seyJ1cmwiOiIvY2hlY2tfZGF0YS8ifSx7InVybCI6Ii9jaGVja19pY19tc2IvIn0seyJ1cmwiOiIvY2hlY2tfaWNfeHp5LyJ9LHsidXJsIjoiL2NoZWNrX2ljX2NzYi8ifSx7InVybCI6Ii9jaGVja19tc2IvIn0seyJ1cmwiOiIvY2hlY2tfeHp5LyJ9LHsidXJsIjoiL2NoZWNrX2NzYi8ifSx7InVybCI6Ii91c2VyLyJ9LHsidXJsIjoiL2luZGV4LyJ9XSwibWVudSI6eyIxIjp7Im1lbnVfbmFtZSI6Ilx1NjU3MFx1NjM2ZVx1NWY1NVx1NTE2NSIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QtYWx0Iiwid2VpZ2h0Ijo1LCJjaGlsZHJlbiI6W3sibWVudV9uYW1lIjoiXHU3ZjE2XHU4ZjkxXHU2NTcwXHU2MzZlIiwidXJsIjoiL2RhdGEvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tcGVuY2lsIn0seyJtZW51X25hbWUiOiJcdTViYTFcdTY4MzhcdTYwYzVcdTUxYjUiLCJ1cmwiOiIvZGF0YXJlc3VsdC8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1saXN0In1dfSwiNCI6eyJtZW51X25hbWUiOiJcdTdlZDNcdTY3OWNcdTY3ZTVcdThiZTIiLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1mb2xkZXItb3BlbiIsIndlaWdodCI6MiwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NmQ0Ylx1OGJkNVx1OGZkYlx1NWVhNiIsInVybCI6Ii9taWRkbGVfcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXRhc2tzIn0seyJtZW51X25hbWUiOiJcdTZkNGJcdThiZDVcdTdlZDNcdTY3OWMiLCJ1cmwiOiIvcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QifV19fSwidXNlciI6Im1hbnUwMSIsIk1ldGVySWQiOiIwMDIwMTkwNjE1MDEiLCJNZXRlclR5cGUiOiJcdTgxOWNcdTVmMGZcdTg4NjgiLCJNYW51ZmFjdHVyZU5hbWVfaWQiOjEsIlRpbWVPZlByb2R1Y2UiOiIyMDE5LTA2LTE1In0=', '2019-06-29 14:33:29.741227');
INSERT INTO `django_session` VALUES ('w9rxusxvwgr69m47o742t18il6l36h3m', 'YmM1YTAxYzAwNThmNzE3ZGNiY2U5MDNkMTJjYTkyZjVlNjU5ZDk3Yjp7InBlcm1pc3Npb24iOlt7InVybCI6Ii9kYXRhY2hlY2svIn0seyJ1cmwiOiIvY2hlY2tyZXN1bHQvIn0seyJ1cmwiOiIvYWxsb2NhdGlvbi8ifSx7InVybCI6Ii9hbGxvX3Jlc3VsdC8ifSx7InVybCI6Ii9taWRkbGVfcmVzdWx0LyJ9LHsidXJsIjoiL3Jlc3VsdC8ifSx7InVybCI6Ii9ncm91cC8ifSx7InVybCI6Ii9tYW51bGlzdC8ifSx7InVybCI6Ii9jaGVja19kYXRhLyJ9LHsidXJsIjoiL2NoZWNrX2ljX21zYi8ifSx7InVybCI6Ii9jaGVja19pY194enkvIn0seyJ1cmwiOiIvY2hlY2tfaWNfY3NiLyJ9LHsidXJsIjoiL2NoZWNrX21zYi8ifSx7InVybCI6Ii9jaGVja194enkvIn0seyJ1cmwiOiIvY2hlY2tfY3NiLyJ9LHsidXJsIjoiL2NoZWNrLyJ9LHsidXJsIjoiL3N1Yl9hbGxvY2F0aW9uLyJ9LHsidXJsIjoiL2dyb3VwX2FkZC8ifSx7InVybCI6Ii9ncm91cF9lZGl0LyJ9LHsidXJsIjoiL2dyb3VwX2RlbC8ifSx7InVybCI6Ii9tYW51bGlzdF9hZGQvIn0seyJ1cmwiOiIvbWFudWxpc3RfZWRpdC8ifSx7InVybCI6Ii9tYW51bGlzdF9kZWwvIn0seyJ1cmwiOiIvcGVybWlzc2lvbmxpc3RfYWRkLyJ9LHsidXJsIjoiL3Blcm1pc3Npb25saXN0X2RlbC8ifSx7InVybCI6Ii9wZXJtaXNzaW9ubGlzdF9lZGl0LyJ9LHsidXJsIjoiL3VzZXIvIn0seyJ1cmwiOiIvaW5kZXgvIn0seyJ1cmwiOiIvbG9naW51c2VyX2FkZC8ifSx7InVybCI6Ii9sb2dpbnVzZXJfZWRpdC8ifSx7InVybCI6Ii9sb2dpbnVzZXJfZGVsLyJ9LHsidXJsIjoiL3N0b3JhZ2UvIn0seyJ1cmwiOiIvZGVsX3Rlc3QvIn0seyJ1cmwiOiIvYmFjay8ifSx7InVybCI6Ii9leHBvcnRfZXhjZWwvIn0seyJ1cmwiOiIvcHdkX3Jlc2V0LyJ9XSwibWVudSI6eyIyIjp7Im1lbnVfbmFtZSI6Ilx1NjU3MFx1NjM2ZVx1NWJhMVx1NjgzOCIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXNlYXJjaCIsIndlaWdodCI6NCwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NWJhMVx1NjgzOFx1NjU3MFx1NjM2ZSIsInVybCI6Ii9kYXRhY2hlY2svIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tc2VhcmNoIn0seyJtZW51X25hbWUiOiJcdTViYTFcdTY4MzhcdTdlZDNcdTY3OWMiLCJ1cmwiOiIvY2hlY2tyZXN1bHQvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tbGlzdCJ9XX0sIjMiOnsibWVudV9uYW1lIjoiXHU2ZDRiXHU4YmQ1XHU1MjA2XHU5MTRkIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tcmV0d2VldCIsIndlaWdodCI6MywiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NTIwNlx1OTE0ZFx1NmQ0Ylx1OGJkNSIsInVybCI6Ii9hbGxvY2F0aW9uLyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXJldHdlZXQifSx7Im1lbnVfbmFtZSI6Ilx1NTIwNlx1OTE0ZFx1N2VkM1x1Njc5YyIsInVybCI6Ii9hbGxvX3Jlc3VsdC8iLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1saXN0In1dfSwiNCI6eyJtZW51X25hbWUiOiJcdTdlZDNcdTY3OWNcdTY3ZTVcdThiZTIiLCJpY29uIjoiZ2x5cGhpY29uIGdseXBoaWNvbi1mb2xkZXItb3BlbiIsIndlaWdodCI6MiwiY2hpbGRyZW4iOlt7Im1lbnVfbmFtZSI6Ilx1NmQ0Ylx1OGJkNVx1OGZkYlx1NWVhNiIsInVybCI6Ii9taWRkbGVfcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXRhc2tzIn0seyJtZW51X25hbWUiOiJcdTZkNGJcdThiZDVcdTdlZDNcdTY3OWMiLCJ1cmwiOiIvcmVzdWx0LyIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLWxpc3QifV19LCI1Ijp7Im1lbnVfbmFtZSI6Ilx1NzUyOFx1NjIzN1x1N2JhMVx1NzQwNiIsImljb24iOiJnbHlwaGljb24gZ2x5cGhpY29uLXVzZXIiLCJ3ZWlnaHQiOjEsImNoaWxkcmVuIjpbeyJtZW51X25hbWUiOiJcdTUyMDZcdTdlYzRcdTdiYTFcdTc0MDYiLCJ1cmwiOiIvZ3JvdXAvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tY29nIn0seyJtZW51X25hbWUiOiJcdTY3NDNcdTk2NTBcdTdiYTFcdTc0MDYiLCJ1cmwiOiIvbWFudWxpc3QvIiwiaWNvbiI6ImdseXBoaWNvbiBnbHlwaGljb24tY29nIn1dfX0sInVzZXIiOiJ0ZXN0bWFuYWdlciIsIk1ldGVySWQiOiIwMDIwMTkwNTI5MTEiLCJNZXRlclR5cGUiOiJcdTgxOWNcdTVmMGZcdTg4NjgiLCJNYW51ZmFjdHVyZU5hbWVfaWQiOjEsIlRpbWVPZlByb2R1Y2UiOiIyMDE5LTA1LTA1IiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNkNWQ5Zjk5NTE3ZTYzMzNiMmM3OGEyNTk1M2U1YzFkNmI0ZmQ4NjMiLCJsb29rMSI6bnVsbCwibG9vazIiOm51bGx9', '2019-06-29 14:39:47.837488');

-- ----------------------------
-- Table structure for `mygas_gs_meterinfo_csb`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_gs_meterinfo_csb`;
CREATE TABLE `mygas_gs_meterinfo_csb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `MeterId` varchar(12) NOT NULL,
  `Com_no_csb` varchar(16) DEFAULT NULL,
  `Sw_rlse_csb` varchar(4) DEFAULT NULL,
  `Vol1` decimal(4,2) DEFAULT NULL,
  `Stan_Ins_Ele_csb` decimal(6,3) DEFAULT NULL,
  `Vol2` decimal(4,2) DEFAULT NULL,
  `Work_Ins_Ele_csb` decimal(6,3) DEFAULT NULL,
  `MeterStateWord` varchar(2) DEFAULT NULL,
  `Temperature_csb` decimal(4,2) DEFAULT NULL,
  `MeterInStateWord` varchar(2) DEFAULT NULL,
  `PValue` decimal(8,3) DEFAULT NULL,
  `Stan_Total_Ele` decimal(10,3) DEFAULT NULL,
  `Peak_Ele` decimal(6,3) DEFAULT NULL,
  `Work_Total_Ele` decimal(10,3) DEFAULT NULL,
  `DropMeter1_csb` datetime(6) DEFAULT NULL,
  `DropMeter2_csb` decimal(8,2) DEFAULT NULL,
  `ReverseInstall1_csb` datetime(6) DEFAULT NULL,
  `ReverseInstall2_csb` decimal(8,2) DEFAULT NULL,
  `MeasureBreakdown1_csb` datetime(6) DEFAULT NULL,
  `MeasureBreakdown2_csb` decimal(8,2) DEFAULT NULL,
  `TSensorBreakdown1_csb` datetime(6) DEFAULT NULL,
  `TSensorBreakdown2_csb` decimal(8,2) DEFAULT NULL,
  `PSensorBreakdown1_csb` datetime(6) DEFAULT NULL,
  `PSensorBreakdown2_csb` decimal(8,2) DEFAULT NULL,
  `TrafficAbnormality1_csb` datetime(6) DEFAULT NULL,
  `TrafficAbnormality2_csb` decimal(8,2) DEFAULT NULL,
  `ComVol1_csb` datetime(6) DEFAULT NULL,
  `ComVol2_csb` decimal(8,2) DEFAULT NULL,
  `BaseVol1_csb` datetime(6) DEFAULT NULL,
  `BaseVol2_csb` decimal(8,2) DEFAULT NULL,
  `CollectFault1_csb` datetime(6) DEFAULT NULL,
  `CollectFault2_csb` decimal(8,2) DEFAULT NULL,
  `GasLeakClose1_csb` datetime(6) DEFAULT NULL,
  `GasLeakClose2_csb` decimal(8,2) DEFAULT NULL,
  `GasStolenClose1_csb` datetime(6) DEFAULT NULL,
  `GasStolenClose2_csb` decimal(8,2) DEFAULT NULL,
  `ResetClose1_csb` datetime(6) DEFAULT NULL,
  `ResetClose2_csb` decimal(8,2) DEFAULT NULL,
  `LowVolClose1_csb` datetime(6) DEFAULT NULL,
  `LowVolClose2_csb` decimal(8,2) DEFAULT NULL,
  `CollectClose1_csb` datetime(6) DEFAULT NULL,
  `CollectClose2_csb` decimal(8,2) DEFAULT NULL,
  `CommandClose1_csb` datetime(6) DEFAULT NULL,
  `CommandClose2_csb` decimal(8,2) DEFAULT NULL,
  `ManulOpen1_csb` datetime(6) DEFAULT NULL,
  `ManulOpen2_csb` decimal(8,2) DEFAULT NULL,
  `AF_ULimit1` varchar(20) DEFAULT NULL,
  `AF_DLimit1` varchar(20) DEFAULT NULL,
  `AF_LLimit1` varchar(20) DEFAULT NULL,
  `AF_ULimit2` varchar(20) DEFAULT NULL,
  `AF_DLimit2` varchar(20) DEFAULT NULL,
  `AF_LLimit2` varchar(20) DEFAULT NULL,
  `AF_ULimit3` varchar(20) DEFAULT NULL,
  `AF_DLimit3` varchar(20) DEFAULT NULL,
  `AF_LLimit3` varchar(20) DEFAULT NULL,
  `FTPUserName_csb` varchar(25) NOT NULL,
  `FTPPassword_csb` varchar(25) NOT NULL,
  `FTPAddress_csb` varchar(50) NOT NULL,
  `FTPCatalog_csb` varchar(50) NOT NULL,
  `FileName_csb` varchar(8) DEFAULT NULL,
  `MeterTypeId_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `MeterId` (`MeterId`),
  UNIQUE KEY `MeterTypeId_id` (`MeterTypeId_id`),
  CONSTRAINT `mygas_gs_me_MeterTypeId_id_dd0f4590_fk_mygas_gs_metertypeinfo_id` FOREIGN KEY (`MeterTypeId_id`) REFERENCES `mygas_gs_metertypeinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_gs_meterinfo_csb
-- ----------------------------

-- ----------------------------
-- Table structure for `mygas_gs_meterinfo_ic`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_gs_meterinfo_ic`;
CREATE TABLE `mygas_gs_meterinfo_ic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `MeterId` varchar(12) NOT NULL,
  `ChargingStatusWord` varchar(2) DEFAULT NULL,
  `CurrentVol` decimal(12,2) DEFAULT NULL,
  `RemainingSum` decimal(8,2) DEFAULT NULL,
  `CumulativeSum` decimal(12,2) DEFAULT NULL,
  `CurrentPrice` decimal(4,2) DEFAULT NULL,
  `CurrentPriceInitialVol` decimal(12,2) DEFAULT NULL,
  `LastPrice` decimal(4,2) DEFAULT NULL,
  `LastPriceInitialVol` decimal(12,2) DEFAULT NULL,
  `ChargingTime` varchar(8) DEFAULT NULL,
  `VerComparison` varchar(2) DEFAULT NULL,
  `PriceSysDate` varchar(10) DEFAULT NULL,
  `PriceMode` varchar(2) DEFAULT NULL,
  `PriceSysVer` varchar(4) DEFAULT NULL,
  `PriceNormal` decimal(4,2) DEFAULT NULL,
  `PriceSysCycle` varchar(2) DEFAULT NULL,
  `PriceCycleDate` varchar(8) DEFAULT NULL,
  `PriceClearSign` varchar(2) DEFAULT NULL,
  `PriceEndDateOne` varchar(8) DEFAULT NULL,
  `PriceOne1` decimal(4,2) DEFAULT NULL,
  `PriceOneAmount1` varchar(8) DEFAULT NULL,
  `PriceOne2` decimal(4,2) DEFAULT NULL,
  `PriceOneAmount2` varchar(8) DEFAULT NULL,
  `PriceOne3` decimal(4,2) DEFAULT NULL,
  `PriceEndDateTwo` varchar(8) DEFAULT NULL,
  `PriceTwo1` decimal(4,2) DEFAULT NULL,
  `PriceTwoAmount1` varchar(8) DEFAULT NULL,
  `PriceTwo2` decimal(4,2) DEFAULT NULL,
  `PriceTwoAmount2` varchar(8) DEFAULT NULL,
  `PriceTwo3` decimal(4,2) DEFAULT NULL,
  `PriceEndDateThree` varchar(8) DEFAULT NULL,
  `PriceThree1` decimal(4,2) DEFAULT NULL,
  `PriceThreeAmount1` varchar(8) DEFAULT NULL,
  `PriceThree2` decimal(4,2) DEFAULT NULL,
  `PriceThreeAmount2` varchar(8) DEFAULT NULL,
  `PriceThree3` decimal(4,2) DEFAULT NULL,
  `PriceEndDateFour` varchar(8) DEFAULT NULL,
  `PriceFour1` decimal(4,2) DEFAULT NULL,
  `PriceFourAmount1` varchar(8) DEFAULT NULL,
  `PriceFour2` decimal(4,2) DEFAULT NULL,
  `PriceFourAmount2` varchar(8) DEFAULT NULL,
  `PriceFour3` decimal(4,2) DEFAULT NULL,
  `PriceEndDateFive` varchar(8) DEFAULT NULL,
  `PriceFive1` decimal(4,2) DEFAULT NULL,
  `PriceFiveAmount1` varchar(8) DEFAULT NULL,
  `PriceFive2` decimal(4,2) DEFAULT NULL,
  `PriceFiveAmount2` varchar(8) DEFAULT NULL,
  `PriceFive3` decimal(4,2) DEFAULT NULL,
  `PriceSysDate_C` varchar(10) DEFAULT NULL,
  `PriceSysCycle_C` varchar(2) DEFAULT NULL,
  `PriceMode_C` varchar(2) DEFAULT NULL,
  `PriceCycleDate_C` varchar(8) DEFAULT NULL,
  `PriceSysVer_C` varchar(4) DEFAULT NULL,
  `PriceClearSign_C` varchar(2) DEFAULT NULL,
  `PriceNormal_C` decimal(4,2) DEFAULT NULL,
  `DelayExists_C` varchar(2) DEFAULT NULL,
  `PriceEndDateOne_C` varchar(8) DEFAULT NULL,
  `PriceOne1_C` decimal(4,2) DEFAULT NULL,
  `PriceOneAmount1_C` varchar(8) DEFAULT NULL,
  `PriceOne2_C` decimal(4,2) DEFAULT NULL,
  `PriceOneAmount2_C` varchar(8) DEFAULT NULL,
  `PriceOne3_C` decimal(4,2) DEFAULT NULL,
  `PriceEndDateTwo_C` varchar(8) DEFAULT NULL,
  `PriceTwo1_C` decimal(4,2) DEFAULT NULL,
  `PriceTwoAmount1_C` varchar(8) DEFAULT NULL,
  `PriceTwo2_C` decimal(4,2) DEFAULT NULL,
  `PriceTwoAmount2_C` varchar(8) DEFAULT NULL,
  `PriceTwo3_C` decimal(4,2) DEFAULT NULL,
  `PriceEndDateThree_C` varchar(8) DEFAULT NULL,
  `PriceThree1_C` decimal(4,2) DEFAULT NULL,
  `PriceThreeAmount1_C` varchar(8) DEFAULT NULL,
  `PriceThree2_C` decimal(4,2) DEFAULT NULL,
  `PriceThreeAmount2_C` varchar(8) DEFAULT NULL,
  `PriceThree3_C` decimal(4,2) DEFAULT NULL,
  `PriceEndDateFour_C` varchar(8) DEFAULT NULL,
  `PriceFour1_C` decimal(4,2) DEFAULT NULL,
  `PriceFourAmount1_C` varchar(8) DEFAULT NULL,
  `PriceFour2_C` decimal(4,2) DEFAULT NULL,
  `PriceFourAmount2_C` varchar(8) DEFAULT NULL,
  `PriceFour3_C` decimal(4,2) DEFAULT NULL,
  `PriceEndDateFive_C` varchar(8) DEFAULT NULL,
  `PriceFive1_C` decimal(4,2) DEFAULT NULL,
  `PriceFiveAmount1_C` varchar(8) DEFAULT NULL,
  `PriceFive2_C` decimal(4,2) DEFAULT NULL,
  `PriceFiveAmount2_C` varchar(8) DEFAULT NULL,
  `PriceFive3_C` decimal(4,2) DEFAULT NULL,
  `RechargeDate1` varchar(8) DEFAULT NULL,
  `RemainingSumBefore1` varchar(8) DEFAULT NULL,
  `RechargeSum1` varchar(8) DEFAULT NULL,
  `RechargeDate2` varchar(8) DEFAULT NULL,
  `RemainingSumBefore2` varchar(8) DEFAULT NULL,
  `RechargeSum2` varchar(8) DEFAULT NULL,
  `RechargeDate3` varchar(8) DEFAULT NULL,
  `RemainingSumBefore3` varchar(8) DEFAULT NULL,
  `RechargeSum3` varchar(8) DEFAULT NULL,
  `RechargeDate4` varchar(8) DEFAULT NULL,
  `RemainingSumBefore4` varchar(8) DEFAULT NULL,
  `RechargeSum4` varchar(8) DEFAULT NULL,
  `RechargeDate5` varchar(8) DEFAULT NULL,
  `RemainingSumBefore5` varchar(8) DEFAULT NULL,
  `RechargeSum5` varchar(8) DEFAULT NULL,
  `MeterTypeId_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `MeterId` (`MeterId`),
  UNIQUE KEY `MeterTypeId_id` (`MeterTypeId_id`),
  CONSTRAINT `mygas_gs_me_MeterTypeId_id_a5c364c5_fk_mygas_gs_metertypeinfo_id` FOREIGN KEY (`MeterTypeId_id`) REFERENCES `mygas_gs_metertypeinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_gs_meterinfo_ic
-- ----------------------------

-- ----------------------------
-- Table structure for `mygas_gs_meterinfo_msb`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_gs_meterinfo_msb`;
CREATE TABLE `mygas_gs_meterinfo_msb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `MeterId` varchar(12) NOT NULL,
  `Com_no_msb` varchar(16) DEFAULT NULL,
  `Sw_rlse_msb` varchar(4) DEFAULT NULL,
  `Real_vol` decimal(10,2) DEFAULT NULL,
  `Meter_v` decimal(4,2) DEFAULT NULL,
  `Temperature_msb` decimal(4,2) DEFAULT NULL,
  `Status` varchar(4) DEFAULT NULL,
  `DropMeter1_msb` datetime(6) DEFAULT NULL,
  `DropMeter2_msb` decimal(8,2) DEFAULT NULL,
  `ReverseInstall1_msb` datetime(6) DEFAULT NULL,
  `ReverseInstall2_msb` decimal(8,2) DEFAULT NULL,
  `MeasureBreakdown1_msb` datetime(6) DEFAULT NULL,
  `MeasureBreakdown2_msb` decimal(8,2) DEFAULT NULL,
  `TSensorBreakdown1_msb` datetime(6) DEFAULT NULL,
  `TSensorBreakdown2_msb` decimal(8,2) DEFAULT NULL,
  `PSensorBreakdown1_msb` datetime(6) DEFAULT NULL,
  `PSensorBreakdown2_msb` decimal(8,2) DEFAULT NULL,
  `TrafficAbnormality1_msb` datetime(6) DEFAULT NULL,
  `TrafficAbnormality2_msb` decimal(8,2) DEFAULT NULL,
  `ComVol1_msb` datetime(6) DEFAULT NULL,
  `ComVol2_msb` decimal(8,2) DEFAULT NULL,
  `BaseVol1_msb` datetime(6) DEFAULT NULL,
  `BaseVol2_msb` decimal(8,2) DEFAULT NULL,
  `CollectFault1_msb` datetime(6) DEFAULT NULL,
  `CollectFault2_msb` decimal(8,2) DEFAULT NULL,
  `GasLeakClose1_msb` datetime(6) DEFAULT NULL,
  `GasLeakClose2_msb` decimal(8,2) DEFAULT NULL,
  `GasStolenClose1_msb` datetime(6) DEFAULT NULL,
  `GasStolenClose2_msb` decimal(8,2) DEFAULT NULL,
  `ResetClose1_msb` datetime(6) DEFAULT NULL,
  `ResetClose2_msb` decimal(8,2) DEFAULT NULL,
  `LowVolClose1_msb` datetime(6) DEFAULT NULL,
  `LowVolClose2_msb` decimal(8,2) DEFAULT NULL,
  `CollectClose1_msb` datetime(6) DEFAULT NULL,
  `CollectClose2_msb` decimal(8,2) DEFAULT NULL,
  `CommandClose1_msb` datetime(6) DEFAULT NULL,
  `CommandClose2_msb` decimal(8,2) DEFAULT NULL,
  `ManulOpen1_msb` datetime(6) DEFAULT NULL,
  `ManulOpen2_msb` decimal(8,2) DEFAULT NULL,
  `FTPUserName_msb` varchar(25) NOT NULL,
  `FTPPassword_msb` varchar(25) NOT NULL,
  `FTPAddress_msb` varchar(50) NOT NULL,
  `FTPCatalog_msb` varchar(50) NOT NULL,
  `FileName_msb` varchar(8) DEFAULT NULL,
  `MeterTypeId_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `MeterId` (`MeterId`),
  UNIQUE KEY `MeterTypeId_id` (`MeterTypeId_id`),
  CONSTRAINT `mygas_gs_me_MeterTypeId_id_a1a75b93_fk_mygas_gs_metertypeinfo_id` FOREIGN KEY (`MeterTypeId_id`) REFERENCES `mygas_gs_metertypeinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_gs_meterinfo_msb
-- ----------------------------
INSERT INTO `mygas_gs_meterinfo_msb` VALUES ('11', '002019061500', '0000000000000000', '0000', '12345.67', '3.50', '12.34', '0000', '2019-08-10 01:00:00.000000', '10.00', null, null, '2019-08-10 03:00:00.000000', '11.00', null, null, null, null, '2019-08-10 06:00:00.000000', '16.00', null, null, '2019-08-10 10:00:00.000000', '20.00', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '01', '01', '139.199.191.23', 'D:\\FTPPoint\\File', '11', '13');
INSERT INTO `mygas_gs_meterinfo_msb` VALUES ('12', '002019061530', '0000000000000000', '0000', '12345.67', '3.50', '12.34', '0000', '2019-08-10 01:00:00.000000', '10.00', null, null, '2019-08-10 03:00:00.000000', '11.00', null, null, null, null, '2019-08-10 06:00:00.000000', '16.00', null, null, '2019-08-10 10:00:00.000000', '20.00', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '01', '01', '139.199.191.23', 'D:\\FTPPoint\\File', '11', '14');
INSERT INTO `mygas_gs_meterinfo_msb` VALUES ('13', '002019061540', '0000000000000000', '0000', '12345.67', '3.50', '12.34', '0000', '2019-08-10 01:00:00.000000', '10.00', null, null, '2019-08-10 03:00:00.000000', '11.00', null, null, null, null, '2019-08-10 06:00:00.000000', '16.00', null, null, '2019-08-10 10:00:00.000000', '20.00', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '01', '01', '139.199.191.23', 'D:\\FTPPoint\\File', '11', '15');
INSERT INTO `mygas_gs_meterinfo_msb` VALUES ('14', '002019061600', '0000000000000000', '0000', '12345.67', '3.50', '12.34', '0000', '2019-08-10 01:00:00.000000', '10.00', null, null, '2019-08-10 03:00:00.000000', '11.00', null, null, null, null, '2019-08-10 06:00:00.000000', '16.00', null, null, '2019-08-10 10:00:00.000000', '20.00', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '01', '01', '139.199.191.23', 'D:\\FTPPoint\\File', '11', '16');
INSERT INTO `mygas_gs_meterinfo_msb` VALUES ('15', '002019061601', '0000000000000000', '0000', '12345.67', '3.50', '12.34', '0000', '2019-08-10 01:00:00.000000', '10.00', null, null, '2019-08-10 03:00:00.000000', '11.00', null, null, null, null, '2019-08-10 06:00:00.000000', '16.00', null, null, '2019-08-10 10:00:00.000000', '20.00', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '01', '01', '139.199.191.23', 'D:\\FTPPoint\\File', '11', '17');
INSERT INTO `mygas_gs_meterinfo_msb` VALUES ('16', '002019061602', '0000000000000000', '0000', '12345.67', '3.50', '12.34', '0000', '2019-08-10 01:00:00.000000', '10.00', null, null, '2019-08-10 03:00:00.000000', '11.00', null, null, null, null, '2019-08-10 06:00:00.000000', '16.00', null, null, '2019-08-10 10:00:00.000000', '20.00', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '01', '01', '139.199.191.23', 'D:\\FTPPoint\\File', '11', '18');

-- ----------------------------
-- Table structure for `mygas_gs_meterinfo_xzy`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_gs_meterinfo_xzy`;
CREATE TABLE `mygas_gs_meterinfo_xzy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `MeterId` varchar(12) NOT NULL,
  `Com_no_xzy` varchar(16) DEFAULT NULL,
  `Sw_rlse_xzy` varchar(4) DEFAULT NULL,
  `MeterNum` int(11) DEFAULT NULL,
  `Temperature_xzy` decimal(4,2) DEFAULT NULL,
  `Disturb_Total_Vol` decimal(8,2) DEFAULT NULL,
  `Pressure` varchar(8) DEFAULT NULL,
  `Correction_E` decimal(4,2) DEFAULT NULL,
  `Stan_Total_Vol` decimal(12,2) DEFAULT NULL,
  `Stan_Ins_Ele_xzy` decimal(6,2) DEFAULT NULL,
  `Work_Total_Vol` decimal(12,2) DEFAULT NULL,
  `Work_Ins_Ele_xzy` decimal(6,2) DEFAULT NULL,
  `DropMeter1_xzy` datetime(6) DEFAULT NULL,
  `DropMeter2_xzy` decimal(8,2) DEFAULT NULL,
  `ReverseInstall1_xzy` datetime(6) DEFAULT NULL,
  `ReverseInstall2_xzy` decimal(8,2) DEFAULT NULL,
  `MeasureBreakdown1_xzy` datetime(6) DEFAULT NULL,
  `MeasureBreakdown2_xzy` decimal(8,2) DEFAULT NULL,
  `TSensorBreakdown1_xzy` datetime(6) DEFAULT NULL,
  `TSensorBreakdown2_xzy` decimal(8,2) DEFAULT NULL,
  `PSensorBreakdown1_xzy` datetime(6) DEFAULT NULL,
  `PSensorBreakdown2_xzy` decimal(8,2) DEFAULT NULL,
  `TrafficAbnormality1_xzy` datetime(6) DEFAULT NULL,
  `TrafficAbnormality2_xzy` decimal(8,2) DEFAULT NULL,
  `ComVol1_xzy` datetime(6) DEFAULT NULL,
  `ComVol2_xzy` decimal(8,2) DEFAULT NULL,
  `BaseVol1_xzy` datetime(6) DEFAULT NULL,
  `BaseVol2_xzy` decimal(8,2) DEFAULT NULL,
  `CollectFault1_xzy` datetime(6) DEFAULT NULL,
  `CollectFault2_xzy` decimal(8,2) DEFAULT NULL,
  `GasLeakClose1_xzy` datetime(6) DEFAULT NULL,
  `GasLeakClose2_xzy` decimal(8,2) DEFAULT NULL,
  `GasStolenClose1_xzy` datetime(6) DEFAULT NULL,
  `GasStolenClose2_xzy` decimal(8,2) DEFAULT NULL,
  `ResetClose1_xzy` datetime(6) DEFAULT NULL,
  `ResetClose2_xzy` decimal(8,2) DEFAULT NULL,
  `LowVolClose1_xzy` datetime(6) DEFAULT NULL,
  `LowVolClose2_xzy` decimal(8,2) DEFAULT NULL,
  `CollectClose1_xzy` datetime(6) DEFAULT NULL,
  `CollectClose2_xzy` decimal(8,2) DEFAULT NULL,
  `CommandClose1_xzy` datetime(6) DEFAULT NULL,
  `CommandClose2_xzy` decimal(8,2) DEFAULT NULL,
  `ManulOpen1_xzy` datetime(6) DEFAULT NULL,
  `ManulOpen2_xzy` decimal(8,2) DEFAULT NULL,
  `FTPUserName_xzy` varchar(25) NOT NULL,
  `FTPPassword_xzy` varchar(25) NOT NULL,
  `FTPAddress_xzy` varchar(50) NOT NULL,
  `FTPCatalog_xzy` varchar(50) NOT NULL,
  `FileName_xzy` varchar(8) DEFAULT NULL,
  `MeterTypeId_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `MeterId` (`MeterId`),
  UNIQUE KEY `MeterTypeId_id` (`MeterTypeId_id`),
  CONSTRAINT `mygas_gs_me_MeterTypeId_id_9c4969e7_fk_mygas_gs_metertypeinfo_id` FOREIGN KEY (`MeterTypeId_id`) REFERENCES `mygas_gs_metertypeinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_gs_meterinfo_xzy
-- ----------------------------

-- ----------------------------
-- Table structure for `mygas_gs_metertypeinfo`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_gs_metertypeinfo`;
CREATE TABLE `mygas_gs_metertypeinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `MeterId` varchar(12) NOT NULL,
  `MeterType` varchar(10) NOT NULL,
  `TimeOfProduce` date NOT NULL,
  `Subtime` datetime(6) DEFAULT NULL,
  `CheckTime` datetime(6) DEFAULT NULL,
  `IsSubmit` tinyint(1) NOT NULL,
  `IsDataChecked` tinyint(1) NOT NULL,
  `DataCheckedResult` tinyint(1) NOT NULL,
  `IsAllocated` tinyint(1) NOT NULL,
  `CommandTest` varchar(10) DEFAULT NULL,
  `ICTest` varchar(10) DEFAULT NULL,
  `ChuTest` varchar(10) DEFAULT NULL,
  `ZhoTest` varchar(10) DEFAULT NULL,
  `MianTest` varchar(10) DEFAULT NULL,
  `TestUnit` varchar(50) NOT NULL,
  `ManufactureName_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `check_user` varchar(50) DEFAULT NULL,
  `allo_user` varchar(50) DEFAULT NULL,
  `MeterPrivilege` varchar(1) NOT NULL,
  `IsTest` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `MeterId` (`MeterId`),
  KEY `mygas_gs_metertypeinfo_c467cca2` (`ManufactureName_id`),
  KEY `mygas_gs_metertypeinfo_e8701ad4` (`user_id`),
  CONSTRAINT `mygas_gs_met_ManufactureName_id_8fe939b4_fk_mygas_manufacture_id` FOREIGN KEY (`ManufactureName_id`) REFERENCES `mygas_manufacture` (`id`),
  CONSTRAINT `mygas_gs_metertypeinfo_user_id_39ed0599_fk_rbac_user_info_id` FOREIGN KEY (`user_id`) REFERENCES `rbac_user_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_gs_metertypeinfo
-- ----------------------------
INSERT INTO `mygas_gs_metertypeinfo` VALUES ('13', '002019061500', '膜式表', '2019-06-15', '2019-06-15 15:03:22.237335', '2019-06-15 15:03:39.511488', '1', '1', '1', '1', '不测', '不测', '待测', '不测', '否', '上海燃气有限公司', '1', '1', 'testmanager', 'testmanager', '0', '0');
INSERT INTO `mygas_gs_metertypeinfo` VALUES ('14', '002019061530', '膜式表', '2019-06-15', '2019-06-15 20:18:39.887801', '2019-06-15 20:18:56.852502', '1', '1', '1', '1', '不测', '不测', '待测', '不测', '否', '上海燃气有限公司', '1', '1', 'testmanager', 'testmanager', '0', '0');
INSERT INTO `mygas_gs_metertypeinfo` VALUES ('15', '002019061540', '膜式表', '2019-06-15', '2019-06-15 21:17:30.456724', '2019-06-15 21:17:41.406570', '1', '1', '1', '1', '不测', '不测', '待测', '不测', '否', '上海燃气有限公司', '1', '1', 'testmanager', 'testmanager', '0', '1');
INSERT INTO `mygas_gs_metertypeinfo` VALUES ('16', '002019061600', '膜式表', '2019-06-16', '2019-06-16 14:29:27.867723', '2019-06-16 14:29:52.424571', '1', '1', '1', '1', '不测', '不测', '待测', '不测', '否', '上海燃气有限公司', '1', '39', 'wll', 'wll', '0', '1');
INSERT INTO `mygas_gs_metertypeinfo` VALUES ('17', '002019061601', '膜式表', '2019-06-16', '2019-06-16 15:45:18.990820', '2019-06-16 15:45:29.394500', '1', '1', '1', '1', '不测', '不测', '待测', '不测', '否', '上海燃气有限公司', '1', '39', 'wll', 'wll', '0', '0');
INSERT INTO `mygas_gs_metertypeinfo` VALUES ('18', '002019061602', '膜式表', '2019-06-16', '2019-06-16 15:46:10.757106', '2019-06-16 15:46:20.426232', '1', '1', '1', '1', '不测', '不测', '待测', '不测', '否', '上海燃气有限公司', '1', '39', 'wll', 'wll', '0', '0');

-- ----------------------------
-- Table structure for `mygas_manufacture`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_manufacture`;
CREATE TABLE `mygas_manufacture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ManufactureName` varchar(30) NOT NULL,
  `code` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_manufacture
-- ----------------------------
INSERT INTO `mygas_manufacture` VALUES ('1', '上海蓝宝石', '01');
INSERT INTO `mygas_manufacture` VALUES ('2', '宁海蓝宝石', '02');
INSERT INTO `mygas_manufacture` VALUES ('3', '上海克罗姆', '03');
INSERT INTO `mygas_manufacture` VALUES ('4', '埃创', '04');
INSERT INTO `mygas_manufacture` VALUES ('5', '丹东热工', '05');
INSERT INTO `mygas_manufacture` VALUES ('6', '浙江荣鑫', '06');
INSERT INTO `mygas_manufacture` VALUES ('7', '天津五机', '07');
INSERT INTO `mygas_manufacture` VALUES ('8', '上海埃科', '08');
INSERT INTO `mygas_manufacture` VALUES ('9', '浙江苍南', '09');
INSERT INTO `mygas_manufacture` VALUES ('10', '浙江天信', '10');
INSERT INTO `mygas_manufacture` VALUES ('11', '天信德莱塞', '11');
INSERT INTO `mygas_manufacture` VALUES ('12', '埃尔斯特', '12');
INSERT INTO `mygas_manufacture` VALUES ('13', '日本', '13');
INSERT INTO `mygas_manufacture` VALUES ('14', '丹尼尔', '14');
INSERT INTO `mygas_manufacture` VALUES ('15', '丹东思凯', '15');
INSERT INTO `mygas_manufacture` VALUES ('16', '杭州先锋', '16');
INSERT INTO `mygas_manufacture` VALUES ('17', '郑州安然', '17');
INSERT INTO `mygas_manufacture` VALUES ('18', '成都千嘉', '18');
INSERT INTO `mygas_manufacture` VALUES ('19', '杭州金卡', '19');
INSERT INTO `mygas_manufacture` VALUES ('20', '航天动力', '20');
INSERT INTO `mygas_manufacture` VALUES ('21', '上海佳盛', '21');
INSERT INTO `mygas_manufacture` VALUES ('22', '上海飞奥', '22');
INSERT INTO `mygas_manufacture` VALUES ('23', '上海众德', '23');
INSERT INTO `mygas_manufacture` VALUES ('24', '上海金速', '24');
INSERT INTO `mygas_manufacture` VALUES ('25', '四川海力', '25');
INSERT INTO `mygas_manufacture` VALUES ('26', '浙江松川', '26');
INSERT INTO `mygas_manufacture` VALUES ('27', '上海安居利', '27');
INSERT INTO `mygas_manufacture` VALUES ('28', '宁波佳德', '28');
INSERT INTO `mygas_manufacture` VALUES ('29', '杭州鸿鹄', '29');
INSERT INTO `mygas_manufacture` VALUES ('30', '上海真兰', '30');
INSERT INTO `mygas_manufacture` VALUES ('31', '山东思达特', '31');
INSERT INTO `mygas_manufacture` VALUES ('32', 'RMG', '32');
INSERT INTO `mygas_manufacture` VALUES ('33', 'FISHER', '33');
INSERT INTO `mygas_manufacture` VALUES ('34', '其他', '34');
INSERT INTO `mygas_manufacture` VALUES ('35', '浙江威星', '35');
INSERT INTO `mygas_manufacture` VALUES ('36', '上海玮轩', '36');
INSERT INTO `mygas_manufacture` VALUES ('37', '兆富电子', '37');
INSERT INTO `mygas_manufacture` VALUES ('38', '无锡云感', '38');

-- ----------------------------
-- Table structure for `mygas_meterplat`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_meterplat`;
CREATE TABLE `mygas_meterplat` (
  `MeterId` varchar(12) NOT NULL,
  `Meterip_Com` varchar(10) DEFAULT NULL,
  `Meterip_IC` varchar(10) DEFAULT NULL,
  `Meterip_Chu` varchar(10) DEFAULT NULL,
  `Meterip_Zhong` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`MeterId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_meterplat
-- ----------------------------
INSERT INTO `mygas_meterplat` VALUES ('002019061500', '-1', '-1', '1', '-1');
INSERT INTO `mygas_meterplat` VALUES ('002019061530', '-1', '-1', '1', '-1');
INSERT INTO `mygas_meterplat` VALUES ('002019061540', '-1', '-1', '1', '-1');
INSERT INTO `mygas_meterplat` VALUES ('002019061600', '-1', '-1', '1', '-1');

-- ----------------------------
-- Table structure for `mygas_meter_result`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_meter_result`;
CREATE TABLE `mygas_meter_result` (
  `MeterId` varchar(12) NOT NULL,
  `MeterType` varchar(10) NOT NULL,
  `MeterComState` varchar(25) NOT NULL,
  `MeterIcState` varchar(25) NOT NULL,
  `MeterChuState` varchar(25) NOT NULL,
  `MeterZhongState` varchar(25) NOT NULL,
  `MeterState` varchar(25) NOT NULL,
  `MeterTest` varchar(25) NOT NULL,
  `MeterRand_num` varchar(25) DEFAULT NULL,
  `Meteriport` varchar(50) DEFAULT NULL,
  `MeterTime` datetime(6) DEFAULT NULL,
  `MeterCancel` varchar(10) NOT NULL,
  `MeterEvery` varchar(32) NOT NULL,
  `MeterPrivilege` varchar(1) NOT NULL,
  `CheckTime` datetime(6),
  `ManufactureName_id` int(11),
  `Subtime` datetime(6),
  PRIMARY KEY (`MeterId`),
  KEY `mygas_meter_result_c467cca2` (`ManufactureName_id`),
  CONSTRAINT `mygas_meter__ManufactureName_id_3b9cb45b_fk_mygas_manufacture_id` FOREIGN KEY (`ManufactureName_id`) REFERENCES `mygas_manufacture` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_meter_result
-- ----------------------------
INSERT INTO `mygas_meter_result` VALUES ('002019061500', '膜式表', '不测', '不测', '合格', '不测', '合格', '准备', '87819DD4', '1@192.168.3.101@3001@PlatChus_msb', '2019-06-15 19:55:59.540000', '否', 'AAAAAAAA000000000000000000000000', '0', '2019-06-15 15:03:39.511488', '1', '2019-06-15 15:03:22.237335');
INSERT INTO `mygas_meter_result` VALUES ('002019061530', '膜式表', '不测', '不测', '合格', '不测', '合格', '准备', 'E8923D14', '1@192.168.3.101@3001@PlatChus_msb', '2019-06-15 20:39:59.997000', '否', 'AAAAAAAA000000000000000000000000', '0', '2019-06-15 20:18:56.852502', '1', '2019-06-15 20:18:39.887801');

-- ----------------------------
-- Table structure for `mygas_meter_result_record`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_meter_result_record`;
CREATE TABLE `mygas_meter_result_record` (
  `MeterId` varchar(12) NOT NULL,
  `MeterType` varchar(10) NOT NULL,
  `MeterComState` varchar(25) NOT NULL,
  `MeterIcState` varchar(25) NOT NULL,
  `MeterChuState` varchar(25) NOT NULL,
  `MeterZhongState` varchar(25) NOT NULL,
  `MeterState` varchar(25) NOT NULL,
  `MeterTest` varchar(25) NOT NULL,
  `MeterRand_num` varchar(25) DEFAULT NULL,
  `Meteriport` varchar(50) DEFAULT NULL,
  `MeterTime` datetime(6) DEFAULT NULL,
  `MeterCancel` varchar(10) NOT NULL,
  `MeterEvery` varchar(32) NOT NULL,
  `MeterPrivilege` varchar(1) NOT NULL,
  `CheckTime` datetime(6),
  `ManufactureName_id` int(11),
  `Subtime` datetime(6),
  PRIMARY KEY (`MeterId`),
  KEY `mygas_meter_result_record_c467cca2` (`ManufactureName_id`),
  CONSTRAINT `mygas_meter__ManufactureName_id_d3d7cd06_fk_mygas_manufacture_id` FOREIGN KEY (`ManufactureName_id`) REFERENCES `mygas_manufacture` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_meter_result_record
-- ----------------------------
INSERT INTO `mygas_meter_result_record` VALUES ('002019061540', '膜式表', '不测', '不测', '合格', '不测', '完成', '空闲', '9857FFD4', '1@192.168.3.101@3001@PlatChus_msb', '2019-06-17 12:40:33.055808', '否', 'AAAAAAAA000000000000000000000000', '0', '2019-06-15 21:17:41.406570', '1', '2019-06-15 21:17:30.456724');
INSERT INTO `mygas_meter_result_record` VALUES ('002019061600', '膜式表', '不测', '不测', '不合格', '不测', '不合格', '空闲', 'CF4F0E5A', '1@192.168.3.101@3001@PlatChus_msb', '2019-06-17 12:40:32.978282', '否', '55AAAAAA000000000000000000000000', '0', '2019-06-16 14:29:52.424571', '1', '2019-06-16 14:29:27.867723');

-- ----------------------------
-- Table structure for `mygas_meter_test`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_meter_test`;
CREATE TABLE `mygas_meter_test` (
  `MeterId` varchar(12) NOT NULL,
  `MeterType` varchar(10) NOT NULL,
  `MeterComState` varchar(25) NOT NULL,
  `MeterIcState` varchar(25) NOT NULL,
  `MeterChuState` varchar(25) NOT NULL,
  `MeterZhongState` varchar(25) NOT NULL,
  `MeterState` varchar(25) NOT NULL,
  `MeterTest` varchar(25) NOT NULL,
  `MeterRand_num` varchar(25) DEFAULT NULL,
  `Meteriport` varchar(50) DEFAULT NULL,
  `MeterTime` datetime(6) DEFAULT NULL,
  `MeterCancel` varchar(10) NOT NULL,
  `MeterEvery` varchar(32) NOT NULL,
  `MeterPrivilege` varchar(1) NOT NULL,
  `CheckTime` datetime(6),
  `ManufactureName_id` int(11),
  `Subtime` datetime(6),
  PRIMARY KEY (`MeterId`),
  KEY `mygas_meter_test_c467cca2` (`ManufactureName_id`),
  CONSTRAINT `mygas_meter__ManufactureName_id_c37bcf49_fk_mygas_manufacture_id` FOREIGN KEY (`ManufactureName_id`) REFERENCES `mygas_manufacture` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_meter_test
-- ----------------------------
INSERT INTO `mygas_meter_test` VALUES ('002019061601', '膜式表', '不测', '不测', '待测', '不测', '初始', '空闲', null, null, '2019-06-16 15:45:33.553248', '否', '00000000000000000000000000000000', '0', '2019-06-16 15:45:29.394500', '1', '2019-06-16 15:45:18.990820');
INSERT INTO `mygas_meter_test` VALUES ('002019061602', '膜式表', '不测', '不测', '待测', '不测', '初始', '空闲', null, null, '2019-06-16 15:46:26.133237', '否', '00000000000000000000000000000000', '0', '2019-06-16 15:46:20.426232', '1', '2019-06-16 15:46:10.757106');

-- ----------------------------
-- Table structure for `mygas_planinfo`
-- ----------------------------
DROP TABLE IF EXISTS `mygas_planinfo`;
CREATE TABLE `mygas_planinfo` (
  `id` int(11) NOT NULL,
  `IP` varchar(30) NOT NULL,
  `PlatComs` varchar(20) NOT NULL,
  `PlatIcs` varchar(20) NOT NULL,
  `PlatChus_msb` varchar(20) NOT NULL,
  `PlatChus_xzy` varchar(20) NOT NULL,
  `PlatChus_csb` varchar(20) NOT NULL,
  `PlatZhos` varchar(20) NOT NULL,
  `PlatComp` varchar(20) DEFAULT NULL,
  `PlatIcp` varchar(20) DEFAULT NULL,
  `PlatChup_msb` varchar(20) DEFAULT NULL,
  `PlatChup_xzy` varchar(20) DEFAULT NULL,
  `PlatChup_csb` varchar(20) DEFAULT NULL,
  `PlatZhop` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mygas_planinfo
-- ----------------------------
INSERT INTO `mygas_planinfo` VALUES ('1', '192.168.3.101', '未启用', '未启用', '空闲', '未启用', '未启用', '未启用', '3003', '3002', '3001', '3004', '3005', '3006');

-- ----------------------------
-- Table structure for `rbac_group_info`
-- ----------------------------
DROP TABLE IF EXISTS `rbac_group_info`;
CREATE TABLE `rbac_group_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groupname` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rbac_group_info
-- ----------------------------
INSERT INTO `rbac_group_info` VALUES ('1', '生产厂商');
INSERT INTO `rbac_group_info` VALUES ('2', '测试人员-管理员');
INSERT INTO `rbac_group_info` VALUES ('3', '测试人员-操作员');
INSERT INTO `rbac_group_info` VALUES ('4', '超级管理员');

-- ----------------------------
-- Table structure for `rbac_group_info_permission`
-- ----------------------------
DROP TABLE IF EXISTS `rbac_group_info_permission`;
CREATE TABLE `rbac_group_info_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_info_id` int(11) NOT NULL,
  `permission_info_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rbac_group_info_permission_group_info_id_59d07785_uniq` (`group_info_id`,`permission_info_id`),
  KEY `rbac_grou_permission_info_id_01203fc3_fk_rbac_permission_info_id` (`permission_info_id`),
  CONSTRAINT `rbac_grou_permission_info_id_01203fc3_fk_rbac_permission_info_id` FOREIGN KEY (`permission_info_id`) REFERENCES `rbac_permission_info` (`id`),
  CONSTRAINT `rbac_group_info_per_group_info_id_b76bb076_fk_rbac_group_info_id` FOREIGN KEY (`group_info_id`) REFERENCES `rbac_group_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=163 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rbac_group_info_permission
-- ----------------------------
INSERT INTO `rbac_group_info_permission` VALUES ('1', '1', '1');
INSERT INTO `rbac_group_info_permission` VALUES ('2', '1', '2');
INSERT INTO `rbac_group_info_permission` VALUES ('3', '1', '3');
INSERT INTO `rbac_group_info_permission` VALUES ('4', '1', '4');
INSERT INTO `rbac_group_info_permission` VALUES ('5', '1', '5');
INSERT INTO `rbac_group_info_permission` VALUES ('6', '1', '6');
INSERT INTO `rbac_group_info_permission` VALUES ('7', '1', '7');
INSERT INTO `rbac_group_info_permission` VALUES ('8', '1', '8');
INSERT INTO `rbac_group_info_permission` VALUES ('9', '1', '9');
INSERT INTO `rbac_group_info_permission` VALUES ('10', '1', '10');
INSERT INTO `rbac_group_info_permission` VALUES ('11', '1', '11');
INSERT INTO `rbac_group_info_permission` VALUES ('12', '1', '12');
INSERT INTO `rbac_group_info_permission` VALUES ('13', '1', '13');
INSERT INTO `rbac_group_info_permission` VALUES ('14', '1', '14');
INSERT INTO `rbac_group_info_permission` VALUES ('15', '1', '15');
INSERT INTO `rbac_group_info_permission` VALUES ('16', '1', '16');
INSERT INTO `rbac_group_info_permission` VALUES ('17', '1', '17');
INSERT INTO `rbac_group_info_permission` VALUES ('146', '1', '19');
INSERT INTO `rbac_group_info_permission` VALUES ('147', '1', '20');
INSERT INTO `rbac_group_info_permission` VALUES ('148', '1', '21');
INSERT INTO `rbac_group_info_permission` VALUES ('149', '1', '22');
INSERT INTO `rbac_group_info_permission` VALUES ('150', '1', '23');
INSERT INTO `rbac_group_info_permission` VALUES ('151', '1', '24');
INSERT INTO `rbac_group_info_permission` VALUES ('152', '1', '25');
INSERT INTO `rbac_group_info_permission` VALUES ('18', '1', '27');
INSERT INTO `rbac_group_info_permission` VALUES ('92', '1', '35');
INSERT INTO `rbac_group_info_permission` VALUES ('96', '1', '36');
INSERT INTO `rbac_group_info_permission` VALUES ('127', '1', '48');
INSERT INTO `rbac_group_info_permission` VALUES ('128', '1', '49');
INSERT INTO `rbac_group_info_permission` VALUES ('22', '2', '18');
INSERT INTO `rbac_group_info_permission` VALUES ('23', '2', '19');
INSERT INTO `rbac_group_info_permission` VALUES ('24', '2', '20');
INSERT INTO `rbac_group_info_permission` VALUES ('25', '2', '21');
INSERT INTO `rbac_group_info_permission` VALUES ('26', '2', '22');
INSERT INTO `rbac_group_info_permission` VALUES ('27', '2', '23');
INSERT INTO `rbac_group_info_permission` VALUES ('28', '2', '24');
INSERT INTO `rbac_group_info_permission` VALUES ('29', '2', '25');
INSERT INTO `rbac_group_info_permission` VALUES ('30', '2', '26');
INSERT INTO `rbac_group_info_permission` VALUES ('31', '2', '28');
INSERT INTO `rbac_group_info_permission` VALUES ('32', '2', '29');
INSERT INTO `rbac_group_info_permission` VALUES ('33', '2', '30');
INSERT INTO `rbac_group_info_permission` VALUES ('34', '2', '31');
INSERT INTO `rbac_group_info_permission` VALUES ('91', '2', '35');
INSERT INTO `rbac_group_info_permission` VALUES ('95', '2', '36');
INSERT INTO `rbac_group_info_permission` VALUES ('98', '2', '37');
INSERT INTO `rbac_group_info_permission` VALUES ('100', '2', '38');
INSERT INTO `rbac_group_info_permission` VALUES ('102', '2', '39');
INSERT INTO `rbac_group_info_permission` VALUES ('104', '2', '40');
INSERT INTO `rbac_group_info_permission` VALUES ('106', '2', '41');
INSERT INTO `rbac_group_info_permission` VALUES ('110', '2', '42');
INSERT INTO `rbac_group_info_permission` VALUES ('111', '2', '43');
INSERT INTO `rbac_group_info_permission` VALUES ('112', '2', '44');
INSERT INTO `rbac_group_info_permission` VALUES ('115', '2', '45');
INSERT INTO `rbac_group_info_permission` VALUES ('116', '2', '46');
INSERT INTO `rbac_group_info_permission` VALUES ('118', '2', '47');
INSERT INTO `rbac_group_info_permission` VALUES ('122', '2', '48');
INSERT INTO `rbac_group_info_permission` VALUES ('123', '2', '49');
INSERT INTO `rbac_group_info_permission` VALUES ('130', '2', '50');
INSERT INTO `rbac_group_info_permission` VALUES ('133', '2', '51');
INSERT INTO `rbac_group_info_permission` VALUES ('134', '2', '52');
INSERT INTO `rbac_group_info_permission` VALUES ('153', '2', '53');
INSERT INTO `rbac_group_info_permission` VALUES ('154', '2', '54');
INSERT INTO `rbac_group_info_permission` VALUES ('155', '2', '55');
INSERT INTO `rbac_group_info_permission` VALUES ('161', '2', '57');
INSERT INTO `rbac_group_info_permission` VALUES ('162', '2', '58');
INSERT INTO `rbac_group_info_permission` VALUES ('37', '3', '18');
INSERT INTO `rbac_group_info_permission` VALUES ('38', '3', '19');
INSERT INTO `rbac_group_info_permission` VALUES ('39', '3', '20');
INSERT INTO `rbac_group_info_permission` VALUES ('40', '3', '21');
INSERT INTO `rbac_group_info_permission` VALUES ('41', '3', '22');
INSERT INTO `rbac_group_info_permission` VALUES ('42', '3', '23');
INSERT INTO `rbac_group_info_permission` VALUES ('43', '3', '24');
INSERT INTO `rbac_group_info_permission` VALUES ('44', '3', '25');
INSERT INTO `rbac_group_info_permission` VALUES ('45', '3', '26');
INSERT INTO `rbac_group_info_permission` VALUES ('46', '3', '28');
INSERT INTO `rbac_group_info_permission` VALUES ('47', '3', '29');
INSERT INTO `rbac_group_info_permission` VALUES ('48', '3', '30');
INSERT INTO `rbac_group_info_permission` VALUES ('49', '3', '31');
INSERT INTO `rbac_group_info_permission` VALUES ('90', '3', '35');
INSERT INTO `rbac_group_info_permission` VALUES ('94', '3', '36');
INSERT INTO `rbac_group_info_permission` VALUES ('125', '3', '48');
INSERT INTO `rbac_group_info_permission` VALUES ('126', '3', '49');
INSERT INTO `rbac_group_info_permission` VALUES ('156', '3', '53');
INSERT INTO `rbac_group_info_permission` VALUES ('157', '3', '54');
INSERT INTO `rbac_group_info_permission` VALUES ('158', '3', '55');
INSERT INTO `rbac_group_info_permission` VALUES ('52', '4', '1');
INSERT INTO `rbac_group_info_permission` VALUES ('53', '4', '2');
INSERT INTO `rbac_group_info_permission` VALUES ('54', '4', '3');
INSERT INTO `rbac_group_info_permission` VALUES ('55', '4', '4');
INSERT INTO `rbac_group_info_permission` VALUES ('56', '4', '5');
INSERT INTO `rbac_group_info_permission` VALUES ('57', '4', '6');
INSERT INTO `rbac_group_info_permission` VALUES ('58', '4', '7');
INSERT INTO `rbac_group_info_permission` VALUES ('59', '4', '8');
INSERT INTO `rbac_group_info_permission` VALUES ('60', '4', '9');
INSERT INTO `rbac_group_info_permission` VALUES ('61', '4', '10');
INSERT INTO `rbac_group_info_permission` VALUES ('62', '4', '11');
INSERT INTO `rbac_group_info_permission` VALUES ('63', '4', '12');
INSERT INTO `rbac_group_info_permission` VALUES ('64', '4', '13');
INSERT INTO `rbac_group_info_permission` VALUES ('65', '4', '14');
INSERT INTO `rbac_group_info_permission` VALUES ('66', '4', '15');
INSERT INTO `rbac_group_info_permission` VALUES ('67', '4', '16');
INSERT INTO `rbac_group_info_permission` VALUES ('68', '4', '17');
INSERT INTO `rbac_group_info_permission` VALUES ('69', '4', '18');
INSERT INTO `rbac_group_info_permission` VALUES ('70', '4', '19');
INSERT INTO `rbac_group_info_permission` VALUES ('71', '4', '20');
INSERT INTO `rbac_group_info_permission` VALUES ('72', '4', '21');
INSERT INTO `rbac_group_info_permission` VALUES ('73', '4', '22');
INSERT INTO `rbac_group_info_permission` VALUES ('74', '4', '23');
INSERT INTO `rbac_group_info_permission` VALUES ('75', '4', '24');
INSERT INTO `rbac_group_info_permission` VALUES ('76', '4', '25');
INSERT INTO `rbac_group_info_permission` VALUES ('77', '4', '26');
INSERT INTO `rbac_group_info_permission` VALUES ('78', '4', '27');
INSERT INTO `rbac_group_info_permission` VALUES ('79', '4', '28');
INSERT INTO `rbac_group_info_permission` VALUES ('80', '4', '29');
INSERT INTO `rbac_group_info_permission` VALUES ('81', '4', '30');
INSERT INTO `rbac_group_info_permission` VALUES ('82', '4', '31');
INSERT INTO `rbac_group_info_permission` VALUES ('89', '4', '35');
INSERT INTO `rbac_group_info_permission` VALUES ('93', '4', '36');
INSERT INTO `rbac_group_info_permission` VALUES ('97', '4', '37');
INSERT INTO `rbac_group_info_permission` VALUES ('99', '4', '38');
INSERT INTO `rbac_group_info_permission` VALUES ('101', '4', '39');
INSERT INTO `rbac_group_info_permission` VALUES ('103', '4', '40');
INSERT INTO `rbac_group_info_permission` VALUES ('105', '4', '41');
INSERT INTO `rbac_group_info_permission` VALUES ('107', '4', '42');
INSERT INTO `rbac_group_info_permission` VALUES ('108', '4', '43');
INSERT INTO `rbac_group_info_permission` VALUES ('109', '4', '44');
INSERT INTO `rbac_group_info_permission` VALUES ('113', '4', '45');
INSERT INTO `rbac_group_info_permission` VALUES ('114', '4', '46');
INSERT INTO `rbac_group_info_permission` VALUES ('117', '4', '47');
INSERT INTO `rbac_group_info_permission` VALUES ('119', '4', '48');
INSERT INTO `rbac_group_info_permission` VALUES ('120', '4', '49');
INSERT INTO `rbac_group_info_permission` VALUES ('129', '4', '50');
INSERT INTO `rbac_group_info_permission` VALUES ('131', '4', '51');
INSERT INTO `rbac_group_info_permission` VALUES ('132', '4', '52');
INSERT INTO `rbac_group_info_permission` VALUES ('143', '4', '53');
INSERT INTO `rbac_group_info_permission` VALUES ('144', '4', '54');
INSERT INTO `rbac_group_info_permission` VALUES ('145', '4', '55');
INSERT INTO `rbac_group_info_permission` VALUES ('142', '4', '56');
INSERT INTO `rbac_group_info_permission` VALUES ('159', '4', '57');
INSERT INTO `rbac_group_info_permission` VALUES ('160', '4', '58');

-- ----------------------------
-- Table structure for `rbac_menu`
-- ----------------------------
DROP TABLE IF EXISTS `rbac_menu`;
CREATE TABLE `rbac_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_name` varchar(32) NOT NULL,
  `icon` varchar(32) DEFAULT NULL,
  `weight` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `menu_name` (`menu_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rbac_menu
-- ----------------------------
INSERT INTO `rbac_menu` VALUES ('1', '数据录入', 'glyphicon glyphicon-list-alt', '5');
INSERT INTO `rbac_menu` VALUES ('2', '数据审核', 'glyphicon glyphicon-search', '4');
INSERT INTO `rbac_menu` VALUES ('3', '测试分配', 'glyphicon glyphicon-retweet', '3');
INSERT INTO `rbac_menu` VALUES ('4', '结果查询', 'glyphicon glyphicon-folder-open', '2');
INSERT INTO `rbac_menu` VALUES ('5', '用户管理', 'glyphicon glyphicon-user', '1');

-- ----------------------------
-- Table structure for `rbac_permission_info`
-- ----------------------------
DROP TABLE IF EXISTS `rbac_permission_info`;
CREATE TABLE `rbac_permission_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `url` varchar(32) NOT NULL,
  `menu_name` varchar(32) DEFAULT NULL,
  `icon` varchar(32) DEFAULT NULL,
  `menu_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rbac_permission_info_menu_id_95766dae_fk_rbac_menu_id` (`menu_id`),
  KEY `rbac_permission_in_parent_id_5c48db64_fk_rbac_permission_info_id` (`parent_id`),
  CONSTRAINT `rbac_permission_in_parent_id_5c48db64_fk_rbac_permission_info_id` FOREIGN KEY (`parent_id`) REFERENCES `rbac_permission_info` (`id`),
  CONSTRAINT `rbac_permission_info_menu_id_95766dae_fk_rbac_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `rbac_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rbac_permission_info
-- ----------------------------
INSERT INTO `rbac_permission_info` VALUES ('1', '未提交的燃气表', '/data/', '编辑数据', 'glyphicon glyphicon-pencil', '1', null);
INSERT INTO `rbac_permission_info` VALUES ('2', '提交数据', '/submit/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('3', '数据录入', '/datainput/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('4', '录入IC卡-膜式表数据', '/datainput_ic_msb/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('5', '录入IC卡-修正仪数据', '/datainput_ic_xzy/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('6', '录入IC卡-超声波数据', '/datainput_ic_csb/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('7', '录入膜式表数据', '/datainput_msb/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('8', '录入修正仪数据', '/datainput_xzy/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('9', '录入超声波数据', '/datainput_csb/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('10', '删除数据', '/del_data/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('11', '修改数据', '/edit_data/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('12', '修改IC卡-膜式表数据', '/edit_ic_msb/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('13', '修改IC卡-修正仪数据', '/edit_ic_xzy/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('14', '修改IC卡-超声波数据', '/edit_ic_csb/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('15', '修改膜式表数据', '/edit_msb/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('16', '修改修正仪数据', '/edit_xzy/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('17', '修改超声波数据', '/edit_csb/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('18', '待审核的燃气表', '/datacheck/', '审核数据', 'glyphicon glyphicon-search', '2', null);
INSERT INTO `rbac_permission_info` VALUES ('19', '审核数据', '/check_data/', '', '', null, '18');
INSERT INTO `rbac_permission_info` VALUES ('20', '审核IC卡-膜式表数据', '/check_ic_msb/', '', '', null, '18');
INSERT INTO `rbac_permission_info` VALUES ('21', '审核IC卡-修正仪数据', '/check_ic_xzy/', '', '', null, '18');
INSERT INTO `rbac_permission_info` VALUES ('22', '审核IC卡-超声波数据', '/check_ic_csb/', '', '', null, '18');
INSERT INTO `rbac_permission_info` VALUES ('23', '审核膜式表数据', '/check_msb/', '', '', null, '18');
INSERT INTO `rbac_permission_info` VALUES ('24', '审核修正仪数据', '/check_xzy/', '', '', null, '18');
INSERT INTO `rbac_permission_info` VALUES ('25', '审核超声波数据', '/check_csb/', '', '', null, '18');
INSERT INTO `rbac_permission_info` VALUES ('26', '数据审核操作', '/check/', '', '', null, '18');
INSERT INTO `rbac_permission_info` VALUES ('27', '审核情况（厂商）', '/dataresult/', '审核情况', 'glyphicon glyphicon-list', '1', null);
INSERT INTO `rbac_permission_info` VALUES ('28', '审核结果（测试人员）', '/checkresult/', '审核结果', 'glyphicon glyphicon-list', '2', null);
INSERT INTO `rbac_permission_info` VALUES ('29', '待分配的燃气表', '/allocation/', '分配测试', 'glyphicon glyphicon-retweet', '3', null);
INSERT INTO `rbac_permission_info` VALUES ('30', '提交分配', '/sub_allocation/', '', '', null, '29');
INSERT INTO `rbac_permission_info` VALUES ('31', '分配结果', '/allo_result/', '分配结果', 'glyphicon glyphicon-list', '3', null);
INSERT INTO `rbac_permission_info` VALUES ('35', '测试进度', '/middle_result/', '测试进度', 'glyphicon glyphicon-tasks', '4', null);
INSERT INTO `rbac_permission_info` VALUES ('36', '最终测试结果', '/result/', '测试结果', 'glyphicon glyphicon-list', '4', null);
INSERT INTO `rbac_permission_info` VALUES ('37', '所有分组', '/group/', '分组管理', 'glyphicon glyphicon-cog', '5', null);
INSERT INTO `rbac_permission_info` VALUES ('38', '增加分组', '/group_add/', '', '', null, '37');
INSERT INTO `rbac_permission_info` VALUES ('39', '编辑分组', '/group_edit/', '', '', null, '37');
INSERT INTO `rbac_permission_info` VALUES ('40', '删除分组', '/group_del/', '', '', null, '37');
INSERT INTO `rbac_permission_info` VALUES ('41', '权限，菜单管理', '/manulist/', '权限管理', 'glyphicon glyphicon-cog', '5', null);
INSERT INTO `rbac_permission_info` VALUES ('42', '增加菜单，权限', '/manulist_add/', '', '', null, '41');
INSERT INTO `rbac_permission_info` VALUES ('43', '编辑菜单，权限', '/manulist_edit/', '', '', null, '41');
INSERT INTO `rbac_permission_info` VALUES ('44', '删除菜单、权限', '/manulist_del/', '', '', null, '41');
INSERT INTO `rbac_permission_info` VALUES ('45', '增加权限', '/permissionlist_add/', '', '', null, '41');
INSERT INTO `rbac_permission_info` VALUES ('46', '删除权限', '/permissionlist_del/', '', '', null, '41');
INSERT INTO `rbac_permission_info` VALUES ('47', '编辑权限', '/permissionlist_edit/', '', '', null, '41');
INSERT INTO `rbac_permission_info` VALUES ('48', '已登录用户信息', '/user/', '', '', null, null);
INSERT INTO `rbac_permission_info` VALUES ('49', '首页', '/index/', '', '', null, null);
INSERT INTO `rbac_permission_info` VALUES ('50', '添加用户', '/loginuser_add/', '', '', null, '41');
INSERT INTO `rbac_permission_info` VALUES ('51', '编辑用户', '/loginuser_edit/', '', '', null, '41');
INSERT INTO `rbac_permission_info` VALUES ('52', '删除用户', '/loginuser_del/', '', '', null, '41');
INSERT INTO `rbac_permission_info` VALUES ('53', '合格的表入库操作', '/storage/', '', '', null, '35');
INSERT INTO `rbac_permission_info` VALUES ('54', '删除无效的表', '/del_test/', '', '', null, '35');
INSERT INTO `rbac_permission_info` VALUES ('55', '退回审核结果', '/back/', '', '', null, '28');
INSERT INTO `rbac_permission_info` VALUES ('56', '再测按键', '/again_test/', '', '', null, '35');
INSERT INTO `rbac_permission_info` VALUES ('57', '导出excel', '/export_excel/', '', '', null, '1');
INSERT INTO `rbac_permission_info` VALUES ('58', '重置密码', '/pwd_reset/', '', '', null, '37');

-- ----------------------------
-- Table structure for `rbac_user_info`
-- ----------------------------
DROP TABLE IF EXISTS `rbac_user_info`;
CREATE TABLE `rbac_user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rbac_user_info
-- ----------------------------
INSERT INTO `rbac_user_info` VALUES ('1', 'manu01', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('2', 'manu02', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('3', 'manu03', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('4', 'manu04', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('5', 'manu05', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('6', 'manu06', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('7', 'manu07', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('8', 'manu08', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('9', 'manu09', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('10', 'manu10', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('11', 'manu11', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('12', 'manu12', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('13', 'manu13', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('14', 'manu14', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('15', 'manu15', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('16', 'manu16', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('17', 'manu17', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('18', 'manu18', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('19', 'manu19', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('20', 'manu20', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('21', 'manu21', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('22', 'manu22', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('23', 'manu23', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('24', 'manu24', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('25', 'manu25', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('26', 'manu26', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('27', 'manu27', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('28', 'manu28', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('29', 'manu29', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('30', 'manu30', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('31', 'manu31', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('32', 'manu32', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('33', 'manu33', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('34', 'manu34', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('35', 'manu35', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('36', 'manu36', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('37', 'manu37', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('38', 'manu38', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('39', 'wll', 'pbkdf2_sha256$24000$a$0tFTU+/CfpIf2DFufuBr/6NqCfteL8F1i187oV9uvpY=');
INSERT INTO `rbac_user_info` VALUES ('40', 'testmanager', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('41', 'testoperator1', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('42', 'testoperator2', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');
INSERT INTO `rbac_user_info` VALUES ('43', 'testoperator3', 'pbkdf2_sha256$24000$a$7fQZzsgx5BkmtU4hHuExl3MMTh0lmWUj/SlodwDqw7s=');

-- ----------------------------
-- Table structure for `rbac_user_info_group`
-- ----------------------------
DROP TABLE IF EXISTS `rbac_user_info_group`;
CREATE TABLE `rbac_user_info_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_info_id` int(11) NOT NULL,
  `group_info_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rbac_user_info_group_user_info_id_28424b79_uniq` (`user_info_id`,`group_info_id`),
  KEY `rbac_user_info_grou_group_info_id_824bdfb6_fk_rbac_group_info_id` (`group_info_id`),
  CONSTRAINT `rbac_user_info_grou_group_info_id_824bdfb6_fk_rbac_group_info_id` FOREIGN KEY (`group_info_id`) REFERENCES `rbac_group_info` (`id`),
  CONSTRAINT `rbac_user_info_group_user_info_id_3ac3a1c6_fk_rbac_user_info_id` FOREIGN KEY (`user_info_id`) REFERENCES `rbac_user_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rbac_user_info_group
-- ----------------------------
INSERT INTO `rbac_user_info_group` VALUES ('19', '1', '1');
INSERT INTO `rbac_user_info_group` VALUES ('20', '2', '1');
INSERT INTO `rbac_user_info_group` VALUES ('21', '3', '1');
INSERT INTO `rbac_user_info_group` VALUES ('22', '4', '1');
INSERT INTO `rbac_user_info_group` VALUES ('23', '5', '1');
INSERT INTO `rbac_user_info_group` VALUES ('24', '6', '1');
INSERT INTO `rbac_user_info_group` VALUES ('25', '7', '1');
INSERT INTO `rbac_user_info_group` VALUES ('26', '8', '1');
INSERT INTO `rbac_user_info_group` VALUES ('27', '9', '1');
INSERT INTO `rbac_user_info_group` VALUES ('28', '10', '1');
INSERT INTO `rbac_user_info_group` VALUES ('29', '11', '1');
INSERT INTO `rbac_user_info_group` VALUES ('30', '12', '1');
INSERT INTO `rbac_user_info_group` VALUES ('31', '13', '1');
INSERT INTO `rbac_user_info_group` VALUES ('32', '14', '1');
INSERT INTO `rbac_user_info_group` VALUES ('33', '15', '1');
INSERT INTO `rbac_user_info_group` VALUES ('34', '16', '1');
INSERT INTO `rbac_user_info_group` VALUES ('35', '17', '1');
INSERT INTO `rbac_user_info_group` VALUES ('36', '18', '1');
INSERT INTO `rbac_user_info_group` VALUES ('37', '19', '1');
INSERT INTO `rbac_user_info_group` VALUES ('38', '20', '1');
INSERT INTO `rbac_user_info_group` VALUES ('39', '21', '1');
INSERT INTO `rbac_user_info_group` VALUES ('40', '22', '1');
INSERT INTO `rbac_user_info_group` VALUES ('41', '23', '1');
INSERT INTO `rbac_user_info_group` VALUES ('42', '24', '1');
INSERT INTO `rbac_user_info_group` VALUES ('43', '25', '1');
INSERT INTO `rbac_user_info_group` VALUES ('18', '26', '1');
INSERT INTO `rbac_user_info_group` VALUES ('16', '27', '1');
INSERT INTO `rbac_user_info_group` VALUES ('17', '28', '1');
INSERT INTO `rbac_user_info_group` VALUES ('15', '29', '1');
INSERT INTO `rbac_user_info_group` VALUES ('14', '30', '1');
INSERT INTO `rbac_user_info_group` VALUES ('13', '31', '1');
INSERT INTO `rbac_user_info_group` VALUES ('12', '32', '1');
INSERT INTO `rbac_user_info_group` VALUES ('11', '33', '1');
INSERT INTO `rbac_user_info_group` VALUES ('10', '34', '1');
INSERT INTO `rbac_user_info_group` VALUES ('9', '35', '1');
INSERT INTO `rbac_user_info_group` VALUES ('8', '36', '1');
INSERT INTO `rbac_user_info_group` VALUES ('7', '37', '1');
INSERT INTO `rbac_user_info_group` VALUES ('6', '38', '1');
INSERT INTO `rbac_user_info_group` VALUES ('1', '39', '4');
INSERT INTO `rbac_user_info_group` VALUES ('2', '40', '2');
INSERT INTO `rbac_user_info_group` VALUES ('5', '41', '3');
INSERT INTO `rbac_user_info_group` VALUES ('4', '42', '3');
INSERT INTO `rbac_user_info_group` VALUES ('3', '43', '3');
