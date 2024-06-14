from flask import Flask, request, render_template
from solution import Solution

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        heights = list(map(int, request.form.get('heights').split(',')))
        if len(heights) < 2 or len(heights) > 100000 or any(h < 0 or h > 10000 for h in heights):
            raise ValueError("Invalid input constraints.")
        solution = Solution()
        result = solution.maxArea(heights)
        return render_template('index.html', result=result, heights=request.form.get('heights'))
    except ValueError as e:
        print(f"Error: {str(e)}")  # Debug print
        return render_template('index.html', error=str(e), heights=request.form.get('heights'))

if __name__ == '__main__':
    app.run(debug=True)
