from flask import render_template, request, jsonify
from db_manger import DBManager
from configs import app
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')
db_manager = DBManager('sivans')


@app.after_request
def cleanup(response):
    plt.close()
    return response


def handle_data(pico1, pico2):
    if pico2 == 4:
        return 0
    else:
        if pico1 == 4:
            return pico2
        return pico1 + pico2


def create_plot(data_history, max_ticks=8):
    if data_history[0] == {'error': 'data not found'}:
        plt.plot([0], [0], label='No data available')
        plt.xlabel("Date")
        plt.ylabel("Number of visitors")
        plt.title("Sivans line history - No data available")
    else:
        dates = [entry['date'] for entry in data_history]
        lengths = [entry['length'] for entry in data_history]

        plt.figure(figsize=(8, 8))
        plt.plot(dates, lengths)
        plt.xlabel("Date")
        plt.ylabel("Number of visitors")
        plt.title("Sivans line history")

        num_dates = len(dates)
        if num_dates > max_ticks:
            step_size = max(1, num_dates // max_ticks)
            step_size = min(step_size, 8)
            print(step_size, 10)
            plt.xticks(dates[::step_size], fontsize=5, rotation='vertical')

    image_path = "./static/graph.png"
    if os.path.exists(image_path):
        os.remove(image_path)
        print('Done')
    plt.savefig(image_path)
    plt.close()
    return image_path


# creates the main website route for the page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# posts the history of the line
@app.route('/data-history', methods=['POST'])
def history():
    if request.method == 'POST':
        weeks = int(request.json.get('data'))
        print(weeks)
        if isinstance(weeks, int):
            current_datetime = datetime.now()
            time_x_weeks_ago = current_datetime - timedelta(weeks=weeks)
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            formatted_date_x_weeks_ago = time_x_weeks_ago.strftime('%Y-%m-%d' +
                                                                   ' %H:%M:%S')

            data_history = db_manager.fetch(formatted_datetime,
                                            formatted_date_x_weeks_ago)

            image_path = create_plot(data_history, weeks)
            print('Sucess')
            # Return image path in JSON response
            return jsonify({'success': True, 'imagePath': image_path}), 200
        print('Error')
        return jsonify({'success': False, 'error': 406}), 406


@app.route('/history', methods=['GET', 'POST'])
def history_route():
    return render_template('historik.html')


# Page for javascript to get updates from the database
@app.route('/get_updates', methods=['GET'])
def get_new_data():
    try:
        data_db = db_manager.fetch()
        if data_db:
            print('Updating data')
            return jsonify(data_db)
        else:
            print('No data found')
            return jsonify({'error': 'No data found'})
    except Exception as e:
        print(f'Error while fetching: {e}')


data = {'pico1': 3, 'pico2': 3}


# Route to handle PATCH requests from pico
@app.route('/upload', methods=['PATCH', 'GET'])
def update_data():
    try:
        if request.method == 'PATCH':

            patch_data = request.get_json()

            # Update the data based on the received patch_data
            for key, value in patch_data.items():
                if key in data:
                    data[key] = value
            db_manager.insert_data(data['latest_computed_data'])

            # Return the updated data as JSON
            return jsonify({'success': True, 'data': data}), 200
    except Exception as e:
        # Handle exceptions appropriately
        print(f'Error updating data: {e}')
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
