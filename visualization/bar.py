import sys
import flask
import json
import urllib
import csv

app = flask.Flask(__name__)
@app.route('/')
def default():
    return flask.render_template('bar_chart_depiction.html')

@app.route('/data/<char1>+<char2>+<char3>')
def create_data(char1, char2, char3):

    manner_data = [{},{},{}]
    placement_data = [{},{},{}]
    voice_data = [{},{},{}]


    files = [[],[],[]]

    files[0].append("../tagging/features/{}_manner.csv".format(char1))
    files[0].append("../tagging/features/{}_manner.csv".format(char2))
    files[0].append("../tagging/features/{}_manner.csv".format(char3))

    files[1].append("../tagging/features/{}_placement.csv".format(char1))
    files[1].append("../tagging/features/{}_placement.csv".format(char2))
    files[1].append("../tagging/features/{}_placement.csv".format(char3))

    files[2].append("../tagging/features/{}_voicing.csv".format(char1))
    files[2].append("../tagging/features/{}_voicing.csv".format(char2))
    files[2].append("../tagging/features/{}_voicing.csv".format(char3))

    manner_data[0]['character'] = char1
    manner_data[1]['character'] = char2
    manner_data[2]['character'] = char3

    placement_data[0]['character'] = char1
    placement_data[1]['character'] = char2
    placement_data[2]['character'] = char3
    #
    voice_data[0]['character'] = char1
    voice_data[1]['character'] = char2
    voice_data[2]['character'] = char3

    for i in range(3):
        manner_data[i]['total'] = 100
        placement_data[i]['total'] = 100
        voice_data[i]['total'] = 100

    for j in range(3):
        with open(files[0][j]) as manner_file:
            manner_reader = csv.DictReader(manner_file)
            for m_row in manner_reader:
                manner_data[j][m_row[('feature')]] = m_row[('percent')]

        with open(files[1][j]) as placement_file:
            placement_reader = csv.DictReader(placement_file)
            for p_row in placement_reader:
                placement_data[j][p_row.get('feature')] = p_row.get('percent')

        with open(files[2][j]) as voice_file:
            voice_reader = csv.DictReader(voice_file)
            for v_row in voice_reader:
                voice_data[j][v_row.get('feature')] = v_row.get('percent')

    return flask.jsonify({'manner':manner_data, 'placement':placement_data, 'voice':voice_data})

if __name__=='__main__':
    app.run(debug=True)
