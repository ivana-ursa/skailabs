from flask import Flask, request, jsonify

app = Flask(__name__)

# REST endpoint that receives a POST request and calculates maximum number of interviews
@app.route('/optimal_scheduling', methods = ['POST'])
def get_max_number_of_interviews():
    try:
        data = request.get_json()

        # check if 'start_times' and 'end_times' exist in the JSON data 
        if 'start_times' not in data or 'end_times' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        
        start_times = data['start_times']
        end_times = data['end_times']

        # check if the number of 'start_times' and 'end_times' are equal
        if len(start_times) != len(end_times):
            return jsonify({'error': 'The number of start times is not equal to the number of end times'}), 400

        # calculate the maximum number of non-overlapping interviews
        max_interviews = calculate_max_inteviews(start_times, end_times)

        # return the result in JSON format
        return jsonify({'max_interviews': max_interviews}), 200
    
    except Exception as e:
        # return the error in JSON format
        return jsonify({'error': str(e)}), 500

# function that calculates the maximum number of non-overlapping interviews
def calculate_max_inteviews(start_times, end_times):
    # organize the data in the sorted list of tuples
    interviews = list(sorted(zip(start_times, end_times)))
    
    count = 0
    previous_end = -1 # set initial previous end time to a negative value
    
    # iterate through all interview intervals to find the number of non-overlapping interviews
    for start, end in interviews:
        if start >= previous_end: # check if the current interview starts after the previous interview ends
            count += 1 # increment the count of maximum interviews
            previous_end = end  # update the previous end time to the current end time
        else:
            previous_end = min(previous_end, end)   # update the previous end time to the smaller of the previous and current end time
   
    return count

if __name__ == '__main__':
    app.run(debug = True)