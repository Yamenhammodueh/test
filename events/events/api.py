from flask import (
	Flask, g, jsonify, make_response, request, abort, Blueprint
)
import user_id, db

bp = Blueprint('api',__name__,url_prefix='/api/1.0')

@bp.route('/test', methods=['GET'])
def test():
	dbb = db.get_db()
	print(f"TEST: {dbb}")
	return jsonify({'test': "Success!"})

@bp.route('/events/<string:event_id>', methods=['GET'])
def get_event_id(event_id):
	r = user_id.get(event_id)
	if r is None:
		abort(400)
	x = {
		'id': event_id,
		'user_id': r,
		'description': f"ID: {event_id} has the user_id {r}"
	}
	return jsonify(x)

@bp.route('/events', methods=['GET'])
def get_events():
   return jsonify({'events': 'N/A'})

@bp.route('/events/', methods=['PATCH'])
def set_event_id():
	if not request.json or not 'event_id' in request.json:
		abort(400)
	user_id.set(event_id, re)
	return jsonify({'ok': 'success'})

@bp.route('/events', methods=['POST'])
def add_event_id():
	user_id.add(event_id)
	return jsonify({'ok': 'success'})

@bp.route('/events/<string:event_id>', methods=['DELETE'])
def remove_event_id(event_id):
	user_id.remove(event_id)
	return jsonify({'ok': 'success'})

# Error handling:
@bp.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': {
		'code': 404,
		'message': "Some message.",
		'type': "The type of error."
	}}), 404)

@bp.errorhandler(400)
def none_type(error):
	return make_response(jsonify({
		'error': {
			'code': 400,
			'message': "The specified id does not exist.",
			'type': "MEH"
		}
	}))