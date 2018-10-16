CREATE DATABASE IF NOT EXISTS event_testdb /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;

USE event_testdb;

CREATE TABLE IF NOT EXISTS events (
  event_id int(10) NOT NULL,
  user_id int (10) NOT NULL,
  event_date int(10) unsigned NOT NULL,
  meny_id int(10) unsigned NOT NULL,
  PRIMARY KEY (event_id),
  UNIQUE KEY event_id_UNIQUE (event_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

TRUNCATE events;

INSERT INTO events (event_id, user_id, event_date, meny_id) VALUES 
  (1, 1, Convert(DateTime,'20181026',112), 5),
  (2, 1, Convert(DateTime,'20181026',112), 3),
  (3, 2, Convert(DateTime,'20181126',112), 5),
  (4, 1, Convert(DateTime,'20181226',112), 6),
  (6, 1, Convert(DateTime,'20180926',112), 2),
  (7, 1, Convert(DateTime,'20181026',112), 6),
  (8, 1, Convert(DateTime,'20181026',112), 2);