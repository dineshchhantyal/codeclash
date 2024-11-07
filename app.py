from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import random
import pandas as pd
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample level data (basic setup for 2 levels)
def generate_gem_positions(num_gems):
    positions = set()
    while len(positions) < num_gems:
        x = random.randint(0, 4)
        y = random.randint(0, 5)

        if x == 0 and y == 0:
            continue
        positions.add((x, y))
    return list(positions)

levels = {
    1: {
        'name': 'Two Gems',
        'commands': ['move("right")', 'move("down")', 'move("right")'],
        'gems': 1,
        'gem_positions': [(0, 1)],
        'scale': 100
    },
    2: {
        'name': 'Three Gems',
        'commands': ['move("right")', 'move("down")', 'move("left")'],
        'gems': 1,
        'gem_positions': [(1, 1)],
        'scale': 100
    },
}



@app.route('/')
def home():
    leaderboard = pd.read_csv('static/leaderboard.csv')
    leaderboard = leaderboard.sort_values(by='score', ascending=False).head(10)

    leaderboard_dict = leaderboard.to_dict(orient='records')
    print(leaderboard_dict)
    return render_template('home.html', leaderboard=leaderboard_dict)

@app.route('/start', methods=['POST'])
def start():
    session['player_name'] = request.form['player_name']
    session['player_email'] = request.form['player_email']
    session['current_level'] = 1

    return redirect(url_for('level', level_id=1))

@app.route('/level/<level_id>')
def level(level_id):
    if 'player_name' not in session:
        return redirect(url_for('home'))

    # Generate levels with unpredictable gem positions for higher levels
    levels[level_id] = {
        'name': f'{level_id} Gems',
        'gems': int(level_id),
        'gem_positions': generate_gem_positions(int(level_id)),
        'scale': 100
    }

    level = levels.get(level_id)

    session['current_level'] = level_id
    return render_template('level.html', level=level, level_id=level_id, player_name=session['player_name'])

@app.route('/submit_moves/<int:level_id>', methods=['POST'])
def submit_moves(level_id):
    level = levels.get(level_id)
    moves = request.json.get('moves')

    print(moves)
    if moves == level['commands']:
        session['current_level'] = level_id + 1
        return jsonify({'status': 'success', 'message': 'Level complete! Moving to the next level.'}), 200
    else:
        return jsonify({'status': 'failure', 'message': 'Incorrect moves. Try again.'}), 400

@app.route('/reset')
def reset():
    leaderboard = pd.read_csv('static/leaderboard.csv')
    winner = False

    if session:
        print(session)
        player_df = pd.DataFrame([{'player_name': session['player_name'], 'player_email': session['player_email'],
                                   'score': session['current_level'], 'time': datetime.now()}])
        leaderboard = pd.concat([leaderboard, player_df])
        # make score as int
        leaderboard['score'] = leaderboard['score'].astype(int)
        leaderboard = leaderboard.sort_values(by='score', ascending=False).head(10)

        if not leaderboard.empty and session.get('player_name') == leaderboard.iloc[0]['player_name']:
            winner = True
        print(leaderboard)
        session.clear()

        leaderboard.to_csv('static/leaderboard.csv', index=False)


    leaderboard_dict = leaderboard.to_dict(orient='records')



    return render_template('leaderboard.html', leaderboard=leaderboard_dict, winner=winner)
    # redirect to home page

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')


if __name__ == '__main__':
    app.run(debug=True)
