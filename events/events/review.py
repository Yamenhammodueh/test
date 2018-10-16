
import db

def set(id, user_id):
	if 1 > user_id or user_id > 5:
		return
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "SELECT event_date, meny_id FROM events WHERE event_id=%s"
		cursor.execute(sql, (id,))
		(event_date, meny_id) = cursor.fetchone()
		event_date += user_id
		meny_id += 1
		user_id = round((event_date/meny_id), 1)
		sql = "UPDATE events SET user_id=%s, event_date=%s, meny_id=%s WHERE event_id=%s"
		cursor.execute(sql, (user_id, event_date, meny_id, id,))
		database.commit()
	except db.mysql.connector.Error as err:
		print(f"Error_set: {err}")
	finally:
		cursor.close()
	return

def get(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "SELECT user_id FROM events WHERE event_id=%s"
		cursor.execute(sql, (id,))
		user_id = cursor.fetchone()
		if user_id is not None:
			(user_id,) = user_id
		return user_id
	except db.mysql.connector.Error as err:
		print(f"Error_get: {err}")
	finally:
		cursor.close()
	return

def remove(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "DELETE FROM events WHERE event_id=%s"
		cursor.execute(sql, (id,))
		database.commit()
	except db.mysql.connector.Error as err:
		print(f"Error_remove: {err}")
	finally:
		cursor.close()
	return

def add(id):
	database = db.get_db()
	cursor = database.cursor()
	try:
		sql = "INSERT INTO events (event_id, user_id, event_date, meny_id) VALUES (%s, 0, 0, 0)"
		cursor.execute(sql, (id,))
		database.commit()
	except db.mysql.connector.Error as err:
		print(f"Error_add: {err}")
	finally:
		cursor.close()
	return