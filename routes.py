from flask import Blueprint, jsonify, request

faq_blueprint = Blueprint('faq_blueprint', __name__)

# In-memory storage for FAQs (for now, you can later replace this with a database)
faqs = [
    {'id': 1, 'question': 'What is an apple?', 'answer': 'An apple a day keeps doctor away.😊'},
    {'id': 2, 'question': 'What is a banana?', 'answer': 'A banana is yellow coloured carbs rich fruit.'},
    {'id': 3, 'question': 'Which fruit is known as king of fruits?', 'answer': 'The correct answer for this question is obviously one, the OG, the legend of Fruits, MANGO👑.'},
    {'id': 4, 'question': 'What can fruits provide?', 'answer': 'Fruits provide essential vitamins, minerals, fiber, and antioxidants, which help boost immunity, improve digestion, and reduce the risk of chronic diseases'},
]

# Initialize next_id based on the highest ID present in the initial data
next_id = max(faq['id'] for faq in faqs) + 1 if faqs else 1

# Get all FAQs
@faq_blueprint.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

# Get a single FAQ by ID
@faq_blueprint.route('/faqs/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    faq = next((faq for faq in faqs if faq['id'] == faq_id), None)
    if faq:
        return jsonify(faq)
    else:
        return jsonify({'error': 'FAQ not found'}), 404

# Create a new FAQ
@faq_blueprint.route('/faqs', methods=['POST'])
def create_faq():
    global next_id
    new_faq = request.get_json()
    new_faq['id'] = next_id  # Assign the current next_id
    next_id += 1  # Increment the next_id for future entries
    faqs.append(new_faq)
    return jsonify(new_faq), 201

# Update an existing FAQ
@faq_blueprint.route('/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    faq = next((faq for faq in faqs if faq['id'] == faq_id), None)
    if faq:
        updated_data = request.get_json()
        faq.update(updated_data)
        return jsonify(faq)
    else:
        return jsonify({'error': 'FAQ not found'}), 404

# Delete an FAQ
@faq_blueprint.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    faq = next((faq for faq in faqs if faq['id'] == faq_id), None)
    if faq:
        faqs.remove(faq)
        return jsonify({'message': 'FAQ deleted successfully'})
    else:
        return jsonify({'error': 'FAQ not found'}), 404
