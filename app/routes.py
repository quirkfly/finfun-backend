from flask import Blueprint, request, jsonify
from .services.assistant import chat_with_assistant

assistant_bp = Blueprint('assistant', __name__)

@assistant_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Missing JSON payload'}), 400

    client_id = data.get('client_id')
    messages = data.get('messages')

    # Validate presence and type
    if not client_id:
        return jsonify({'error': 'Missing client_id'}), 400
    if not isinstance(messages, list) or not messages:
        return jsonify({'error': 'Missing or invalid messages'}), 400

    # Optionally, validate each message
    for msg in messages:
        if 'role' not in msg or 'message' not in msg:
            return jsonify({'error': 'Invalid message format'}), 400

    # Pass to assistant logic
    response = chat_with_assistant(client_id, messages)
    return jsonify({'reply': response})